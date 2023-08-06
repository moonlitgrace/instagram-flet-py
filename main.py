import flet as ft

from utils import image_loader

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
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
                    size=22,
                ),
                ft.Row(
                    [
                        ft.IconButton(
                            content=ft.Image(
                                src="icons/like-outline.svg",
                                width=22,
                                height=22,
                                fit=ft.ImageFit.COVER,
                                repeat=ft.ImageRepeat.NO_REPEAT,
                            )
                        ),
                        ft.IconButton(
                            content=ft.Image(
                                src="icons/messenger-outline.svg",
                                width=22,
                                height=22,
                                fit=ft.ImageFit.COVER,
                                repeat=ft.ImageRepeat.NO_REPEAT,
                            )
                        )
                    ],
                    spacing=0
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.only(left=10, right=10, top=5)
    )

    stories = ft.Container(
        content = ft.Row(
            [
                ft.Column(
                    [
                        ft.Stack(
                            [
                                image_loader(
                                    src="images/tokito.jpg",
                                    width=45,
                                    height=45,
                                    border_radius=50,
                                ),
                            ]
                        ),
                        ft.Text("Your Story")
                    ]
                )
            ],
        ),
        padding=ft.padding.symmetric(horizontal=10)  
    )

    page.add(
        appbar,
        stories,
        image_loader(
            src="images/post-1.jpg",
            width=page.window_width,
            height=300
        ),
    )

    page.window_width = 330
    page.window_height = 660
    page.update()

if __name__ == "__main__":
    ft.app(
        target=main,
        assets_dir="assets",
    )