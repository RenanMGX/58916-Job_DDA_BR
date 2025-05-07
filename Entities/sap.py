from dependencies.sap import SAPManipulation
from dependencies.config import Config
from dependencies.logs import Logs
from dependencies.credenciais import Credential
from dependencies.functions import Functions, P
from datetime import datetime
from dateutil.relativedelta import relativedelta
from time import sleep
import os

class SAP(SAPManipulation):
    def __init__(self):
        crd:dict = Credential(Config()['credenciais']['sap']).load()
        
        super().__init__(user=crd['user'], password=crd['password'], ambiente=crd['ambiente'])
    
    @SAPManipulation.start_SAP
    def get_empresas(self):
        path = os.path.join(f"C:\\Users\\{os.getlogin()}\\Downloads", datetime.now().strftime("%Y%m%d%H%M%S_relatorio_empresas.xlsx"))
        
        self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n ZFI006"
        self.session.findById("wnd[0]").sendVKey(0)
        try:
            self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        except:
            pass

        self.session.findById("wnd[0]").sendVKey(13)
        
        self.session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").contextMenu()
        self.session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell/shellcont[1]/shell").selectContextMenuItem("&XXL")
        
        self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        self.session.findById("wnd[1]/usr/ctxtDY_PATH").text = os.path.dirname(path)
        self.session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = os.path.basename(path)
        self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        
        sleep(5)

        Functions.fechar_excel(path)
        
        self.fechar_sap()
        
        return path

    @SAPManipulation.start_SAP
    def dda_br(self, *, centro:str, date) -> bool:

        self.session.findById("wnd[0]/tbar[0]/okcd").text = "/n dda_br"
        self.session.findById("wnd[0]").sendVKey(0)
        
        self.session.findById("wnd[0]/usr/ctxtS_BUKRS").text = centro
        
        self.session.findById("wnd[0]/usr/txtS_GJAHR").text = date.year
        
        self.session.findById("wnd[0]/usr/ctxtS_DATE-LOW").text = date.strftime("%d.%m.%Y")
        self.session.findById("wnd[0]/usr/ctxtS_DATE-HIGH").text = (date + relativedelta(days=30)).strftime("%d.%m.%Y")
        
        self.session.findById("wnd[0]/usr/ctxtP_STATUS-LOW").text = "E"
        
        self.session.findById("wnd[0]/tbar[1]/btn[8]").press()

        self.session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").selectAll()
        self.session.findById("wnd[0]/tbar[1]/btn[7]").press()
        
        if (tbar:=self.session.findById("wnd[0]/sbar/pane[0]").text):
            print(P(tbar))
            Logs().register(status='Report', description=str(tbar))
            return True
        else:
            print(P("Nenhum DDA alterado."))
            return False
        
    
    @SAPManipulation.start_SAP
    def teste(self):
        print("finalizou")
    
        

if __name__ == "__main__":
    pass
