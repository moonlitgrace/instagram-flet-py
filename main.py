import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 330
    page.window_height = 660
    # configure custom fonts
    page.fonts = {
        "Poppins": "fonts/Poppins/Poppins-regular.ttf",
        "Fontspring": "fonts/Fontspring/Fontspring-bold.otf",
    }

    page.add(
        ft.Text(
            "Instagram",
            font_family="Fontspring",
            size=20,
        )
    )

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")