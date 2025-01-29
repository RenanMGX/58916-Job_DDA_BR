from Entities.sap import SAP
import os
import pandas as pd
from Entities.dependencies.arguments import Arguments

class Execute:
    @staticmethod
    def start():
        sap = SAP()
        path = sap.get_empresas()
        
        df = pd.read_excel(path)
        lista_empresas = df['Empresa'].unique().tolist()
        
        del df
        os.unlink(path)
        
        for empresa in lista_empresas:
            sap.dda_br(centro=empresa)
            
        sap.fechar_sap()
        
if __name__ == "__main__":
    Arguments({
        "start": Execute.start
    })