import flet as ft
from utils import image_loader
# Components
from libs.components.appbar import appbar
from libs.components.story import story_view, add_story
from libs.components.post import post_view
from libs.components.navigation_bar import navigation_bar

def main(page: ft.Page):
   page.theme_mode = ft.ThemeMode.LIGHT
   page.padding = 0
   page.spacing = 0
   page.window_width = 330
   page.window_height = 660
   page.update()
   # configure custom fonts
   page.fonts = {
      # Instagram logo font
      "Fontspring": "fonts/Fontspring/Fontspring-bold.otf",
      # Roboto ( default font ) variants
      "Roboto": "fonts/Roboto/Roboto-Regular.ttf",
      "Roboto-Medium": "fonts/Roboto/Roboto-Medium.ttf",
      "Roboto-Bold": "fonts/Roboto/Roboto-Bold.ttf",
   }

   stories = ft.Container(
      content = ft.Row(
         [
            ft.Container(
               content=ft.Row(
                  [
                     # add story button
                     add_story(pfp="images/tokito.jpg"),
                     # other stories
                     story_view(image="images/baseplate.png", username="sheldon_shit"),
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

   page.add(
      ft.ListView([
         appbar(),
         stories,
         post_view(
            page=page,
            pfp="images/tokito.jpg",
            username="tokitou_san",
            image="images/post-1.jpg",
            likes=10574,
            title="⚡ Joyboy has returned!!!",
            bg_song="One piece ft.Luffy bgm"
         ),
      ],
      expand=True),
      navigation_bar
   )

if __name__ == "__main__":
   ft.app(
      target=main,
      assets_dir="assets",
   )