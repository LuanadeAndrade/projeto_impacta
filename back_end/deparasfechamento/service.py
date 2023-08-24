import os
import getpass
#import pymssql
import time
from flask import request, jsonify, send_file,Response
import pandas as pd
import json
from typing import List
from flask.json import load
from app import db

from .model import *

class deparaService:

       # FECHAMENTO

       # DEPARA EMPRESAS
       #Get all
       @staticmethod
       def allEmpresas() -> List[Empresas]:
              #puxando todos os campos do depara empresas
              return [item.serialize for item in Empresas.query.all()], 200
       
       #Create Empresa
       @staticmethod
       def createEmpresa() -> List[Empresas]:
              # Leitura dos dados de input
              input_form = request.get_json()

              # Tratamento nos dados de input
              idt_empresa = input_form['idt_empresa']
              desc_empresa = input_form['desc_empresa']
              tipo_empresa = input_form['tipo_empresa']

              #cirando DF com campos ara inserção
              df = pd.DataFrame({'IDT_EMPR': [int(idt_empresa)], 'DES_EMPR': [desc_empresa], 'COD_TIPO_EMPR': [tipo_empresa]})

              df.to_sql(Empresas.__tablename__, con=db.engine, if_exists='append', index=False,method='multi', chunksize=100)

              return input_form, 200
       
       #Delete Empresa
       @staticmethod
       def deleteEmpresa() -> List[Empresas]:
              input_form = request.get_json()

              empresa = input_form['empresa']

              #Nessa area fazemos primeiro uma consulta para achar uma linha para a exclusão,
              #Insira os campos para filtrar
              #db.session.query(Cosif).filter_by(COD=cod, COD_MODA=moda).delete()  
              db.session.query(Empresas).filter_by(IDT_EMPR=empresa).delete()    
              db.session.commit()
       
       #Update Empresa
       @staticmethod
       def updateEmpresa() -> List[Empresas]:
              input_form = request.get_json()

              #campos
              idt_empresa = input_form['idt_empresa']
              desc_empresa = input_form['desc_empresa']
              tipo_empresa = input_form['tipo_empresa']
              #Basicamente o comando filtra uma linha especifica, e depois altera seus campos com base em chave : Valor
              rows_changed = Empresas.query.filter_by(IDT_EMPR=idt_empresa).update(dict(IDT_EMPR = idt_empresa, DES_EMPR = desc_empresa, COD_TIPO_EMPR=tipo_empresa))
              db.session.commit()
              return rows_changed, 200
              ####### Fim Apelido

       # DEPARA CONSDATAS
       #Get all
       @staticmethod
       def allConsdata() -> List[Consdata]:
              #puxando todos os campos do depara empresas
              return [item.serialize for item in Consdata.query.all()], 200
       
       # Create Consdatas
       @staticmethod
       def createConsdata() -> List[Consdata]:
              # Leitura dos dados de input
              input_form = request.get_json()
              
              # Tratamento nos dados de input
              idt = input_form['cod']
              desc =  input_form['des']
              tipo =  input_form['tipo']
              
              #criando DF com campos para inserção
              df = pd.DataFrame({'IDT_CSDT': [int(idt)], 'DES_CSDT': [str(desc)], 'IDT_TIPO_RESU': [int(tipo)]})

              df.to_sql(Consdata.__tablename__, con=db.engine, if_exists='append', index=False,method='multi', chunksize=100)

              return input_form, 200
       
       # Update Consdatas
       @staticmethod
       def updateConsdata() -> List[Consdata]:
              input_form = request.get_json()

              #campos
              idt = input_form['cod']
              desc =  input_form['des']
              tipo =  input_form['tipo']
              
              #
              #Basicamente o comando filtra uma linha especifica, e depois altera seus campos com base em chave : Valor
              rows_changed = Consdata.query.filter_by(IDT_CSDT = idt).update(dict(IDT_CSDT = idt, DES_CSDT = desc, IDT_TIPO_RESU = tipo))
              db.session.commit()
              return rows_changed, 200
       
       #Delete Consdatas
       @staticmethod
       def deleteConsdata() -> List[Consdata]:
              input_form = request.get_json()

              id = input_form['cod']

              #
              #Nessa area fazemos primeiro uma consulta para achar uma linha para a exclusão,
              #Insira os campos para filtrar
              #db.session.query(Cosif).filter_by(COD=cod, COD_MODA=moda).delete()  
              db.session.query(Consdata).filter_by(IDT_CSDT=id).delete()    
              db.session.commit()   
              #FIM 

       
       # DEPARA PAI X FILHO
       #Get all
       @staticmethod
       def allPaiFilho() -> List[PaiXFilho]:
              #puxando todos os campos do depara empresas
              return [item.serialize for item in PaiXFilho.query.all()], 200
       
       #Create Pai Filho
       @staticmethod
       def createPaiFilho() -> List[PaiXFilho]:
              # Leitura dos dados de input
              input_form = request.get_json()

              # Tratamento nos dados de input
              empr_pai = input_form['empr_pai']
              empr_filho = input_form['empr_filho']
              
              #cirando DF com campos ara inserção
              df = pd.DataFrame({'IDT_EMPR_PAI': [int(empr_pai)], 'IDT_EMPR_FILH': [int(empr_filho)]})

              df.to_sql(PaiXFilho.__tablename__, con=db.engine, if_exists='append', index=False,method='multi', chunksize=100)

              return input_form, 200
       
       #Delete Pai Filho
       @staticmethod
       def deletePaiFilho() -> List[PaiXFilho]:
              input_form = request.get_json()

              empr_filho = input_form['empr_filho']

              #Nessa area fazemos primeiro uma consulta para achar uma linha para a exclusão,
              #Insira os campos para filtrar
              #db.session.query(Cosif).filter_by(COD=cod, COD_MODA=moda).delete()  
              db.session.query(PaiXFilho).filter_by(IDT_EMPR_FILH=empr_filho).delete()    
              db.session.commit()

        #Update Pai x Filho
       @staticmethod
       def updatePaiFilho() -> List[PaiXFilho]:
              input_form = request.get_json()

              #campos
              empr_pai = input_form['empr_pai']
              empr_filho = input_form['empr_filho']
       
              #Basicamente o comando filtra uma linha especifica, e depois altera seus campos com base em chave : Valor
              rows_changed = PaiXFilho.query.filter_by(IDT_EMPR_FILH=empr_filho).update(dict(IDT_EMPR_PAI = empr_pai))
              db.session.commit()
              return rows_changed, 200
              ####### Fim Empresa x Moeda          

       # DEPARA CONSTAS GERENCIAIS
       #Get all
       @staticmethod
       def allContasGer() -> List[ContasGer]:
              #puxando todos os campos do depara contas gerenciais
              return [item.serialize for item in ContasGer.query.all()], 200     

       # Create Contas Gerenciais
       @staticmethod
       def createContasGer() -> List[ContasGer]:
              # Leitura dos dados de input
              input_form = request.get_json()

              # Tratamento nos dados de input
              idt_plano = input_form['idt_plano']
              idt_empresa = input_form['idt_empresa']
              num_conta_local = input_form['num_conta_local']
              num_conta_pci = input_form['num_conta_pci']
              dig_prefixo = input_form['dig_prefixo']
              dig_sufixo = input_form['dig_sufixo']
              qtd_dig_esquerda = input_form['qtd_dig_esquerda']
              qtd_dig_direita = input_form['qtd_dig_direita']
              qtd_dig_incrementais = input_form['qtd_dig_incrementais']

              #criando DF com campos para inserção
              df = pd.DataFrame({'IDT_PLNO': [int(idt_plano)], 'IDT_EMPR': [int(idt_empresa)], 'NUM_CONT_LOCL': [int(num_conta_local)], 'NUM_CONT_PCI': [int(num_conta_pci)], 'NUM_PREX': [int(dig_prefixo)], 'NUM_SUFI': [int(dig_sufixo)], 'NUM_REGR_VIRT_1': [int(qtd_dig_esquerda)], 'NUM_REGR_VIRT_2': [int(qtd_dig_direita)], 'NUM_REGR_VIRT_SEQU': [int(qtd_dig_incrementais)]})

              df.to_sql(ContasGer.__tablename__, con=db.engine, if_exists='append', index=False,method='multi', chunksize=100)

              return input_form, 200

       #Delete Contas Gerenciais
       @staticmethod
       def deleteContasGer() -> List[ContasGer]:
              input_form = request.get_json()

              idt_plano = input_form['plano']
              idt_empresa = input_form['empresa']

              #Nessa area fazemos primeiro uma consulta para achar uma linha para a exclusão,
              #Insira os campos para filtrar
              #db.session.query(Cosif).filter_by(COD=cod, COD_MODA=moda).delete()  
              db.session.query(ContasGer).filter_by(IDT_PLNO=idt_plano, IDT_EMPR=idt_empresa).delete()    
              db.session.commit()

        #Update Contas Gerenciais
       @staticmethod
       def updateContasGer() -> List[ContasGer]:
              input_form = request.get_json()

              #campos
              idt_plano = input_form['idt_plano']
              idt_empresa = input_form['idt_empresa']
              num_conta_local = input_form['num_conta_local']
              num_conta_pci = input_form['num_conta_pci']
              dig_prefixo = input_form['dig_prefixo']
              dig_sufixo = input_form['dig_sufixo']
              qtd_dig_esquerda = input_form['qtd_dig_esquerda']
              qtd_dig_direita = input_form['qtd_dig_direita']
              qtd_dig_incrementais = input_form['qtd_dig_incrementais']
              #Basicamente o comando filtra uma linha especifica, e depois altera seus campos com base em chave : Valor
              rows_changed = ContasGer.query.filter_by(IDT_EMPR=idt_empresa, IDT_PLNO=idt_plano).update(dict(NUM_CONT_LOCL = num_conta_local, NUM_CONT_PCI=num_conta_pci, NUM_PREX=dig_prefixo, NUM_SUFI=dig_sufixo, NUM_REGR_VIRT_1=qtd_dig_esquerda, NUM_REGR_VIRT_2=qtd_dig_direita, NUM_REGR_VIRT_SEQU=qtd_dig_incrementais))
              db.session.commit()
              return rows_changed, 200
              ####### Fim Contas Ger      

        # DEPARA EMPRESA X MOEDA
       #Get all
       @staticmethod
       def allEmpresaxMoeda() -> List[EmpresaxMoeda]:
              #puxando todos os campos do depara contas gerenciais
              return [item.serialize for item in EmpresaxMoeda.query.all()], 200     

        # Create Empresa x Moeda
       @staticmethod
       def createEmpresaxMoeda() -> List[EmpresaxMoeda]:
              # Leitura dos dados de input
              input_form = request.get_json()

              # Tratamento nos dados de input
              idtEmpr = input_form['idtEmpr']
              codMoeda = input_form['codMoeda']

              #criando DF com campos para inserção
              df = pd.DataFrame({'IDT_EMPR': [int(idtEmpr)], 'COD_ISO_MOED': [codMoeda]})

              df.to_sql(EmpresaxMoeda.__tablename__, con=db.engine, if_exists='append', index=False,method='multi', chunksize=100)

              return input_form, 200

       #Delete Empresa x Moeda
       @staticmethod
       def deleteEmpresaxMoeda() -> List[EmpresaxMoeda]:
              input_form = request.get_json()

              idtEmpr = input_form['empresa']

              #Nessa area fazemos primeiro uma consulta para achar uma linha para a exclusão,
              #Insira os campos para filtrar
              #db.session.query(Cosif).filter_by(COD=cod, COD_MODA=moda).delete()  
              db.session.query(EmpresaxMoeda).filter_by(IDT_EMPR=idtEmpr).delete()    
              db.session.commit()

        #Update Empresa x Moeda
       @staticmethod
       def updateEmpresaxMoeda() -> List[EmpresaxMoeda]:
              input_form = request.get_json()

              #campos
              idtEmpr = input_form['idtEmpr']
              codMoeda = input_form['codMoeda']
       
              #Basicamente o comando filtra uma linha especifica, e depois altera seus campos com base em chave : Valor
              rows_changed = EmpresaxMoeda.query.filter_by(IDT_EMPR=idtEmpr).update(dict(IDT_EMPR = idtEmpr, COD_ISO_MOED = codMoeda))
              db.session.commit()
              return rows_changed, 200
              ####### Fim Empresa x Moeda   
              
       #CARGA RECEITA           
                     
       # DEPARA FILTRO COLETA
       #Get all
       @staticmethod
       def allFiltroColeta() -> List[filtroColeta]:
              #puxando todos os campos do depara empresas
              return [item.serialize for item in filtroColeta.query.all()], 200
       
       # Create Filtro coleta
       @staticmethod
       def createFiltroColeta() -> List[filtroColeta]:
              # Leitura dos dados de input
              input_form = request.get_json()
              
              # Tratamento nos dados de input
              idt_saida = input_form['idtSaida']
              desc_saida =  input_form['descSaida']
              cod_pais = input_form['codPais']
              baln_dre = input_form['balnDre']
              exce_baln = input_form['exceBaln']
              sbcl = input_form['codSbcl']
              exce_sbcl = input_form['exceSbcl']
              produto = input_form['codProd']
              exce_prod = input_form['exceProd']

              if sbcl != None:
                     sbcl = int(sbcl)
              if produto != None:
                     produto = int(produto)

              #criando DF com campos para inserção
              df = pd.DataFrame({'IDT_SAID': [int(idt_saida)], 'DES_SAID': [desc_saida], 'IDT_PAIS': [int(cod_pais)], 'DES_BALN_DRE': [baln_dre], 'DES_EXCE_BALN_DRE': [exce_baln], 'IDT_SBCL': [sbcl], 'DES_EXCE_SBCL': [exce_sbcl], 'IDT_PROD': [produto], 'DES_EXCE_PROD':[exce_prod]})

              df.to_sql(filtroColeta.__tablename__, con=db.engine, if_exists='append', index=False,method='multi', chunksize=100)

              return input_form, 200

        # Update Filtro Coleta
       @staticmethod
       def updateFiltroColeta() -> List[filtroColeta]:
              input_form = request.get_json()

              #campos
              idt_saida = input_form['idt_saida']
              desc_saida = input_form['desc_saida']
              cod_pais = input_form['cod_pais']
              baln_dre = input_form['baln_dre']
              exce_baln = input_form['exce_baln']
              sbcl = input_form['sbcl']
              exce_sbcl = input_form['exce_sbcl']
              produto = input_form['produto']
              exce_prod = input_form['exce_prod']
              id = input_form['chave']
              
              #
              #Basicamente o comando filtra uma linha especifica, e depois altera seus campos com base em chave : Valor
              rows_changed = filtroColeta.query.filter_by(IDT_CHAVE = id).update(dict(IDT_SAID = idt_saida, DES_SAID = desc_saida, IDT_PAIS = cod_pais, DES_BALN_DRE = baln_dre, DES_EXCE_BALN_DRE = exce_baln, IDT_SBCL = sbcl, DES_EXCE_SBCL = exce_sbcl, IDT_PROD = produto, DES_EXCE_PROD = exce_prod))
              db.session.commit()
              return rows_changed, 200
       
       #Delete Filtro Coleta
       @staticmethod
       def deleteFiltroColeta() -> List[filtroColeta]:
              input_form = request.get_json()

              id = input_form['id']

              #
              #Nessa area fazemos primeiro uma consulta para achar uma linha para a exclusão,
              #Insira os campos para filtrar
              #db.session.query(Cosif).filter_by(COD=cod, COD_MODA=moda).delete()  
              db.session.query(filtroColeta).filter_by(IDT_CHAVE=id).delete()    
              db.session.commit()
       
       # DEPARA PRODUTOS SUBCANAIS
       #Get all
       @staticmethod
       def allProdSubcanais() -> List[prodSubcanais]:
              #puxando todos os campos do depara empresas
              return [item.serialize for item in prodSubcanais.query.all()], 200
       
       # Create Produtos Subcanais
       @staticmethod
       def createProdSubcanais() -> List[prodSubcanais]:
              # Leitura dos dados de input
              input_form = request.get_json()
              
              # Tratamento nos dados de input
              prodOpel = input_form['prodOpel']
              emprCanal =  input_form['emprCanal']
              

              #criando DF com campos para inserção
              df = pd.DataFrame({'COD_PROD_OPEL': [int(prodOpel)], 'IDT_EMPR_CANA': [int(emprCanal)]})

              df.to_sql(prodSubcanais.__tablename__, con=db.engine, if_exists='append', index=False,method='multi', chunksize=100)

              return input_form, 200
       
       # Update Produtos Subcanal
       # @staticmethod
       # def updateProdSubcanal() -> List[prodSubcanais]:
       #        input_form = request.get_json()

       #        #campos
       #        prod_opel = input_form['prod_opel']
       #        empr_canal = input_form['empr_canal']
       #        id = input_form['chave']
              
       #        #
       #        #Basicamente o comando filtra uma linha especifica, e depois altera seus campos com base em chave : Valor
       #        rows_changed = prodSubcanais.query.filter_by(IDT_CHAVE = id).update(dict(COD_PROD_OPEL = prod_opel, IDT_EMPR_CANA = empr_canal,))
       #        db.session.commit()
       #        return rows_changed, 200
       
       #Delete Produtos Subcanal
       @staticmethod
       def deleteProdSubcanal() -> List[prodSubcanais]:
              input_form = request.get_json()

              prodOpel = input_form['produto']
              emprCanal = input_form['canal']

              #
              #Nessa area fazemos primeiro uma consulta para achar uma linha para a exclusão,
              #Insira os campos para filtrar
              #db.session.query(Cosif).filter_by(COD=cod, COD_MODA=moda).delete()  
              db.session.query(prodSubcanais).filter_by(COD_PROD_OPEL=prodOpel, IDT_EMPR_CANA=emprCanal).delete()    
              db.session.commit()
       
       # DEPARA EMPRESA DEBITO
       #Get all
       @staticmethod
       def allEmpDeb() -> List[empDeb]:
              #puxando todos os campos do depara empresas
              return [item.serialize for item in empDeb.query.all()], 200

       # Create Empresa Débito
       @staticmethod
       def createEmpDeb() -> List[empDeb]:
              # Leitura dos dados de input
              input_form = request.get_json()
       
              # Tratamento nos dados de input
              emprCod = input_form['emprCod']
              emprCont = input_form['emprCont']
              contCredResu = input_form['contCredResu']
              contCredMarg = input_form['contCredMarg']
              varGerSald = input_form['varGerSald']
              varGerResu = input_form['varGerResu']
              nomeCanal = input_form['nomeCanal']
              sbclDeb = input_form['sbclDeb']
              codMulti = input_form['codMulti']
              prodSLA = input_form['prodSLA']
              prodDelta = input_form['prodDelta']
              
              #criando DF com campos para inserção
              df = pd.DataFrame({'IDT_EMPR': [int(emprCod)], 'DES_EMPR_CTBL': emprCont, 'COD_CONT_CRED_RESU': [int(contCredResu)], 'COD_CONT_CRED_MARG': [int(contCredMarg)], 'COD_VRVL_GEEN_SALD': [int(varGerSald)], 'COD_VRVL_GEEN_RESU': [int(varGerResu)], 'DES_NOM_CANA': nomeCanal, 'COD_SBCL_DEBT': [int(sbclDeb)], 'COD_MULI': [int(codMulti)], 'COD_PROD_SLA': [int(prodSLA)], 'COD_PROD_DELA': [int(prodDelta)]})

              df.to_sql(empDeb.__tablename__, con=db.engine, if_exists='append', index=False,method='multi', chunksize=100)

              return input_form, 200
       
       # Update Empresa Débito
       @staticmethod
       def updateEmpDeb() -> List[empDeb]:
              input_form = request.get_json()

              #campos
              emprCod = input_form['emprCod']
              emprCont = input_form['emprCont']
              contCredResu = input_form['contCredResu']
              contCredMarg = input_form['contCredMarg']
              varGerSald = input_form['varGerSald']
              varGerResu = input_form['varGerResu']
              nomeCanal = input_form['nomeCanal']
              sbclDeb = input_form['sbclDeb']
              codMulti = input_form['codMulti']
              prodSLA = input_form['prodSLA']
              prodDelta = input_form['prodDelta']
              
              #Basicamente o comando filtra uma linha especifica, e depois altera seus campos com base em chave : Valor
              rows_changed = empDeb.query.filter_by(IDT_EMPR = emprCod).update(dict(IDT_EMPR = emprCod,DES_EMPR_CTBL = emprCont, COD_CONT_CRED_RESU = contCredResu, COD_CONT_CRED_MARG = contCredMarg, COD_VRVL_GEEN_SALD = varGerSald, COD_VRVL_GEEN_RESU = varGerResu, DES_NOM_CANA = nomeCanal, COD_SBCL_DEBT = sbclDeb, COD_MULI = codMulti, COD_PROD_SLA = prodSLA, COD_PROD_DELA= prodDelta))
              
              db.session.commit()
              return rows_changed, 200
       
       #Delete Empresa Débito
       @staticmethod
       def deleteEmpDeb() -> List[empDeb]:
              input_form = request.get_json()

              id = input_form['id']

              #
              #Nessa area fazemos primeiro uma consulta para achar uma linha para a exclusão,
              #Insira os campos para filtrar
              #db.session.query(Cosif).filter_by(COD=cod, COD_MODA=moda).delete()  
              db.session.query(empDeb).filter_by(DES_EMPR_CTBL=id).delete()    
              db.session.commit()
              #Fim 

