from Entities.sap import SAP, datetime, relativedelta
import os
import pandas as pd
from time import sleep
from patrimar_dependencies.functions import P, Functions
from botcity.maestro import *  # type: ignore
from patrimar_dependencies.sharepointfolder import SharePointFolders
import pywintypes

_SAP_MAX_RETRIES = 3
_SAP_RETRY_DELAY = 15  # segundos entre tentativas

class ExecuteAPP:
    @staticmethod
    def start(
        *,
        user:str,
        password:str,
        ambiente:str,
        maestro:BotMaestroSDK|None = None
    ):
        print(P("Iniciando execução do script..."))
        sap = SAP(
            user=user,
            password=password,
            ambiente=ambiente,
            maestro=maestro
        )
        path: str | None = None
        try:
            for attempt in range(1, _SAP_MAX_RETRIES + 1):
                try:
                    path = sap.get_empresas()
                    break
                except (ConnectionError, AttributeError) as e:
                    if attempt < _SAP_MAX_RETRIES:
                        print(P(f"Tentativa {attempt}/{_SAP_MAX_RETRIES} de conexão ao SAP falhou: {e}. Aguardando {_SAP_RETRY_DELAY}s..."))
                        sleep(_SAP_RETRY_DELAY)
                    else:
                        raise
        finally:
            sap.fechar_sap()

        if not path:
            raise RuntimeError("get_empresas() não retornou um caminho de arquivo válido.")

        print(P("Lendo arquivo de empresas..."))
        df = pd.read_excel(path)
        lista_empresas = df['Empresa'].unique().tolist()
        
        print(P(f"Total de empresas encontradas: {len(lista_empresas)}"))
        del df
        try:
            Functions.fechar_excel(path)
            os.unlink(path)
        except:
            pass
        
        print(P("Iniciando processamento das empresas..."))
        quantidade_empresas = len(lista_empresas)
        cont = 1
        for empresa in lista_empresas:
            print(P(f"Processando empresa {empresa} de {cont}/{quantidade_empresas}"))
            for attempt in range(1, _SAP_MAX_RETRIES + 1):
                try:
                    sap.dda_br(centro=str(empresa), date=(datetime.now() + relativedelta(days=1)))
                    break
                except pywintypes.com_error as e:
                    if attempt < _SAP_MAX_RETRIES:
                        print(P(f"Tentativa {attempt}/{_SAP_MAX_RETRIES} COM error em dda_br (empresa {empresa}): {e}. Reconectando em {_SAP_RETRY_DELAY}s..."))
                        del sap.session  # descarta objeto COM obsoleto para forçar reconexão
                        sleep(_SAP_RETRY_DELAY)
                    else:
                        raise
            cont += 1
            
        sap.fechar_sap()
        
        print(P("Processamento concluído!"))
        
if __name__ == "__main__":
    from patrimar_dependencies.credenciais import Credential
    
    crd:dict = Credential(
        path_raiz=SharePointFolders(r'RPA - Dados\CRD\.patrimar_rpa\credenciais').value,
        name_file="SAP_PRD"
    ).load()
    
    
    ExecuteAPP.start(
        user=crd['user'],
        password=crd['password'],
        ambiente=crd['ambiente'],
    )
    