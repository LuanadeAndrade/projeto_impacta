from typing import Type
from mypy_extensions import TypedDict

class consdataInterface(TypedDict, total=True):
    IDT_CSDT = int
    DES_CSDT = str
    IDT_TIPO_RESU = int

class EmpresasInterface(TypedDict, total=True):
    #Insira os campos do BD
    IDT_EMPR: int
    DES_EMPR: str
    COD_TIPO_EMPR: int

class PaiXFilhoInterface(TypedDict, total=True):
    #Insira os campos do BD
    IDT_EMPR_PAI: int
    IDT_EMPR_FILH: int

class ContasGerInterface(TypedDict, total=True):
    #Insira os campos do BD
    IDT_PLNO: int
    IDT_EMPR: int
    NUM_CONT_LOCL: int   
    NUM_CONT_PCI: int
    NUM_PREX: int
    NUM_SUFI: int
    NUM_REGR_VIRT_1: int
    NUM_REGR_VIRT_2: int
    NUM_REGR_VIRT_SEQU: int


class EmpresaxMoedaInterface(TypedDict, total=True):
    #Insira os campos do BD
    IDT_EMPR: int
    COD_ISO_MOED: str  

class filtroColetaInterface(TypedDict, total=True):
    #Insira os campos do BD
    IDT_SAID: int
    DES_SAID: str
    IDT_PAIS: int
    DES_BALN_DRE: str 
    DES_EXCE_BALN_DRE: str 
    IDT_SBCL: int 
    DES_EXCE_SBCL: str 
    IDT_PROD: int 
    DES_EXCE_PROD: str 
    IDT_CHAVE: int  

class prodSubcanaisInterface(TypedDict, total=True):
    #Insira os campos do BD
    COD_PROD_OPEL: int
    IDT_EMPR_CANA: int

class empDebInterface(TypedDict, total=True):
    #Insira os campos do BD
    IDT_EMPR: int
    DES_EMPR_CTBL: str
    COD_CONT_CRED_RESU: int
    COD_CONT_CRED_MARG: int
    COD_VRVL_GEEN_SALD: int
    COD_VRVL_GEEN_RESU: int
    DES_NOM_CANA: str
    COD_SBCL_DEBT: int
    COD_MULI: int
    COD_PROD_SLA: int
    COD_PROD_DELA: int

class empresaServicoInterface(TypedDict, total=True):
    #Insira os campos do BD
    IDT_EMPR_SERV: int
    IDT_EMPR_SBSO: int   
    
class servicoOrgaoInterface(TypedDict, total=True):
    #Insira os campos do BD
    IDT_SERV_ORGO: int
    IDT_SERV_SUB: int
    IDT_SERV_ORGO_EMPR: int

class contaFolhaInterface(TypedDict, total=True):
    #Insira os campos do BD
    IDT_PAIS: int
    COD_PROD: int
    IDT_CSDT: int
    IDT_SALD_ORIG: str
    IDT_CONT_RSTI_ORIG: str
    IDT_FOLH: int 

class contaDeltaInterface(TypedDict, total=True):
    #Insira os campos do BD
    DES_AJUS_DELA: str
    IDT_SAID: int
    IDT_EMPR: int
    IDT_CONT_DEBT: int
    IDT_SBCL_DEBT: int
    IDT_PESS_DEBT: str
    IDT_CONT_CRED: int
    IDT_SBCL_CRED: int


class prodSLAInterface(TypedDict, total=True):
    #Insira os campos do BD
    IDT_EMPR_SLA: int
    IDT_PROD_SLA: int

class codCustosInterface(TypedDict, total=True):
    #Insira os campos do BD
    DES_UNID: str
    COD_UNID: int
    IDT_EMPR: int
    COD_EVEN_BONU: int
    COD_EVEN_EXCT_BONU: int 
    IDT_CANA_COML_LOCL: int

class subcanalPfXPjInterface(TypedDict, total=True):
    #Insira os campos do BD
    IDT_SBCL: int
    DES_TIPO_ENTI: str

class ajusteUnidExternaGeralInterface(TypedDict, total=True):
    DES_AJUS: str
    COD_TIPO_AJUS: int
    COD_VRVL_GEEN_DEBT: int 
    COD_VRVL_GEEN_CRED: int
    COD_EMPR: int 
    COD_RATE: int 
    COD_SBCL_DEBT: int 
    COD_FOLH_DEBT: int  
    DES_MOED: str 

class ajusteProdFolhaInterface(TypedDict, total=True):
    
    COD_PROD = int 
    DES_PROD = str 
    COD_FOLH = int 
    DES_FOLH = str 
    COD_FAMI = int 
    DES_FAMI = str 
 
 