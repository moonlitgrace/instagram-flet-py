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
                padding=ft.padding.only(
                    top=10,
                    left=10,
                    right=10
                )
            )
        )

    def slider():
        return(
            ft.Stack(
                [
                    ft.Container(
                        width=page.window_width,
                        height=300,
                        bgcolor = "#e7ebf4"
                    ),
                    ft.Image(
                        src=f"https://picsum.photos/300/300",
                        width=page.window_width,
                        height=300,
                        fit=ft.ImageFit.COVER,
                        repeat=ft.ImageRepeat.NO_REPEAT,
                    )
                ],
                width=page.window_width,
                height=300,
            )
        )

    page.add(
        appbar(),
        slider(),
    )

if __name__ == "__main__":
    ft.app(
        target=main,
        assets_dir="assets",
    )