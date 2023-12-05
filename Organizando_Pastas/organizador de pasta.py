import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione Uma Pasta")

locais = {
    "imagens": [".png",".jpg"],
    "Banco De Dados": [".sql"],
    "aplicativos_executaveis":[".exe"],
    "PDFs":[".pdf"],
    "planilhas":[".xls"],
    "Navegação":[".html"],
    "Bloco de Notas":[".txt"]
}

lista_de_arquivo = os.listdir(caminho)

for arquivo in lista_de_arquivo:
  nome, extenção = os.path.splitext(f"{caminho}/{arquivo}")
  for pasta in locais:
    print(pasta)
    if extenção in locais[pasta]:
      if not os.path.exists(f"{caminho}/{pasta}"):
        os.mkdir(f"{caminho}/{pasta}")
      os.rename(f"{caminho}/{pasta}", f"{caminho}/{pasta}/{arquivo}")
      