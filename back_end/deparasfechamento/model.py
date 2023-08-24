from sqlalchemy import Column, Integer, String, Boolean, Float, Date
from sqlalchemy.sql.expression import null, nullslast
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.type_api import NULLTYPE
from app import db
from .interface import *

#Carga Fechamento

#DEPARAS DO FECHAMENTO

class Consdata(db.Model):  # type: ignore

    __tablename__ = "TABE_FECM_CSDT"

    IDT_CSDT = Column(Integer(), primary_key=True) 
    DES_CSDT = Column(String(126))
    IDT_TIPO_RESU = Column(Integer()) 

    def update(self, changes: consdataInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
            'IDT_CSDT': self.IDT_CSDT,
            'DES_CSDT': self.DES_CSDT,
            'IDT_TIPO_RESU': self.IDT_TIPO_RESU
        }


class Empresas(db.Model):  # type: ignore
    __tablename__ = 'TABE_EMPR'
    #Insira os campos das tabelas, com as primary keys também 
    IDT_EMPR  = Column(Integer(), primary_key=True, nullable=False)
    DES_EMPR  = Column(String(125))
    COD_TIPO_EMPR = Column(Integer())
    #Altere o campo Interface...
    def update(self, changes: EmpresasInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
    
    #Altere o serialize com os mesmos campos da tabela
    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
            'IDT_EMPR': self.IDT_EMPR,
            'DES_EMPR': self.DES_EMPR,
            'COD_TIPO_EMPR': self.COD_TIPO_EMPR
        }


class PaiXFilho(db.Model):  # type: ignore
    __tablename__ = 'TABE_EMPR_PAI_FILH'
    #Insira os campos das tabelas, com as primary keys também 
    IDT_EMPR_PAI  = Column(Integer(), nullable=False)
    IDT_EMPR_FILH  = Column(Integer(), primary_key=True, nullable=False)

    #Altere o campo Interface...
    def update(self, changes: PaiXFilhoInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
    
    #Altere o serialize com os mesmos campos da tabela
    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
            'IDT_EMPR_PAI': self.IDT_EMPR_PAI,
            'IDT_EMPR_FILH': self.IDT_EMPR_FILH,
        }

class ContasGer(db.Model):  # type: ignore
    __tablename__ = 'TABE_FECM_REGR_GERR_PCI'
    #Insira os campos das tabelas, com as primary keys também 
    IDT_PLNO  = Column(Integer(), primary_key=True, nullable=False)
    IDT_EMPR  = Column(Integer(), primary_key=True, nullable=False)
    NUM_CONT_LOCL = Column(Integer(), nullable=False)
    NUM_CONT_PCI = Column(Integer(), nullable=False)
    NUM_PREX = Column(Integer(), nullable=False)
    NUM_SUFI = Column(Integer(), nullable=False)
    NUM_REGR_VIRT_1 = Column(Integer(), nullable=False)
    NUM_REGR_VIRT_2 = Column(Integer(), nullable=False)
    NUM_REGR_VIRT_SEQU = Column(Integer(), nullable=False)

    #Altere o campo Interface...
    def update(self, changes: ContasGerInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
    
    #Altere o serialize com os mesmos campos da tabela
    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
            'IDT_PLNO': self.IDT_PLNO,
            'IDT_EMPR': self.IDT_EMPR,
            'NUM_CONT_LOCL': self.NUM_CONT_LOCL,
            'NUM_CONT_PCI': self.NUM_CONT_PCI,
            'NUM_PREX': self. NUM_PREX,
            'NUM_SUFI': self.NUM_SUFI, 
            'NUM_REGR_VIRT_1': self.NUM_REGR_VIRT_1,
            'NUM_REGR_VIRT_2': self.NUM_REGR_VIRT_2 ,
            'NUM_REGR_VIRT_SEQU': self.NUM_REGR_VIRT_SEQU
        }  

class EmpresaxMoeda(db.Model):  # type: ignore
    __tablename__ = 'TABE_FECM_MAPE_EMPR_MOED'
    #Insira os campos das tabelas, com as primary keys também 
    IDT_EMPR  = Column(Integer(), primary_key=True, nullable=False)
    COD_ISO_MOED = Column(String(3))

    #Altere o campo Interface...
    def update(self, changes: EmpresaxMoedaInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
    
    #Altere o serialize com os mesmos campos da tabela
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
                'IDT_EMPR': self.IDT_EMPR,
                'COD_ISO_MOED': self.COD_ISO_MOED,
            }         

