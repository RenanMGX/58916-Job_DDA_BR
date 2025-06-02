from Entities.sap import SAP, datetime, relativedelta
import os
import pandas as pd
from Entities.dependencies.arguments import Arguments
from Entities.dependencies.functions import P, Functions

class Execute:
    @staticmethod
    def start():
        print(P("Iniciando execução do script..."))
        sap = SAP()
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
    Arguments({
        "start": Execute.start
    })