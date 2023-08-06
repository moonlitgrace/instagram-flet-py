import flet as ft

from utils import image_loader

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.spacing = 0
    page.bgcolor = ft.colors.BLACK
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
                    color=ft.colors.WHITE,
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
                                color=ft.colors.WHITE,
                            )
                        ),
                        ft.IconButton(
                            content=ft.Image(
                                src="icons/messenger-outline.svg",
                                width=22,
                                height=22,
                                fit=ft.ImageFit.COVER,
                                repeat=ft.ImageRepeat.NO_REPEAT,
                                color=ft.colors.WHITE,
                            )
                        )
                    ],
                    spacing=0
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.symmetric(horizontal=10, vertical=7),
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
                                    width=60,
                                    height=60,
                                    border_radius=50,
                                ),
                                ft.Container(
                                    content=ft.Container(
                                        content=ft.Icon(name=ft.icons.ADD, size=15, color=ft.colors.WHITE),
                                        width=22,
                                        height=22,
                                        bgcolor=ft.colors.BLUE,
                                        border_radius=100,
                                        border=ft.border.all(1.5, ft.colors.WHITE),
                                    ),
                                    alignment=ft.alignment.bottom_right,
                                )
                            ],
                            width=60,
                            height=60,
                        ),
                        ft.Text(
                            "Your Story",
                            size=10,
                            font_family="Poppins",
                            color=ft.colors.WHITE,
                        )
                    ],
                    spacing=5,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            ],
        ),
        padding=ft.padding.symmetric(horizontal=20, vertical=10),
        border=ft.border.symmetric(vertical=ft.BorderSide(1, ft.colors.with_opacity(0.1, ft.colors.WHITE))),
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