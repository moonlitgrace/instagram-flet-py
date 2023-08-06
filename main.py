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

    appbar = ft.Container(
        content = ft.Row(
            [
                ft.Text(
                    "Instagram",
                    font_family="Fontspring",
                    size=20,
                ),
                ft.IconButton(
                    content=ft.Image(
                        src="icons/like-outline.svg",
                        width=20,
                        height=20,
                        fit=ft.ImageFit.COVER,
                        repeat=ft.ImageRepeat.NO_REPEAT,
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.only(left=10, right=10, top=5)
    )

    def image_loader(image: str):
        return ft.Stack(
            [
                ft.Container(
                    width=page.window_width,
                    height=300,
                    bgcolor = "#e7ebf4"
                ),
                ft.Image(
                    src=image,
                    width=page.window_width,
                    height=300,
                    fit=ft.ImageFit.COVER,
                    repeat=ft.ImageRepeat.NO_REPEAT,
                )
            ],
            width=page.window_width,
            height=300,
        )

    page.add(
        appbar,
        image_loader("https://picsum.photos/300/300")
    )

if __name__ == "__main__":
    ft.app(
        target=main,
        assets_dir="assets",
    )