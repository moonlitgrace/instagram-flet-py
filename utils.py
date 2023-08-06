import flet as ft

def image_loader(image: str, width: ft.OptionalNumber, height: int, border_radius: int):
    return ft.Stack(
        [
            ft.Container(
                width=width,
                height=height,
                bgcolor = "#e7ebf4",
                border_radius=border_radius
            ),
            ft.Image(
                src=image,
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