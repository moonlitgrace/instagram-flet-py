import flet as ft

def main(page: ft.Page):
    page.bgcolor = "#03020c"
    page.window_width = 330
    page.window_height = 660

    page.fonts = {
        "Poppins": "/fonts/Poppins/Poppins-regular.ttf",
    }

    page.add(ft.Text("Instagram", font_family="Poppins"))

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")