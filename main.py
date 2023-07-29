import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 330
    page.window_height = 660
    page.padding = 0
    # configure custom fonts
    page.fonts = {
        "Poppins": "fonts/Poppins/Poppins-regular.ttf",
        "Fontspring": "fonts/Fontspring/Fontspring-bold.otf",
    }

    def appbar():
        return (
            ft.Container(
                content = ft.Row(
                    [
                        ft.Text(
                            "Instagram",
                            font_family="Fontspring",
                            size=20,
                        ),
                        ft.IconButton(icon=ft.icons.ADD)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                padding=10
            )
        )

    def slider():
        return(
            ft.Image(
                src=f"https://picsum.photos/200/200",
                width=200,
                height=200,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
            )
        )

    page.add(
        appbar(),
        slider(),
    )

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")