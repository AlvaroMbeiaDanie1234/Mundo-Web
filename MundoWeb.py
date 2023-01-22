import flet as ft

def main(page: ft.Page):
    page.title="Mundo 1.0"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = "auto"


    def check_item_clicked(e):
        if e.control.checked ==  e.control.checked:
            page.theme_mode = ft.ThemeMode.DARK
            page.update()



    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.CODE),
        leading_width=40,
        title=ft.Text("Mundo 1.0"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Dark Mode", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )
    page.add(ft.Text(""))


    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    page.add(
        ft.Row(
            [

                ft.Container(
                    content=ft.Text("Mundo | Programming Language"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    width=150,
                    height=40,
                    border_radius=10,
                    ink=True,
                    expand = True,
                    on_click=lambda e: print("Clickable transparent with Ink clicked!"),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )




    # COlocando função ao clicar na infomatica
    def informatica(e):
        pass


    page.add(
        ft.Row(
            [

                ft.Container(
                    content=ft.Text("Hello World!"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.GREEN_200,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink = True,
                    expand = True,
                    on_click=informatica,
                ),
                ft.Container(
                    content=ft.Text("Variables"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.GREEN_200,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    expand = True,
                    on_click=lambda e: print("Clickable transparent with Ink clicked!"),
                ),
                ft.Container(
                    content=ft.Text("While"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.GREEN_200,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    expand = True,
                    on_click=lambda e: print("Clickable transparent with Ink clicked!"),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

    page.add(
        ft.FilledButton(text="Learn Mundo"),
        )





    page.add(
        ft.Row(
            [

                ft.Container(
                    content=ft.Text("Mundo | Programming Language\n\nMundo is a Programming Language basade on Python, and writen 100% in Python,\nby Álvaro Mbeia Daniel Miguel, a cumputer student"),
                    margin=10,
                    padding=10,
                    width=150,
                    height=200,
                    border_radius=1,
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    alignment=ft.alignment.center,
                    ink=True,
                    expand = True,
                    on_click=lambda e: print("Clickable transparent with Ink clicked!"),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )




    def Joao(e):
        pass





    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
            #ft.NavigationDestination(icon=ft.icons.PEOPLE, label=""),
            ft.NavigationDestination(icon=ft.icons.BOOKMARK_BORDER,selected_icon=ft.icons.BOOKMARK,label="Documentation",),
            #ft.NavigationDestination(icon=ft.icons.GITHUB, label="Notificações"),
           
            

        ]
    )
    page.add(ft.Text(""))

ft.app(target=main, view=ft.WEB_BROWSER)
