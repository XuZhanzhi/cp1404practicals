from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        self.title = "Dynamic Labels"
        main_layout = BoxLayout(orientation='vertical')
        self.create_labels(main_layout)
        return main_layout

    def create_labels(self, layout):
        """Create labels for each name and add them to the layout"""
        for name, phone in self.name_to_phone.items():
            label_text = f"{name}'s number is {phone}"
            label = Label(text=label_text, font_size=24)
            layout.add_widget(label)


DynamicLabelsApp().run()
