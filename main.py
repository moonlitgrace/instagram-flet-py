import flet as ft

from utils import image_loader

def main(page: ft.Page):
   page.theme_mode = ft.ThemeMode.LIGHT
   page.padding = 0
   page.spacing = 0
   page.scroll = ft.ScrollMode.HIDDEN
   # configure custom fonts
   page.fonts = {
      "Poppins": "fonts/Poppins/Poppins-regular.ttf",
      "Fontspring": "fonts/Fontspring/Fontspring-bold.otf",
   }

   appbar = ft.Container(
      content = ft.Row(
         [
            ft.Text(
               "Instagram",
               font_family="Fontspring",
               size=22
            ),
            ft.Row(
               [
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
                        src="icons/messenger-outline.svg",
                        width=22,
                        height=22,
                        fit=ft.ImageFit.COVER,
                        repeat=ft.ImageRepeat.NO_REPEAT
                     )
                  )
               ],
               spacing=15
            )
         ],
         alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
         vertical_alignment=ft.CrossAxisAlignment.CENTER
      ),
      padding=ft.padding.all(10),
      border=ft.border.only(bottom=ft.BorderSide(1, ft.colors.with_opacity(0.05, ft.colors.BLACK)))
   )

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
                  username,
                  size=8,
                  font_family="Poppins",
                  weight=ft.FontWeight.BOLD
               )
            ],
            spacing=3,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
         ),
      )

   addstory = ft.Column(
      [
         ft.Stack(
            [
               image_loader(
                  src="images/tokito.jpg",
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
            size=8,
            font_family="Poppins",
            weight=ft.FontWeight.BOLD
         )
      ],
      spacing=5,
      horizontal_alignment=ft.CrossAxisAlignment.CENTER
   )

   stories = ft.Container(
      content = ft.Row(
         [
            ft.Container(
               content=ft.Row(
                  [
                     # add story button
                     addstory,
                     # other stories
                     story_view(image="images/baseplate.png", username="sheldon"),
                     story_view(image="images/pfp-1.jpg", username="marin"),
                     story_view(image="images/pfp-2.jpg", username="sunx_prox"),
                     story_view(image="images/pfp-3.jpg", username="monkey.d.luffy"),
                     story_view(image="images/pfp-4.jpg", username="sssuneeth"),
                  ]
               ),
               padding=ft.padding.symmetric(horizontal=10)
            )
         ],
         scroll=ft.ScrollMode.HIDDEN
      ),
      padding=ft.padding.symmetric(vertical=10)
   )

   def post_view(pfp: str, username: str, image: str, likes: int, title: str):
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
                     ft.Text(username, size=10, font_family="Poppins", weight=ft.FontWeight.BOLD)
                  ]),
                  ft.Image(src="icons/more.svg", height=20)
               ],
               alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
               padding=ft.padding.all(10)
            ),
            image_loader(
               src=image,
               width=page.window_width,
               height=300
            ),
         ],
         spacing=0),
         border=ft.border.only(top=ft.BorderSide(1, ft.colors.with_opacity(0.05, ft.colors.BLACK)))
      )

   page.add(
      appbar,
      stories,
      post_view(
         pfp="images/tokito.jpg",
         username="tokitou-san",
         image="images/post-1.jpg",
         likes=106,
         title="Joyboy has returned"
      ),
   )

   page.window_width = 330
   page.window_height = 660
   page.update()

if __name__ == "__main__":
   ft.app(
      target=main,
      assets_dir="assets",
   )