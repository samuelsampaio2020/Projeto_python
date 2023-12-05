import mysql.connector as mys
import json

cnx = mys.connect(user='root',password='sua-senha',
                  host='localhost',database='aplicativo')
cursor = cnx.cursor()

def updateNome(id_user:int,NovoNome:str):
  commando = ("update cadastro"
              f" set Nome = '{NovoNome}'"
              f" where id_user = {id_user}")
  cursor.execute(commando)
  cnx.commit()
  print("dados Atualizados Com sucesso")
  cursor.close()
  
def updateIdade(id_user:int,NovaIdade:int):
  commando = ("update cadastro"
              f" set Idade = {NovaIdade}"
              f" where id_user = {id_user}")
  cursor.execute(commando)
  cnx.commit()
  print("dados Atualizados Com sucesso")
  cursor.close()
  
def updateFunção(id_user:int,NovaFunção:str):
  commando = ("update cadastro"
              f" set função = '{NovaFunção}'"
              f" where id_user = {id_user}")
  cursor.execute(commando)
  cnx.commit()
  print("dados Atualizados Com sucesso")
  cursor.close()
  
def inserirNovosDados(nome:str,idade:int,função:str):
  command = ("INSERT INTO cadastro(nome,idade,função)"
            f"VALUES('{nome}',{idade},'{função}')")
  cursor.execute(command)
  cnx.commit()

def mostrar():
  cursor.execute("""select * from cadastro""")
  dados = (cursor.fetchall())
  for x in dados:
    print(x)

def excluirDados(id_user:int):
    comando = f"""delete from cadastro where id_user = {id_user}"""
    cursor.execute(comando)
    cnx.commit()
    print("dados Apagados com Sucesso")
    cursor.close()
    
def alterVARCHARtable(nome:str,N:int):
  command = ("ALTER TABLE cadastro"#alter table cadastro modify column Nome varchar(40)
            f" MODIFY COLUMN {nome} varchar({N})")
  cursor.execute(command)
  cnx.commit()
  print('Dados Alterados Com Sucesso')
  cursor.close() 
#zona de chamada#






#zona de chamada#

cnx.close()
