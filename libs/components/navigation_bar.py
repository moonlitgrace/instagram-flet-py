import flet as ft

navigation_bar = ft.Container(
	content=ft.Row([
		ft.Container(
	        content=ft.Image(
	            src="icons/home.svg",
	            width=22,
	            height=22,
	            fit=ft.ImageFit.COVER,
	           	repeat=ft.ImageRepeat.NO_REPEAT
	        )
	     ),
	]),
	padding=ft.padding.all(10)
)