class filtroColeta(db.Model):  # type: ignore
    __tablename__ = 'TABE_FILT_CLET'
    #Insira os campos das tabelas, com as primary keys também 
    IDT_SAID  = Column(Integer(), nullable=False)
    DES_SAID = Column(String(100), nullable=False)
    IDT_PAIS = Column(Integer(), nullable=False)
    DES_BALN_DRE = Column(String(20))
    DES_EXCE_BALN_DRE = Column(String(20),nullable=False)
    IDT_SBCL = Column(Integer())
    DES_EXCE_SBCL = Column (String(20), nullable=False)
    IDT_PROD = Column(Integer())
    DES_EXCE_PROD = Column(String(20), nullable=False)
    IDT_CHAVE = Column(Integer(), primary_key=True, nullable=False)

    #Altere o campo Interface...
    def update(self, changes: filtroColetaInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
    
    #Altere o serialize com os mesmos campos da tabela
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
                'IDT_SAID': self.IDT_SAID, 
                'DES_SAID': self.DES_SAID, 
                'IDT_PAIS': self.IDT_PAIS,
                'DES_BALN_DRE': self.DES_BALN_DRE,
                'DES_EXCE_BALN_DRE': self.DES_EXCE_BALN_DRE,
                'IDT_SBCL': self.IDT_SBCL,
                'DES_EXCE_SBCL': self.DES_EXCE_SBCL,
                'IDT_PROD': self.IDT_PROD,
                'DES_EXCE_PROD': self.DES_EXCE_PROD,
                'IDT_CHAVE': self.IDT_CHAVE
            }  
    
#DEPARAS DA CARGA RECEITA

class prodSubcanais(db.Model):  # type: ignore
    __tablename__ = 'TABE_CARG_FECM_PROD_OPEL_EMPR'
    #Insira os campos das tabelas, com as primary keys também 
    COD_PROD_OPEL  = Column(Integer(), primary_key=True, nullable=False)
    IDT_EMPR_CANA = Column(Integer(), primary_key=True, nullable=False)

    #Altere o campo Interface...
    def update(self, changes: prodSubcanaisInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
    
    #Altere o serialize com os mesmos campos da tabela
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
                'COD_PROD_OPEL': self.COD_PROD_OPEL,
                'IDT_EMPR_CANA': self.IDT_EMPR_CANA
        }   

class empDeb(db.Model):  # type: ignore
    __tablename__ = 'TABE_CARG_FECM_EMPR_GEEN_DP'
    #Insira os campos das tabelas, com as primary keys também 
    IDT_EMPR  = Column(Integer(), nullable=False)
    DES_EMPR_CTBL = Column(String(100), nullable=False, primary_key=True)
    COD_CONT_CRED_RESU = Column(Integer(), nullable=False)
    COD_CONT_CRED_MARG = Column(Integer(), nullable=False)
    COD_VRVL_GEEN_SALD = Column(Integer(), nullable=False)
    COD_VRVL_GEEN_RESU = Column(Integer(), nullable=False)
    DES_NOM_CANA = Column (String(30), nullable=False)
    COD_SBCL_DEBT = Column(Integer(), nullable=False)
    COD_MULI = Column(Integer(), nullable=False)
    COD_PROD_SLA = Column(Integer(), nullable=False)
    COD_PROD_DELA = Column(Integer(), nullable=False)

    #Altere o campo Interface...
    def update(self, changes: empDebInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
    
    #Altere o serialize com os mesmos campos da tabela
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
                'IDT_EMPR': self.IDT_EMPR, 
                'DES_EMPR_CTBL': self.DES_EMPR_CTBL, 
                'COD_CONT_CRED_RESU': self.COD_CONT_CRED_RESU,
                'COD_CONT_CRED_MARG': self.COD_CONT_CRED_MARG,
                'COD_VRVL_GEEN_SALD': self.COD_VRVL_GEEN_SALD,
                'COD_VRVL_GEEN_RESU': self.COD_VRVL_GEEN_RESU,
                'DES_NOM_CANA': self.DES_NOM_CANA,
                'COD_SBCL_DEBT': self.COD_SBCL_DEBT,
                'COD_MULI': self.COD_MULI,
                'COD_PROD_SLA': self.COD_PROD_SLA,
                'COD_PROD_DELA': self.COD_PROD_DELA
            }   

class empresaServico(db.Model):  # type: ignore
    __tablename__ = 'TABE_CARG_FECM_EMPR_SERV'
    #Insira os campos das tabelas, com as primary keys também 
    IDT_EMPR_SERV  = Column(Integer(), primary_key=True, nullable=False)
    IDT_EMPR_SBSO = Column(Integer(), nullable=False)

    #Altere o campo Interface...
    def update(self, changes: empresaServicoInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
    
    #Altere o serialize com os mesmos campos da tabela
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
                'IDT_EMPR_SERV': self.IDT_EMPR_SERV,
                'IDT_EMPR_SBSO': self.IDT_EMPR_SBSO
        }   

