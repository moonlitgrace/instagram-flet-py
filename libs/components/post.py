import flet as ft
from flet_core.colors import with_opacity
from utils import image_loader, icon

def post_view(page: ft.Page, pfp: str, username: str, image: str, likes: int, title: str, bg_song: str):
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
                        ft.Text(bg_song, size=9, font_family="Roboto", color=with_opacity(0.75, ft.colors.BLACK))
                     ],
                     spacing=0)
                  ]),
                  icon(src="icons/more.svg", width=22, height=22),
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
                     icon(src="icons/like-outline.svg", width=22, height=22),
                     icon(src="icons/comment.svg", width=22, height=22),
                     icon(src="icons/share.svg", width=18, height=18),
                  ]),
                  icon(src="icons/save.svg", width=17, height=17),
               ],
               alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
               padding=ft.padding.symmetric(vertical=7, horizontal=10)
            ),
            ft.Container(
               content=ft.Column([
                  ft.Text(f"{likes} Likes", font_family="Roboto-Medium", size=11),
                  ft.Row([
                     ft.Text(f"@{username}", font_family="Roboto-Bold", size=11, weight=ft.FontWeight.BOLD),
                     ft.Text(title, font_family="Roboto-Medium", size=11)
                  ]),
                  ft.Text("3hr ago", font_family="Roboto", size=10)
               ],
               spacing=0),
               padding=ft.padding.only(left=10, right=10, bottom=10)
            )
         ],
         spacing=0),
         border=ft.border.only(top=ft.BorderSide(1, ft.colors.with_opacity(0.05, ft.colors.BLACK)))
      )