import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 330
    page.window_height = 660
    page.padding = 0
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
                    size=20,
                ),
                ft.IconButton(icon=ft.icons.ADD, icon_size=20)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.symmetric(horizontal=10)
    )

    post_image = ft.Stack(
        [
            ft.Container(
                width=page.window_width,
                height=300,
                bgcolor = "#e7ebf4"
            ),
            ft.Image(
                src=f"https://picsum.photos/300/300",
                width=page.window_width,
                height=300,
                fit=ft.ImageFit.COVER,
                repeat=ft.ImageRepeat.NO_REPEAT,
            )
        ],
        width=page.window_width,
        height=300,
    )

    page.add(
        appbar,
        post_image,
    )

if __name__ == "__main__":
    ft.app(
        target=main,
        assets_dir="assets",
    )