import flet as ft

def main(page: ft.Page):
    page.bgcolor = "#03020c"
    page.window_width = 330
    page.window_height = 660
    
    page.add(
        ft.FloatingActionButton(
            icon=ft.icons.ADD_CIRCLE,
            bgcolor=ft.colors.BLUE,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)