class servicoOrgao(db.Model):  # type: ignore
    __tablename__ = 'TABE_CARG_FECM_SERV_ORGO'
    #Insira os campos das tabelas, com as primary keys também 
    IDT_SERV_ORGO  = Column(Integer(),primary_key=True, nullable=False)
    IDT_SERV_SUB = Column(Integer(),primary_key=True, nullable=False)
    IDT_SERV_ORGO_EMPR = Column(Integer(),primary_key=True, nullable=False)

    #Altere o campo Interface...
    def update(self, changes: servicoOrgaoInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
    
    #Altere o serialize com os mesmos campos da tabela
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
                'IDT_SERV_ORGO': self.IDT_SERV_ORGO,
                'IDT_SERV_SUB': self.IDT_SERV_SUB,
                'IDT_SERV_ORGO_EMPR': self.IDT_SERV_ORGO_EMPR
        }  


class contaFolha(db.Model):  # type: ignore
    __tablename__ = 'TABE_CARG_FECM_PROD_CONT_FOLH'
    #Insira os campos das tabelas, com as primary keys também 
    IDT_PAIS  = Column(Integer(), primary_key=True, nullable=False)
    COD_PROD = Column(Integer(), primary_key=True, nullable=False)
    IDT_CSDT = Column(Integer())
    IDT_SALD_ORIG = Column(String(20))
    IDT_CONT_RSTI_ORIG = Column(String(20))
    IDT_FOLH = Column(Integer())

    #Altere o campo Interface...
    def update(self, changes: contaFolhaInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
    
    #Altere o serialize com os mesmos campos da tabela
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
                'IDT_PAIS': self.IDT_PAIS,
                'COD_PROD': self.COD_PROD,
                'IDT_CSDT': self.IDT_CSDT,
                'IDT_SALD_ORIG': self.IDT_SALD_ORIG,
                'IDT_CONT_RSTI_ORIG': self.IDT_CONT_RSTI_ORIG,
                'IDT_FOLH': self.IDT_FOLH
        }       


class contaDelta(db.Model):  # type: ignore
    __tablename__ = 'TABE_CARG_FECM_DELA'
    #Insira os campos das tabelas, com as primary keys também 
    DES_AJUS_DELA = Column(String(20))
    IDT_SAID =  Column(Integer(), primary_key=True, nullable=False)
    IDT_EMPR =  Column(Integer(), primary_key=True, nullable=False)
    IDT_CONT_DEBT = Column(Integer())
    IDT_SBCL_DEBT = Column(Integer())
    IDT_PESS_DEBT = Column(String(1))
    IDT_CONT_CRED = Column(Integer())
    IDT_SBCL_CRED = Column(Integer())

    #Altere o campo Interface...
    def update(self, changes: contaDeltaInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
    
    #Altere o serialize com os mesmos campos da tabela
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
                'DES_AJUS_DELA': self.DES_AJUS_DELA,
                'IDT_SAID': self.IDT_SAID,
                'IDT_EMPR': self.IDT_EMPR,
                'IDT_CONT_DEBT': self.IDT_CONT_DEBT,
                'IDT_SBCL_DEBT': self.IDT_SBCL_DEBT,
                'IDT_PESS_DEBT': self.IDT_PESS_DEBT,
                'IDT_CONT_CRED': self.IDT_CONT_CRED,
                'IDT_SBCL_CRED': self.IDT_SBCL_CRED
        }   

#DEPARAS DA CARGA CUSTO        

class prodSLA(db.Model):  # type: ignore
    __tablename__ = 'TABE_FECM_BONU_EMPR_PROD'
    #Insira os campos das tabelas, com as primary keys também 
    IDT_EMPR_SLA  = Column(Integer(), primary_key=True, nullable=False)
    IDT_PROD_SLA = Column(Integer(), primary_key=True, nullable=False)

    #Altere o campo Interface...
    def update(self, changes: prodSLAInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
    
    #Altere o serialize com os mesmos campos da tabela
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
                'IDT_EMPR_SLA': self.IDT_EMPR_SLA,
                'IDT_PROD_SLA': self.IDT_PROD_SLA
        }  

