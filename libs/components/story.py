import flet as ft
from utils import image_loader

def story_view(image: str, username: str):
      return ft.Container(
         content=ft.Column(
            [
               ft.Container(
                  content=ft.Container(
                     content=image_loader(
                        src=image,
                           width=60,
                           height=60,
                           border_radius=100
                        ),
                        border_radius=100,
                        border=ft.border.all(3, ft.colors.WHITE)
                     ),
                     border_radius=100,
                     gradient=ft.LinearGradient(
                     begin=ft.alignment.top_center,
                     end=ft.alignment.bottom_center,
                     colors=[ft.colors.BLUE, ft.colors.YELLOW],
                     rotation=45
                  ),
                  padding=2.5
               ),
               ft.Text(
                  f"@{username}",
                  size=9.5,
                  font_family="Roboto-Medium",
               )
            ],
            spacing=3,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
         ),
      )

def add_story(pfp: str):
   return ft.Column(
         [
            ft.Stack(
               [
                  image_loader(
                     src=pfp,
                     width=60,
                     height=60,
                     border_radius=50
                  ),
                  ft.Container(
                     content=ft.Container(
                        content=ft.Icon(name=ft.icons.ADD, size=13, color=ft.colors.WHITE),
                        width=22,
                        height=22,
                        bgcolor=ft.colors.BLUE,
                        border_radius=100,
                        border=ft.border.all(3, ft.colors.WHITE)
                     ),
                     alignment=ft.alignment.bottom_right
                  )
               ],
               width=60,
               height=60
            ),
            ft.Text(
               "Your Story",
               size=9.5,
               font_family="Roboto-Medium",
            )
         ],
         spacing=5,
         horizontal_alignment=ft.CrossAxisAlignment.CENTER
      )