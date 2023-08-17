import flet as ft
from utils import Icon

class Appbar(ft.Container):
   def __init__(self, *args, **kwargs) -> None:
      super().__init__(*args, **kwargs)

      self.content = self.__create_appbar()
      self.padding = ft.padding.all(10)

   def __create_appbar(self) -> ft.Control:
      appbar = ft.Row(
         [
            self.__create_app_name(),
            self.__create_icons()
         ],
         alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
         vertical_alignment=ft.CrossAxisAlignment.CENTER
      )
      return appbar

   def __create_app_name(self) -> ft.Control:
      appbar_name = ft.Text(
         "Instagram",
         font_family="Fontspring",
         size=22
      )
      return appbar_name

   def __create_icons(self) -> ft.Control:
      appbar_icons = ft.Row(
         [
            Icon(src="icons/like-outline.svg", width=22, height=22),
            Icon(src="icons/messenger-outline.svg", width=22, height=22),
         ],
         spacing=15
      )
      return appbar_icons