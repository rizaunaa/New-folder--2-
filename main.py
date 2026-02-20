from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label


class BlankApp(App):
    def build(self):
        root = FloatLayout()
        root.add_widget(
            Label(
                text="Tampilan Awalan",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        return root


if __name__ == "__main__":
    BlankApp().run()
