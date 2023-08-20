import flet as ft
from utils import Icon


class Appbar(ft.Container):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.content = self._build_appbar()
        self.padding = ft.padding.all(10)

    def _build_appbar(self) -> ft.Control:
        return ft.Row(
            [self._build_app_name(), self._build_icons()],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def _build_app_name(self) -> ft.Control:
        return ft.Text("Instagram", font_family="Fontspring", size=22)

    def _build_icons(self) -> ft.Control:
        return ft.Row(
            [
                Icon(src="icons/like-outline.svg", width=22, height=22),
                Icon(src="icons/messenger-outline.svg", width=22, height=22),
            ],
            spacing=15,
        )
