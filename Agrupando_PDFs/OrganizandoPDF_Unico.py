import PyPDF2
import os

aux = PyPDF2.PdfMerger()

lista_Arquivos = os.listdir("C:\samuel\VSCode Project\Projetos\Agrupando_PDFs\PDFs")
lista_Arquivos.sort()

for arquivo in lista_Arquivos:
  nome , ext = os.path.splitext(f'{lista_Arquivos}/{arquivo}')#dividindo e extraindo a extenção do arquivo
  if ext in arquivo:
    aux.append(f"C:\samuel\VSCode Project\Projetos\Agrupando_PDFs\PDFs/{arquivo}")

aux.write("PDF Unico.pdf")