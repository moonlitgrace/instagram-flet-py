import flet as ft
from flet_core.colors import with_opacity
from utils import image_loader, icon
      
class PostView:
   def __init__(self, page: ft.Page, pfp: str, username: str, image: str, likes: int, title: str, bg_song: str):

      self.page = page
      self.pfp = pfp
      self.username = username
      self.image = image
      self.likes = likes
      self.title = title
      self.bg_song = bg_song

   def create_view(self):
      return ft.Container(
         content=ft.Column([
            self._create_header(),
            image_loader(
               src=self.image,
               width=self.page.window_width,
               height=350
            ),
            self._create_options(),
            self._create_footer()
         ],
         spacing=0),
      )

   def _create_header(self):
      return ft.Container(
         content=ft.Row([
            ft.Row([
               image_loader(
                  src=self.pfp,
                  width=30,
                  height=30,
                  border_radius=100
               ),
               ft.Column([
                  ft.Text(self.username, size=12, font_family="Roboto-Medium",),
                  ft.Text(self.bg_song, size=9, font_family="Roboto", color=with_opacity(0.75, ft.colors.BLACK))
               ],
               spacing=0)
            ]),
            icon(src="icons/more.svg", width=22, height=22),
         ],
         alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
         padding=ft.padding.only(left=10, top=10, bottom=10, right=2)
      )

   def _create_options(self):
      return ft.Container(
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
      )

   def _create_footer(self):
      return ft.Container(
         content=ft.Column([
            ft.Text(f"{self.likes} Likes", font_family="Roboto-Medium", size=11),
            ft.Row([
               ft.Text(f"@{self.username}", font_family="Roboto-Bold", size=11, weight=ft.FontWeight.BOLD),
               ft.Text(self.title, font_family="Roboto-Medium", size=11)
            ]),
            ft.Text("3hr ago", font_family="Roboto", size=10)
         ],
         spacing=0),
         padding=ft.padding.only(left=10, right=10, bottom=10)
      )