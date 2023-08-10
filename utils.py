import flet as ft

def image_loader(src: str, width: ft.OptionalNumber, height: int, border_radius: int = 0):
   return ft.Stack(
      [
         ft.Container(
            width=width,
            height=height,
            bgcolor = "#e7ebf4",
            border_radius=border_radius
         ),
         ft.Image(
            src=src,
            width=width,
            height=height,
            fit=ft.ImageFit.COVER,
            repeat=ft.ImageRepeat.NO_REPEAT,
            border_radius=border_radius
         )
      ],
      width=width,
      height=height,
   )

def icon(src: str, width: int, height: int) -> ft.Container:
   return ft.Container(
      content=ft.Image(
         src=src,
         width=width,
         height=height,
         fit=ft.ImageFit.COVER,
         repeat=ft.ImageRepeat.NO_REPEAT
      )
   )