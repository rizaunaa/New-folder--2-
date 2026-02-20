from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class EmptyScreen(Widget):
    pass


class BlankApp(App):
    def build(self):
        root = EmptyScreen()
        root.add_widget(Label(text="Tampilan Awalan", center=root.center))
        root.bind(size=lambda instance, value: setattr(root.children[0], "center", root.center))
        return root


if __name__ == "__main__":
    BlankApp().run()
