import flet as ft
from flet_core.colors import with_opacity
from utils import image_loader

def post_view(page: ft.Page, pfp: str, username: str, image: str, likes: int, title: str):
      return ft.Container(
         content=ft.Column([
            ft.Container(
               content=ft.Row([
                  ft.Row([
                     image_loader(
                        src=pfp,
                        width=30,
                        height=30,
                        border_radius=100
                     ),
                     ft.Column([
                        ft.Text(username, size=12, font_family="Roboto-Medium",),
                        ft.Text("One piece ft.Luffy bgm", size=9, font_family="Roboto", color=with_opacity(0.75, ft.colors.BLACK))
                     ],
                     spacing=0)
                  ]),
                  ft.Container(
                     content=ft.Image(
                        src="icons/more.svg",
                        width=22,
                        height=22,
                        fit=ft.ImageFit.COVER,
                        repeat=ft.ImageRepeat.NO_REPEAT
                     )
                  ),
               ],
               alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
               padding=ft.padding.only(left=10, top=10, bottom=10, right=2)
            ),
            image_loader(
               src=image,
               width=page.window_width,
               height=350
            ),
            ft.Container(
               content=ft.Row([
                  ft.Row([
                     ft.Container(
                        content=ft.Image(
                           src="icons/like-outline.svg",
                           width=22,
                           height=22,
                           fit=ft.ImageFit.COVER,
                           repeat=ft.ImageRepeat.NO_REPEAT
                        )
                     ),
                     ft.Container(
                        content=ft.Image(
                           src="icons/comment.svg",
                           width=22,
                           height=22,
                           fit=ft.ImageFit.COVER,
                           repeat=ft.ImageRepeat.NO_REPEAT
                        )
                     ),
                     ft.Container(
                        content=ft.Image(
                           src="icons/share.svg",
                           width=18,
                           height=18,
                           fit=ft.ImageFit.COVER,
                           repeat=ft.ImageRepeat.NO_REPEAT,
                           rotate=0.35
                        )
                     ),
                  ]),
                  ft.Container(
                     content=ft.Image(
                        src="icons/save.svg",
                        width=18,
                        height=18,
                        fit=ft.ImageFit.COVER,
                        repeat=ft.ImageRepeat.NO_REPEAT,
                     )
                  ),
               ],
               alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
               padding=ft.padding.symmetric(vertical=7, horizontal=10)
            ),
            ft.Container(
               content=ft.Text(f"{likes} Likes", font_family="Roboto-Bold", size=11),
               padding=ft.padding.symmetric(horizontal=10)
            ),
            ft.Container(
               content=ft.Row([
                  ft.Text(f"@{username}", font_family="Roboto-Bold", size=11, weight=ft.FontWeight.BOLD),
                  ft.Text(title, font_family="Roboto-Medium", size=11)
               ]),
               padding=ft.padding.symmetric(horizontal=10)
            )
         ],
         spacing=0),
         border=ft.border.only(top=ft.BorderSide(1, ft.colors.with_opacity(0.05, ft.colors.BLACK)))
      )