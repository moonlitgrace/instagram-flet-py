import flet as ft
from utils import ImageLoader


class StoryView:
    def __init__(self, image: str, username: str) -> None:
        self.image = image
        self.username = username

    def _build_pfp_view(self) -> ft.Container:
        return ft.Container(
            content=ft.Container(
                content=ImageLoader(
                    src=self.image, width=60, height=60, border_radius=100
                ),
                border_radius=100,
                border=ft.border.all(3, ft.colors.WHITE),
            ),
            border_radius=100,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[ft.colors.BLUE, ft.colors.YELLOW],
                rotation=45,
            ),
            padding=2.5,
        )

    def build_view(self) -> ft.Control:
        return ft.Container(
            content=ft.Column(
                [
                    self._build_pfp_view(),
                    ft.Text(f"@{self.username}", size=9.5, font_family="Roboto-Medium"),
                ],
                spacing=3,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )


class AddStory:
    def __init__(self, pfp: str) -> None:
        self.pfp = pfp

    def _build_stack(self) -> ft.Control:
        return ft.Stack(
            [
                ImageLoader(src=self.pfp, width=60, height=60, border_radius=50),
                ft.Container(
                    content=ft.Container(
                        content=ft.Icon(
                            name=ft.icons.ADD, size=13, color=ft.colors.WHITE
                        ),
                        width=22,
                        height=22,
                        bgcolor=ft.colors.BLUE,
                        border_radius=100,
                        border=ft.border.all(3, ft.colors.WHITE),
                    ),
                    alignment=ft.alignment.bottom_right,
                ),
            ],
            width=60,
            height=60,
        )

    def build_view(self) -> ft.Control:
        return ft.Column(
            [
                self._build_stack(),
                ft.Text(
                    "Your Story",
                    size=9.5,
                    font_family="Roboto-Medium",
                ),
            ],
            spacing=5,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
