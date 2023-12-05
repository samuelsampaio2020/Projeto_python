import requests as r
import json

bd = "https://conectandopython-f7c23-default-rtdb.firebaseio.com"#link do banco de dados da firebase

############## coneção com banco de dados do firebase ####################

##### metodo post criando uma informação nova no banco de dados #####
#dadosUser = {'email':'samuelsampaio2020@hotmail.com','senha':'1151224'}
#postar = r.post(f'{bd}/Usuarios/.json', data=json.dumps(dadosUser))
#print(postar)
#print(postar.text)
##### metodo post criando uma informação nova no banco de dados #####


##### metodo patch alterar o banco de dados ######
#alterDados = {'senha':1234}
#caminho = r.patch(f'{bd}/Usuarios/-NjvZMj2ML67sgYfhGMT/.json',data=json.dumps(alterDados))
#print(caminho)
#print(caminho.text)
##### metodo patch alterar o banco de dados ######


##### metodo get pegando valores do banco de dados #####
#pegandoDados = r.get(f'{bd}/Usuarios/.json')
#print(pegandoDados)
#print(pegandoDados.json())
#dadosEmail = pegandoDados.json()
#for id_user in dadosEmail:
#  print('Id_Usuario_:',id_user)
#  email = dadosEmail[id_user]['email']
#  print('Email_:',email)
#  senha = dadosEmail[id_user]['senha']
#  print('Senha:',senha)
##### metodo get pegando valores do banco de dados #####


##### metodo DELETE deletando dados do database #####
#Dados_A_Deletar = r.get(f'{bd}/Usuarios/.json')
#dados = Dados_A_Deletar.json()
#for id_user in dados:
#  if id_user == 'carlos':
#    print(f'Usuario Deletado {id_user:#_^20}')
#    id_D_user = id_user
#deletandoDados = r.delete(f'{bd}/Usuarios/{id_D_user}/.json')
#print(deletandoDados)
#print(deletandoDados.text)
##### metodo DELETE deletando dados do database #####