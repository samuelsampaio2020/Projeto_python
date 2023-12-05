import flet as ft

def main(page: ft.page):
  page.title = "Exemplos de Rotas"
  page.vertical_alignment = ft.MainAxisAlignment.CENTER
  
  container = ft.Container(
    border=ft.border.all(1,ft.colors.BLACK),
    content=ft.FilledButton("primary Color"),
    theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.RED))
  )
  page.add(container)
  page.update()
  
  def mudar_rota(route):
    page.views.clear()
    page.views.append(
      ft.View(
        "/",
        [
          ft.AppBar(title=ft.Text("Home",bgcolor=ft.colors.SURFACE_VARIANT)),
          ft.ElevatedButton('ARMAZEM',on_click=lambda _:page.go('/armazem')),
          ft.ElevatedButton('INFORMAÇÔES',on_click=lambda _:page.go('/informações')),
          
          
          ft.Text('Formulario\n',size=25),
          ft.TextField(label="Informe seu Nome",text_size=20),
          ft.TextField(label="Informe SobreNome",text_size=20)
        ]
        ))
    if page.route == "/informações":
      page.views.append(
        ft.View(
          "/informações",
          [
            ft.AppBar(title=ft.Text("informações"),bgcolor=ft.colors.SURFACE_VARIANT),
            ft.ElevatedButton("Inicio", on_click=lambda _:page.go("/")),
            
            ft.Text('Formulario\n',size=25,text_align='center'),
            ft.TextField(label="Informe seu Nome",text_size=20,width=350),
            ft.TextField(label="Informe SobreNome",text_size=20,width=350)
          ]
        )
      )
    if page.route == "/armazem":
      page.views.append(
        ft.View(
          "/armazem",
          [
            ft.AppBar(title=ft.Text("armazem"),bgcolor=ft.colors.SURFACE_VARIANT),
            ft.ElevatedButton("Inicio", on_click=lambda _:page.go("/")),
          ]
        )
      )
    
    page.update()
    
  def vizualizar(view):
    page.views.pop()
    top_view = page.views[-1]
    page.go(top_view.route)
    
  
  page.on_route_change = mudar_rota
  page.on_view_pop = vizualizar
  page.go(page.route)


ft.app(target=main)