# DEPARA EMPRESA SERVICO
       #Get all
       @staticmethod
       def allEmpresaServico() -> List[empresaServico]:
              #puxando todos os campos do depara empresas
              return [item.serialize for item in empresaServico.query.all()], 200
       
       # Create Empresa Servico
       @staticmethod
       def createEmpresaServico() -> List[empresaServico]:
              # Leitura dos dados de input
              input_form = request.get_json()
              
              # Tratamento nos dados de input
              emprServ = input_form['emprServ']
              emprSbso =  input_form['emprSbso']
              
              #criando DF com campos para inserção
              df = pd.DataFrame({'IDT_EMPR_SERV': [int(emprServ)], 'IDT_EMPR_SBSO': [int(emprSbso)]})

              df.to_sql(empresaServico.__tablename__, con=db.engine, if_exists='append', index=False,method='multi', chunksize=100)

              return input_form, 200
       
       # Update Empresa Servico
       @staticmethod
       def updateEmpresaServico() -> List[empresaServico]:
              input_form = request.get_json()

              #campos
              empr_serv = input_form['empr_serv']
              empr_sbso = input_form['empr_sbso']
              
              #
              #Basicamente o comando filtra uma linha especifica, e depois altera seus campos com base em chave : Valor
              rows_changed = empresaServico.query.filter_by(IDT_EMPR_SERV = empr_serv).update(dict(IDT_EMPR_SERV = empr_serv, IDT_EMPR_SBSO = empr_sbso))
              db.session.commit()
              return rows_changed, 200
       
       #Delete Empresa Servico
       @staticmethod
       def deleteEmpresaServico() -> List[empresaServico]:
              input_form = request.get_json()

              emprServ = input_form['servico']

              #
              #Nessa area fazemos primeiro uma consulta para achar uma linha para a exclusão,
              #Insira os campos para filtrar
              #db.session.query(Cosif).filter_by(COD=cod, COD_MODA=moda).delete()  
              db.session.query(empresaServico).filter_by(IDT_EMPR_SERV=emprServ).delete()    
              db.session.commit()      


       # DEPARA SERVICO ORGAO
       #Get all
       @staticmethod
       def allServicoOrgao() -> List[servicoOrgao]:
              #puxando todos os campos do depara empresas
              return [item.serialize for item in servicoOrgao.query.all()], 200
       
       # Create Serviço Orgao
       @staticmethod
       def createServicoOrgao() -> List[servicoOrgao]:
              # Leitura dos dados de input
              input_form = request.get_json()
              
              # Tratamento nos dados de input
              serv_org = input_form['servOrg']
              serv_sub =  input_form['servSub']
              serv_org_empr = input_form['servOrgEmpr']
              
              #criando DF com campos para inserção
              df = pd.DataFrame({'IDT_SERV_ORGO': [int(serv_org)], 'IDT_SERV_SUB': [int(serv_sub)], 'IDT_SERV_ORGO_EMPR': [int(serv_org_empr)]})

              df.to_sql(servicoOrgao.__tablename__, con=db.engine, if_exists='append', index=False,method='multi', chunksize=100)

              return input_form, 200
       
       # Update Serviço Orgao
       @staticmethod
       def updateServicoOrgao() -> List[servicoOrgao]:
              input_form = request.get_json()

              #campos
              serv_org = input_form['serv_org']
              serv_sub =  input_form['serv_sub']
              serv_sub_ant =  input_form['serv_sub_ant']
              serv_org_empr = input_form['serv_org_empr']
              serv_org_empr_ant = input_form['serv_org_empr_ant']
              # #
              #Basicamente o comando filtra uma linha especifica, e depois altera seus campos com base em chave : Valor
              rows_changed = servicoOrgao.query.filter_by(IDT_SERV_SUB=serv_sub_ant, IDT_SERV_ORGO_EMPR=serv_org_empr_ant).update(dict(IDT_SERV_ORGO = serv_org, IDT_SERV_SUB = serv_sub, IDT_SERV_ORGO_EMPR = serv_org_empr,))
              db.session.commit()
              
              return rows_changed, 200
       
       #Delete Serviço Orgao
       @staticmethod
       def deleteServicoOrgao() -> List[servicoOrgao]:
              input_form = request.get_json()

              servOrg = input_form['servorgao']
              servSub = input_form['servsub']
              servOrgEmpr = input_form['orgempresa']

              # #
              #Nessa area fazemos primeiro uma consulta para achar uma linha para a exclusão,
              #Insira os campos para filtrar
              #db.session.query(Cosif).filter_by(COD=cod, COD_MODA=moda).delete()  
              db.session.query(servicoOrgao).filter_by(IDT_SERV_ORGO=servOrg, IDT_SERV_SUB=servSub, IDT_SERV_ORGO_EMPR=servOrgEmpr).delete()    
              db.session.commit() 
              #FIM


        # DEPARA CONTA FOLHA
       #Get all
       @staticmethod
       def allContaFolha() -> List[contaFolha]:
              #puxando todos os campos do depara empresas
              return [item.serialize for item in contaFolha.query.all()], 200
       
       # Create Conta Folha
       @staticmethod
       def createContaFolha() -> List[contaFolha]:
              # Leitura dos dados de input
              input_form = request.get_json()
              
              # Tratamento nos dados de input
              idt_pais = input_form['idtPais']
              cod_prod =  input_form['codProd']
              idt_csdt =  input_form['idtCsdt']
              saldo_orig =  input_form['saldoOrig']
              rsti_orig =  input_form['rstOrig']
              idt_folha = input_form['idtFolha']
              
              #criando DF com campos para inserção
              df = pd.DataFrame({'IDT_PAIS': [int(idt_pais)], 'COD_PROD': [int(cod_prod)], 'IDT_CSDT': [int(idt_csdt)], 'IDT_SALD_ORIG': [int(saldo_orig)], 'IDT_CONT_RSTI_ORIG': [int(rsti_orig)], 'IDT_FOLH': [int(idt_folha)]})

              df.to_sql(contaFolha.__tablename__, con=db.engine, if_exists='append', index=False,method='multi', chunksize=100)

              return input_form, 200
       
       # Update Conta Folha
       @staticmethod
       def updateContaFolha() -> List[contaFolha]:
              input_form = request.get_json()

              #campos
              idt_pais = input_form['idt_pais']
              cod_prod =  input_form['cod_prod']
              idt_csdt =  input_form['idt_csdt']
              saldo_orig =  input_form['saldo_orig']
              rsti_orig =  input_form['rsti_orig']
              idt_folha = input_form['idt_folha']
              
              #
              #Basicamente o comando filtra uma linha especifica, e depois altera seus campos com base em chave : Valor
              rows_changed = contaFolha.query.filter_by(IDT_PAIS = idt_pais, COD_PROD=cod_prod).update(dict(IDT_PAIS = idt_pais, COD_PROD = cod_prod, IDT_CSDT = idt_csdt, IDT_SALD_ORIG = saldo_orig, IDT_CONT_RSTI_ORIG = rsti_orig, IDT_FOLH = idt_folha,))
              db.session.commit()
              return rows_changed, 200
       
       #Delete Conta Folha
       @staticmethod
       def deleteContaFolha() -> List[contaFolha]:
              input_form = request.get_json()

              idtPais = input_form['idt_pais']
              codProd = input_form['codprod']

              # #
              #Nessa area fazemos primeiro uma consulta para achar uma linha para a exclusão,
              #Insira os campos para filtrar
              #db.session.query(Cosif).filter_by(COD=cod, COD_MODA=moda).delete()  
              db.session.query(contaFolha).filter_by(IDT_PAIS=idtPais, COD_PROD=codProd).delete()    
              db.session.commit()   
              #FIM 


       # DEPARA CONTA DELTA
       #Get all
       @staticmethod
       def allContaDelta() -> List[contaDelta]:
              #puxando todos os campos do depara empresas
              return [item.serialize for item in contaDelta.query.all()], 200
       
       # Create Conta Delta
       @staticmethod
       def createContaDelta() -> List[contaDelta]:
              # Leitura dos dados de input
              input_form = request.get_json()
              
              # Tratamento nos dados de input
              ajus_Delta = input_form['ajusDelta']
              idt_Saida =  input_form['idtSaida']
              idt_Empr =  input_form['idtEmpr']
              cont_Deb =  input_form['contDeb']
              sub_Deb =  input_form['subDeb']
              pess_Deb = input_form['pessDeb']
              cont_Cred = input_form['contCred']
              sub_Cred = input_form['subCred']
              
              #criando DF com campos para inserção
              df = pd.DataFrame({'DES_AJUS_DELA': ajus_Delta, 'IDT_SAID': [int(idt_Saida)], 'IDT_EMPR': [int(idt_Empr)], 'IDT_CONT_DEBT': [int(cont_Deb)], 'IDT_SBCL_DEBT': [int(sub_Deb)], 'IDT_PESS_DEBT': pess_Deb, 'IDT_CONT_CRED': [int(cont_Cred)], 'IDT_SBCL_CRED': [int(sub_Cred)]})

              df.to_sql(contaDelta.__tablename__, con=db.engine, if_exists='append', index=False,method='multi', chunksize=100)

              return input_form, 200
       
       # Update Conta Delta
       @staticmethod
       def updateContaDelta() -> List[contaDelta]:
              input_form = request.get_json()

              #campos
              ajus_Delta = input_form['ajus_Delta']
              idt_Saida =  input_form['idt_Saida']
              idt_Empr =  input_form['idt_Empr']
              cont_Deb =  input_form['cont_Deb']
              sub_Deb =  input_form['sub_Deb']
              pess_Deb = input_form['pess_Deb']
              cont_Cred = input_form['cont_Cred']
              sub_Cred = input_form['sub_Cred']
              
              #Basicamente o comando filtra uma linha especifica, e depois altera seus campos com base em chave : Valor
              rows_changed = contaDelta.query.filter_by(IDT_SAID = idt_Saida, IDT_EMPR=idt_Empr).update(dict(DES_AJUS_DELA = ajus_Delta, IDT_SAID=idt_Saida, IDT_EMPR=idt_Empr, IDT_CONT_DEBT=cont_Deb, IDT_SBCL_DEBT = sub_Deb, IDT_PESS_DEBT = pess_Deb, IDT_CONT_CRED = cont_Cred, IDT_SBCL_CRED = sub_Cred,))
              db.session.commit()
              return rows_changed, 200
       
       #Delete Conta Delta
       @staticmethod
       def deleteContaDelta() -> List[contaDelta]:
              input_form = request.get_json()

              idtSaida = input_form['idsaida']
              idtEmpr = input_form['idempresa']

              #Nessa area fazemos primeiro uma consulta para achar uma linha para a exclusão,
              #Insira os campos para filtrar
              #db.session.query(Cosif).filter_by(COD=cod, COD_MODA=moda).delete()  
              db.session.query(contaDelta).filter_by(IDT_SAID=idtSaida, IDT_EMPR=idtEmpr).delete()    
              db.session.commit()                   

       # CARGA CUSTO
       
       # DEPARA PRODUTO SLA
       #Get all
       @staticmethod
       def allProdSLA() -> List[prodSLA]:
              #puxando todos os campos do depara empresas
              return [item.serialize for item in prodSLA.query.all()], 200
       
       # Create Prod SLA
       @staticmethod
       def createProdSLA() -> List[prodSLA]:
              # Leitura dos dados de input
              input_form = request.get_json()
              
              # Tratamento nos dados de input
              empr_sla = input_form['empr_sla']
              prod_sla =  input_form['prod_sla']
              
              #criando DF com campos para inserção
              df = pd.DataFrame({'IDT_EMPR_SLA': [int(empr_sla)], 'IDT_PROD_SLA': [int(prod_sla)]})

              df.to_sql(prodSLA.__tablename__, con=db.engine, if_exists='append', index=False,method='multi', chunksize=100)

              return input_form, 200
       
       # Update Prod SLA
       # @staticmethod
       # def updateProdSLA() -> List[prodSLA]:
       #        input_form = request.get_json()

       #        #campos
       #        empr_sla = input_form['empr_sla']
       #        prod_sla =  input_form['prod_sla']
       #        id =  input_form['id']
       
       #        # #
       #        #Basicamente o comando filtra uma linha especifica, e depois altera seus campos com base em chave : Valor
       #        rows_changed = prodSLA.query.filter_by(IDT_CHAVE = id).update(dict(IDT_EMPR_SLA = empr_sla, IDT_PROD_SLA = prod_sla))
       #        db.session.commit()
       #        return rows_changed, 200
       
       
       #Delete Prod SLA
       @staticmethod
       def deleteProdSLA() -> List[prodSLA]:
              input_form = request.get_json()

              empr_sla = input_form['empresa_sla']
              prod_sla = input_form['produto_sla']

              #
              #Nessa area fazemos primeiro uma consulta para achar uma linha para a exclusão,
              #Insira os campos para filtrar
              #db.session.query(Cosif).filter_by(COD=cod, COD_MODA=moda).delete()  
              db.session.query(prodSLA).filter_by(IDT_EMPR_SLA=empr_sla, IDT_PROD_SLA=prod_sla).delete()    
              db.session.commit()                   
       
       # DEPARA CODIGO DE CUSTOS
       #Get all
       @staticmethod
       def allCodCustos() -> List[codCustos]:
              #puxando todos os campos do depara empresas
              return [item.serialize for item in codCustos.query.all()], 200
       
       # Create Código de Custos
       @staticmethod
       def createCodCustos() -> List[codCustos]:
              # Leitura dos dados de input
              input_form = request.get_json()
              
              # Tratamento nos dados de input
              descUnid = input_form['desc_unid']
              codUnid =  input_form['cod_unid']
              empr = input_form['empr']
              codEvento = input_form['cod_evento']
              codExctEvento = input_form['cod_exct_evento']
              canalCom = input_form['canal_com']
              
              #criando DF com campos para inserção
              df = pd.DataFrame({'DES_UNID': descUnid, 'COD_UNID': [int(codUnid)], 'IDT_EMPR': [int(empr)], 'COD_EVEN_BONU': [int(codEvento)], 'COD_EVEN_EXCT_BONU': [int(codExctEvento)], 'IDT_CANA_COML_LOCL': [int(canalCom)]})
              
              df.to_sql(codCustos.__tablename__, con=db.engine, if_exists='append', index=False,method='multi', chunksize=100)

              return input_form, 200
       
       # Update Código de Custos
       @staticmethod
       def updateCodCustos() -> List[codCustos]:
              input_form = request.get_json()

              #campos
              desc_unid = input_form['desc_unid']
              id =  input_form['cod_unid']
              empr =  input_form['empr']
              cod_evento = input_form['cod_evento']
              cod_exct_evento = input_form['cod_exct_evento']
              canal_com = input_form['canal_com']

              #Basicamente o comando filtra uma linha especifica, e depois altera seus campos com base em chave : Valor
              rows_changed = codCustos.query.filter_by(COD_UNID = id).update(dict(DES_UNID = desc_unid, IDT_EMPR = empr, COD_EVEN_BONU = cod_evento, COD_EVEN_EXCT_BONU = cod_exct_evento, IDT_CANA_COML_LOCL = canal_com))
              db.session.commit()
              return rows_changed, 200
       
       
       #Delete Código de Custos
       @staticmethod
       def deleteCodCustos() -> List[codCustos]:
              input_form = request.get_json()

              id = input_form['id']

              #
              #Nessa area fazemos primeiro uma consulta para achar uma linha para a exclusão,
              #Insira os campos para filtrar
              #db.session.query(Cosif).filter_by(COD=cod, COD_MODA=moda).delete()  
              db.session.query(codCustos).filter_by(COD_UNID=id).delete()    
              db.session.commit()        
       
       # DEPARA SUBCANAL PF ou PJ
       #Get all
       @staticmethod
       def allSubcanalPfxPj() -> List[subcanalPfXPj]:
              #puxando todos os campos do depara empresas
              return [item.serialize for item in subcanalPfXPj.query.all()], 200
       
       # Create Subcanal x PF ou PJ
       @staticmethod
       def createSubcanalPfxPj() -> List[subcanalPfXPj]:
              # Leitura dos dados de input
              input_form = request.get_json()
              
              # Tratamento nos dados de input
              sbcl = input_form['sbcl']
              tipo_entidade =  input_form['tipo_entidade']
       
              #criando DF com campos para inserção
              df = pd.DataFrame({'IDT_SBCL': [int(sbcl)], 'DES_TIPO_ENTI': tipo_entidade})
              
              df.to_sql(subcanalPfXPj.__tablename__, con=db.engine, if_exists='append', index=False,method='multi', chunksize=100)

              return input_form, 200
       
       # Update Subcanal x PF ou PJ
       @staticmethod
       def updateSubcanalPfxPj() -> List[subcanalPfXPj]:
              input_form = request.get_json()

              #campos
              sbcl = input_form['sbcl']
              tipo_entidade =  input_form['tipo_entidade']
              
              #
              #Basicamente o comando filtra uma linha especifica, e depois altera seus campos com base em chave : Valor
              rows_changed = subcanalPfXPj.query.filter_by(IDT_SBCL = sbcl).update(dict(DES_TIPO_ENTI = tipo_entidade))
              db.session.commit()
              return rows_changed, 200
       
       #Delete Subcanal x PF ou PJ
       @staticmethod
       def deleteSubcanalPfxPj() -> List[subcanalPfXPj]:
              input_form = request.get_json()

              id = input_form['id']

              #Nessa area fazemos primeiro uma consulta para achar uma linha para a exclusão,
              #Insira os campos para filtrar
              #db.session.query(Cosif).filter_by(COD=cod, COD_MODA=moda).delete()  
              db.session.query(subcanalPfXPj).filter_by(IDT_SBCL=id).delete()    
              db.session.commit()
       
       # AJUSTES

       # DEPARA AJUSTE PROD. SALDO
       #Get all
       @staticmethod
       def allAjusteProdSaldo() -> List[ajusteUnidExternaGeral]:
              #puxando todos os campos do depara empresas
              #return [item.serialize for item in ajusteUnidExternaGeral.query.all()], 200
              for item in ajusteUnidExternaGeral.query.all():
                     print(item.serialize)
              return [item.serialize for item in ajusteUnidExternaGeral.query.all()], 200
       
        # Create Ajuste Prod. Saldo
       @staticmethod
       def createAjusteProdSaldo() -> List[ajusteUnidExternaGeral]:
              # Leitura dos dados de input
              input_form = request.get_json()
              
              # Tratamento nos dados de input
              des_ajus = input_form['des_ajus']
              cod_tipo_ajus = input_form['cod_tipo_ajus']
              cod_geen_debt = input_form['cod_geen_debt']
              cod_geen_cred = input_form['cod_geen_cred']
              cod_empr = input_form['cod_empr']
              cod_rate = input_form['cod_rate']
              cod_sbcl_debt = input_form['cod_sbcl_debt']
              cod_folha_debt = input_form['cod_folha_debt']
              des_moeda = input_form['des_moeda']
              
              print(des_ajus, cod_tipo_ajus, cod_geen_debt, cod_geen_cred, cod_empr, cod_rate, cod_sbcl_debt, cod_folha_debt, des_moeda)
              #criando DF com campos para inserção
              df = pd.DataFrame({'DES_AJUS': des_ajus, 'COD_TIPO_AJUS': [int(cod_tipo_ajus)], 'COD_VRVL_GEEN_DEBT': [int(cod_geen_debt)], 'COD_VRVL_GEEN_CRED':[int(cod_geen_cred)], 'COD_EMPR': [int(cod_empr)], 'COD_RATE': [int(cod_rate)], 'COD_SBCL_DEBT': [int(cod_sbcl_debt)],'COD_FOLH_DEBT': [int(cod_folha_debt)], 'DES_MOED': des_moeda})
              
              df.to_sql(ajusteUnidExternaGeral.__tablename__, con=db.engine, if_exists='append', index=False,method='multi', chunksize=100)

              return input_form, 200
       
       # Update Ajuste Prod. Saldo
       @staticmethod
       def updateAjusteProdSaldo() -> List[ajusteUnidExternaGeral]:
              input_form = request.get_json()

              #campos
              des_ajus = input_form['des_ajus']
              cod_tipo_ajus = input_form['cod_tipo_ajus']
              cod_geen_debt = input_form['cod_geen_debt']
              cod_geen_cred = input_form['cod_geen_cred']
              cod_empr = input_form['cod_empr']
              cod_rate = input_form['cod_rate']
              cod_sbcl_debt = input_form['cod_sbcl_debt']
              cod_folha_debt = input_form['cod_folha_debt']
              des_moeda = input_form['des_moeda']
              
              #Basicamente o comando filtra uma linha especifica, e depois altera seus campos com base em chave : Valor
              rows_changed = ajusteUnidExternaGeral.query.filter_by(COD_TIPO_AJUS = cod_tipo_ajus).update(dict(DES_AJUS = des_ajus,  COD_VRVL_GEEN_DEBT= cod_geen_debt, COD_VRVL_GEEN_CRED = cod_geen_cred, COD_EMPR = cod_empr, COD_RATE=cod_rate, COD_SBCL_DEBT=cod_sbcl_debt, COD_FOLH_DEBT=cod_folha_debt, DES_MOED=des_moeda))
              db.session.commit()
              return rows_changed, 200
       
       #Delete Ajuste Prod. Saldo
       @staticmethod
       def deleteAjusteProdSaldo() -> List[ajusteUnidExternaGeral]:
              input_form = request.get_json()

              id = input_form['id']

              #Nessa area fazemos primeiro uma consulta para achar uma linha para a exclusão,
              #Insira os campos para filtrar
              #db.session.query(Cosif).filter_by(COD=cod, COD_MODA=moda).delete()  
              db.session.query(ajusteUnidExternaGeral).filter_by(COD_TIPO_AJUS=id).delete()    
              db.session.commit()