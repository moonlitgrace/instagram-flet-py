import flet as ft
from utils import Icon


class NavigationBar(ft.Container):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.content = self._build_navbar()
        self.padding = ft.padding.all(10)
        self.border = ft.border.only(
            top=ft.BorderSide(1, ft.colors.with_opacity(0.05, ft.colors.BLACK))
        )

    def _build_navbar(self) -> ft.Control:
        return ft.Row(
            [
                Icon(src="icons/home.svg", width=22, height=22),
                Icon(src="icons/search.svg", width=25, height=25),
                Icon(src="icons/add_box.svg", width=25, height=25),
                Icon(src="icons/reel.svg", width=18, height=18),
                Icon(src="icons/user.svg", width=22, height=22),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
        )
