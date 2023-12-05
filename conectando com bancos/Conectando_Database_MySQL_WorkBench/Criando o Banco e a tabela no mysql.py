import mysql.connector as mys
from mysql.connector import errorcode
#$cbd = conecção banco de dados(cbd)
cbd = mys.connect(user='root',password='sua-senha',
                  host='localhost',)
cursor = cbd.cursor(buffered=True)

#criando tabelas no sql WorkBench#
data_base_name = 'aplicativo'
TABLES = {}
TABLES['aplicativo'] = (
  "CREATE TABLE `cadastro`("
  "`id_user`int(11) NOT NULL AUTO_INCREMENT,"
  "`Nome` varchar(20) NOT NULL,"
  "`Idade` int NOT NULL,"
  "`função` varchar(15) NOT NULL,"
  " PRIMARY KEY (`id_user`)"
  ")ENGINE=InnoDB")

def create_database(cursor):
  try:
    cursor.execute(
      "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(data_base_name))
  except mys.Error as err:
    print('falhou na criação do database: {}'.format(err))
    
try:
  cursor.execute("USE {}".format(data_base_name))
except mys.Error as err:
  print('o bando de dados não existe'. format(data_base_name))
  if err.errno == errorcode.ER_BAD_DB_ERROR:
    create_database(cursor)
    print('banco de dados criado com sucesso'.format(data_base_name))
    cbd.database = data_base_name
  else:
    print(err)
    exit(1)

for table_name in TABLES:
  descTable = TABLES[table_name]
  try:
    print('Criando tabela {}:'.format(table_name),end='')
    cursor.execute(descTable)
  except mys.Error as err:
    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
      print('a tabela ja existe.')
    else:
      print(err.msg)
  else:
    print("OK")
cursor.close()    

#criando tabelas no sql WorkBench#


cbd.close()
