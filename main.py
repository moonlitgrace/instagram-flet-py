from typing import List

import flet as ft

# Components
from libs.components.appbar import Appbar
from libs.components.navigation_bar import NavigationBar
from libs.components.post import PostView
from libs.components.story import AddStory, StoryView
from utils import ImageLoader


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.spacing = 0
    page.window_width = 330
    page.window_height = 660
    # configure custom fonts
    page.fonts = {
        # Instagram logo font
        "Fontspring": "fonts/Fontspring/Fontspring-bold.otf",
        # Roboto ( default font ) variants
        "Roboto": "fonts/Roboto/Roboto-Regular.ttf",
        "Roboto-Medium": "fonts/Roboto/Roboto-Medium.ttf",
        "Roboto-Bold": "fonts/Roboto/Roboto-Bold.ttf",
    }
    page.update()

    class StoriesLayoutView(ft.Container):
        def __init__(self, *args, **kwargs) -> None:
            super(StoriesLayoutView, self).__init__(*args, **kwargs)

            self._initialize_data()

            self.content = self._create_view()
            self.padding = ft.padding.symmetric(vertical=10)
            self.border = ft.border.symmetric(
                vertical=ft.BorderSide(1, ft.colors.with_opacity(0.05, ft.colors.BLACK))
            )

        def _initialize_data(self) -> None:
            self.datas = [
                {"image": "images/baseplate.png", "username": "sheldon_shit"},
                {"image": "images/pfp-1.jpg", "username": "marin"},
                {"image": "images/pfp-2.jpg", "username": "sunx_prox"},
                {"image": "images/pfp-3.jpg", "username": "monkey.d.luffy"},
                {"image": "images/pfp-4.jpg", "username": "sssuneeth"},
            ]

            self.stories = [StoryView(**data).build_view() for data in self.datas]
            self.add_story = AddStory(pfp="images/tokito.jpg").build_view()

        def _create_view(self) -> ft.Control:
            return ft.Row(
                [
                    ft.Container(
                        content=ft.Row([self.add_story, ft.Row(controls=self.stories)]),
                        padding=ft.padding.symmetric(horizontal=10),
                    )
                ],
                scroll=ft.ScrollMode.HIDDEN,
            )

    class PostsLayoutView(ft.ListView):
        def __init__(self, *args, **kwargs) -> None:
            super(PostsLayoutView, self).__init__(*args, **kwargs)

            self._initialize_data()
            self.controls = [PostView(**data).build_view() for data in self.datas]

        def _initialize_data(self) -> None:
            self.datas = [
                {
                    "page": page,
                    "pfp": "images/tokito.jpg",
                    "username": "tokitou_san",
                    "image": "images/post-1.jpg",
                    "likes": 10574,
                    "title": "⚡ Joyboy has returned!!!",
                    "bg_song": "One piece ft.Luffy bgm",
                },
                {
                    "page": page,
                    "pfp": "images/baseplate.png",
                    "username": "sheldon_shit",
                    "image": "images/post-2.jpg",
                    "likes": 24875,
                    "title": "Like if I'm a Gay :P",
                    "bg_song": "I'm a Gay!",
                },
            ]

    page.controls = [
        ft.ListView(
            [
                Appbar(),
                StoriesLayoutView(),
                PostsLayoutView(),
            ],
            expand=True,
        ),
        NavigationBar(),
    ]

    page.update()


ft.app(
    target=main,
    assets_dir="assets",
)
