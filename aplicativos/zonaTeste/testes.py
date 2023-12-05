import flet as ft

def main(page: ft.page):
  page.scroll = "always" #ativa o SCROLL de rolamento da pagina
  
  #pegando valores e utilizando em uma função
  def mostrarNome(e):
    if not nome.value:
      nome.error_text = "!!!Campo Obrigatorio!!!"
      page.update()
    else:
      name = nome.value
      page.clean()
      page.add(ft.Text(f'seu nome é:{name}'))  
  nome = ft.TextField(label='!!!informe seu nome!!!')
  page.add(nome, ft.ElevatedButton('Enviar', on_click=mostrarNome))
  #pegando valores(tipo Texto) e utilizando em uma função



  #pegando valores checkbox(e utilizando um comparado value=false ou true) caso o valor mude de estado(bolean)
  def checkbox_mudando(e):
    output_text.value = (
      f'you have learned how to ski: {todo_check.value}'
    )
    page.update()
  
  output_text = ft.Text()
  todo_check = ft.Checkbox(label="todo: learn how to use ski",value=False, on_change=checkbox_mudando)
  page.add(todo_check,output_text)
  #pegando valores checkbox(e utilizando um comparado value=false ou true) caso o valor mude de estado(bolean)
  
  
  
  #Menu suspendo-------------------------------------------
  def buton_click(e):
    texto_output.value = f'o valor do dropdown:{color_dropdown.value}'
    page.update()
  texto_output = ft.Text()
  butao_enviar = ft.ElevatedButton(text="enviar", on_click=buton_click,bgcolor=ft.colors.GREEN_300,color=ft.colors.BLACK)
  color_dropdown = ft.Dropdown(
    width=100,
    options=[ft.dropdown.Option("RED",),
      ft.dropdown.Option("GREEN"),
      ft.dropdown.Option("BLUE")])
  page.add(color_dropdown,butao_enviar,texto_output)#a ordem importa
  #Menu suspendo-------------------------------------------
  
  #ativando as chaves do teclado---------------------------
  def teclado(e: ft.KeyboardEvent):
    page.add(
      ft.Text(
        f"chaves: {e.key} ,Control:{e.ctrl},ALT:{e.alt},SHIFT:{e.shift}"))
  page.on_keyboard_event = teclado
  page.add(
    ft.Text("pressione uma dos butoes com uma combinação de CTRL,ALT,SHIFT,"))
  #ativando as chaves do teclado---------------------------
  
  
  
  
ft.app(target=main)