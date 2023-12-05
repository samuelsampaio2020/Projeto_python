import flet as ft

def main(page: ft.Page):
  page.vertical_alignment = ft.MainAxisAlignment.CENTER
  page.add(
    ft.Text(f"Rota inicial {page.route}")
  )
  def mudar_rota(e: ft.RouteChangeEvent):
    page.add(ft.Text(f'Nova Rota:{e.route}'))
  
  def Go_armazem(e):
    page.route = '/armazem'
    page.update()
    
  page.on_route_change = mudar_rota
  page.add(
    ft.ElevatedButton('armazem', on_click=Go_armazem)
  )
  
  
ft.app(target=main, view=ft.AppView.WEB_BROWSER)