class codCustos(db.Model):  # type: ignore
    __tablename__ = 'TABE_FECM_BONU_UNID_EVEN'
    
    DES_UNID = Column(String(3))
    COD_UNID = Column(Integer(), primary_key=True, nullable=False)
    IDT_EMPR = Column(Integer(), nullable=False)
    COD_EVEN_BONU = Column(Integer(), nullable=False)
    COD_EVEN_EXCT_BONU = Column(Integer(), nullable=False)
    IDT_CANA_COML_LOCL = Column(Integer(), nullable=False)
    
    #Altere o campo Interface...
    def update(self, changes: codCustosInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
    
    #Altere o serialize com os mesmos campos da tabela
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
                'DES_UNID': self.DES_UNID,
                'COD_UNID': self.COD_UNID,
                'IDT_EMPR': self.IDT_EMPR,
                'COD_EVEN_BONU': self.COD_EVEN_BONU,
                'COD_EVEN_EXCT_BONU': self.COD_EVEN_EXCT_BONU,
                'IDT_CANA_COML_LOCL': self.IDT_CANA_COML_LOCL
        }  

class subcanalPfXPj(db.Model):  # type: ignore
    __tablename__ = 'TABE_FECM_BONU_SBCL'
    
    IDT_SBCL = Column(Integer(), primary_key=True, nullable=False)
    DES_TIPO_ENTI = Column(String(1), nullable=False)
    
    #Altere o campo Interface...
    def update(self, changes: subcanalPfXPjInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
    
    #Altere o serialize com os mesmos campos da tabela
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
                'IDT_SBCL': self.IDT_SBCL,
                'DES_TIPO_ENTI': self.DES_TIPO_ENTI,
        }  

#DEPARAS AJUSTES
# return {
#                 'DES_UNID': self.DES_UNID,
#                 'COD_UNID': self.COD_UNID,
#                 'IDT_EMPR': self.IDT_EMPR,
#                 'COD_EVEN_BONU': self.COD_EVEN_BONU,
#                 'COD_EVEN_EXCT_BONU': self.COD_EVEN_EXCT_BONU,
#                 'IDT_CANA_COML_LOCL': self.IDT_CANA_COML_LOCL
#         }  

# #Altere o campo Interface...
#     def update(self, changes: subcanalPfXPjInterface):
#         for key, val in changes.items():
#             setattr(self, key, val)
#         return self
    

class ajusteUnidExternaGeral(db.Model):  # type: ignore
    __tablename__ = 'TABE_FECM_AJUS_UNID_EXTO_GERL'
    
    DES_AJUS = Column(String(100))
    COD_TIPO_AJUS = Column(Integer(), nullable=False, primary_key=True)
    COD_VRVL_GEEN_DEBT = Column(Integer())
    COD_VRVL_GEEN_CRED = Column(Integer())
    COD_EMPR = Column(Integer(), nullable=False)
    COD_RATE = Column(Integer())
    COD_SBCL_DEBT = Column(Integer())
    COD_FOLH_DEBT = Column(Integer())
    DES_MOED = Column(String(3))

    #Altere o campo Interface...
    def update(self, changes: ajusteUnidExternaGeralInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
    
    #Altere o serialize com os mesmos campos da tabela
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
                'DES_AJUS': self.DES_AJUS,
                'COD_TIPO_AJUS': self.COD_TIPO_AJUS,
                'COD_VRVL_GEEN_DEBT': self.COD_VRVL_GEEN_DEBT,
                'COD_VRVL_GEEN_CRED': self.COD_VRVL_GEEN_CRED,
                'COD_EMPR': self.COD_EMPR,
                'COD_RATE': self.COD_RATE,
                'COD_SBCL_DEBT': self.COD_SBCL_DEBT,
                'COD_FOLH_DEBT': self.COD_FOLH_DEBT,
                'DES_MOED': self.DES_MOED    
        }  

class ajusteProdFolha(db.Model):  # type: ignore
    __tablename__ = 'TABE_FECM_AJUS_PROD_FOLH'

    COD_PROD = Column (Integer(), primary_key=True) 
    DES_PROD = Column(String(100), nullable=True)
    COD_FOLH = Column(Integer(), primary_key=True)
    DES_FOLH =  Column(String(100), nullable=True)
    COD_FAMI = Column(Integer(), primary_key=True)
    DES_FAMI = Column(String(100), nullable= True)
    
    
    #Altere o campo Interface...
    def update(self, changes: ajusteProdFolhaInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self

    #Altere o serialize com os mesmos campos da tabela
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
                'COD_PROD': self.COD_PROD,
                'DES_PROD': self.DES_PROD,
                'COD_FOLH': self.COD_FOLH,
                'DES_FOLH': self.DES_FOLH,
                'COD_FAMI': self.COD_FAMI,
                'DES_FAMI': self.DES_FAMI    
        }  