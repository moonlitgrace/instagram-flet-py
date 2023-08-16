import flet as ft
from utils import icon

class NavigationBar(ft.Container):
	def __init__(self, *args, **kwargs) -> None:
		super(NavigationBar, self).__init__(*args, **kwargs)

		self.content = self._create_navbar()
		self.padding=ft.padding.all(10)
		self.border=ft.border.only(top=ft.BorderSide(1, ft.colors.with_opacity(0.05, ft.colors.BLACK)))

	def _create_navbar(self) -> ft.Row:
		return ft.Row([
			    icon(src="icons/home.svg", width=22, height=22),
			    icon(src="icons/search.svg", width=25, height=25),
			    icon(src="icons/add_box.svg", width=25, height=25),
			    icon(src="icons/reel.svg", width=18, height=18),
			    icon(src="icons/user.svg", width=22, height=22),
			],
			alignment=ft.MainAxisAlignment.SPACE_AROUND
		)