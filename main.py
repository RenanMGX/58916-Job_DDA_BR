from Entities.sap import SAP, datetime, relativedelta
import os
import pandas as pd
from patrimar_dependencies.functions import P, Functions
from botcity.maestro import *  # type: ignore
from patrimar_dependencies.sharepointfolder import SharePointFolders

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
        path = sap.get_empresas()
        
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
            sap.dda_br(centro=empresa, date=(datetime.now() + relativedelta(days=1)))
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
    