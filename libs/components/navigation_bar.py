import flet as ft
from utils import icon

navigation_bar = ft.Container(
	content=ft.Row([
	    icon(src="icons/home.svg", width=22, height=22),
	    icon(src="icons/search.svg", width=25, height=25),
	    icon(src="icons/add_box.svg", width=22, height=22),
	    icon(src="icons/reel.svg", width=18, height=18),
	    icon(src="icons/user.svg", width=22, height=22),
	],
	alignment=ft.MainAxisAlignment.SPACE_AROUND),
	padding=ft.padding.all(10)
)