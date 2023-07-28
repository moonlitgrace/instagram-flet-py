from kivy.config import Config
# configure width and height for window
Config.set("graphics", "width", str(300))

from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.label import MDLabel

class MainApp(MDApp):
    def __init__(self, *args, **kwargs):
        super(MainApp, self).__init__(*args, **kwargs)

    def build_app(self):
        return MDLabel(text="Instagram")

if __name__ == "__main__":
    MainApp().run()