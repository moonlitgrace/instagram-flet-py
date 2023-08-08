import flet as ft

def appbar():
   return ft.Container(
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