from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    def build(self):
        """use kivy file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """calculate miles to kilometers"""
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change_value):
        """change the value +1/-1 with two buttons"""
        value = self.get_validated_miles() + change_value
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """check error input"""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0


MilesConverterApp().run()
