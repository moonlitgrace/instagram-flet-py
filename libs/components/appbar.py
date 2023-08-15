import flet as ft
from utils import icon

class Appbar(ft.Container):
   def __init__(self, *args, **kwargs):
      super(Appbar, self).__init__(*args, **kwargs)

      self.content = ft.Row(
         [
            ft.Text(
               "Instagram",
               font_family="Fontspring",
               size=22
            ),
            ft.Row(
               [
                  icon(src="icons/like-outline.svg", width=22, height=22),
                  icon(src="icons/messenger-outline.svg", width=22, height=22),
               ],
               spacing=15
            )
         ],
         alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
         vertical_alignment=ft.CrossAxisAlignment.CENTER
      )

      self.padding = ft.padding.all(10)