import flet as ft

def image_loader(image: str, width: int, height: int):
    return ft.Stack(
        [
            ft.Container(
                width=width,
                height=height,
                bgcolor = "#e7ebf4"
            ),
            ft.Image(
                src=image,
                width=width,
                height=height,
                fit=ft.ImageFit.COVER,
                repeat=ft.ImageRepeat.NO_REPEAT,
            )
        ],
        width=width,
        height=height,
    )