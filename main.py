import flet as ft

def main(page: ft.Page):
    page.bgcolor = "#03020c"
    
    page.add(
        ft.FloatingActionButton(
            icon=ft.icons.ADD_CIRCLE,
            bgcolor=ft.colors.BLUE_500
        )
    )

if __name__ == "__main__":
    ft.app(target=main)