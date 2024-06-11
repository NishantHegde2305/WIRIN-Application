from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class RGBBrightnessApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Label to display RGB values
        self.rgb_label = Label(text='RGB: (0, 0, 0)', size_hint=(1, None), height=50)
        layout.add_widget(self.rgb_label)

        # Color sliders with labels
        for color, label_text in [('red', 'Red'), ('green', 'Green'), ('blue', 'Blue')]:
            slider_layout = BoxLayout(orientation='horizontal')
            slider = Slider(min=0, max=255, value=0, orientation='horizontal')
            setattr(self, f"{color}_slider", slider)  # Store slider in self
            slider_layout.add_widget(Label(text=label_text))
            slider_layout.add_widget(slider)
            layout.add_widget(slider_layout)

            # Bind slider to update color
            slider.bind(value=self.update_color)

        # Brightness slider with label
        brightness_layout = BoxLayout(orientation='horizontal')
        self.brightness_slider = Slider(min=0, max=1, value=1, orientation='horizontal')
        brightness_layout.add_widget(Label(text='Brightness'))
        brightness_layout.add_widget(self.brightness_slider)
        layout.add_widget(brightness_layout)

        # Bind brightness slider to update color
        self.brightness_slider.bind(value=self.update_color)

        # Color display
        self.color_display = Label(size_hint=(1, 0.2))
        layout.add_widget(self.color_display)

        # List to store RGB values
        self.rgb_values = [0, 0, 0]

        # Initial color update
        self.update_color() 

        return layout

    def update_color(self, instance=None, value=None):
        red = self.red_slider.value / 255
        green = self.green_slider.value / 255
        blue = self.blue_slider.value / 255
        brightness = self.brightness_slider.value

        # Update RGB values list
        self.rgb_values = [int(self.red_slider.value), int(self.green_slider.value), int(self.blue_slider.value)]

        # Update RGB label text
        self.rgb_label.text = f'RGB: ({self.rgb_values[0]}, {self.rgb_values[1]}, {self.rgb_values[2]})'

        # Set color and display
        self.color_display.canvas.clear()
        with self.color_display.canvas:
            Color(red * brightness, green * brightness, blue * brightness, 1)
            Rectangle(pos=self.color_display.pos, size=self.color_display.size)

if __name__ == '__main__':
    RGBBrightnessApp().run()
