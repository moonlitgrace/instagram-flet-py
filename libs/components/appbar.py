import flet as ft
from utils import icon

class Appbar(ft.Container):
   def __init__(self, *args, **kwargs):
      super(Appbar, self).__init__(*args, **kwargs)

      self.content = self._create_appbar()
      self.padding = ft.padding.all(10)

   def _create_appbar(self):
      return ft.Row(
         [
            self._create_app_name(),
            self._create_icons()
         ],
         alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
         vertical_alignment=ft.CrossAxisAlignment.CENTER
      )

   def _create_app_name(self):
      return ft.Text(
         "Instagram",
         font_family="Fontspring",
         size=22
      )

   def _create_icons(self):
      return ft.Row(
         [
            icon(src="icons/like-outline.svg", width=22, height=22),
            icon(src="icons/messenger-outline.svg", width=22, height=22),
         ],
         spacing=15
      )