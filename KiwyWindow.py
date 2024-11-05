from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

class KivyWindow(App):
    def build(self):
        self.dark = False
        layout = BoxLayout(orientation='vertical')
        Window.size = (600, 400)
        
        self.cycle_color_button = Button(text='Cycle Color', size_hint=(None, None), size=(64, 64),
                                         background_color=(0.294, 0.0, 0.509, 1), color=(1, 1, 1, 1))  # Indigo
        self.cycle_color_button.bind(on_press=self.cycle_color)
        
        self.exit_button = Button(text='Exit', size_hint=(None, None), size=(64, 64),
                                  background_color=(0.863, 0.078, 0.235, 1), color=(1, 1, 1, 1))  # Crimson
        self.exit_button.bind(on_press=self.stop)
        
        # Create a sub-layout for cycle button to center it at the top
        top_layout = BoxLayout(size_hint_y=None, height=64)
        top_layout.add_widget(self.cycle_color_button)
        layout.add_widget(top_layout)
        
        # Add empty space in the middle
        layout.add_widget(BoxLayout())
        
        # Create a sub-layout for exit button to place it at the bottom left
        bottom_layout = BoxLayout(size_hint_y=None, height=64)
        bottom_layout.add_widget(self.exit_button)
        layout.add_widget(bottom_layout)
        
        Window.clearcolor = (0.184, 0.310, 0.310, 1)  # Dark Slate Gray
        return layout
    
    def cycle_color(self, instance):
        if self.dark:
            self.cycle_color_button.background_color = (0.294, 0.0, 0.509, 1)  # Indigo
        else:
            self.cycle_color_button.background_color = (0.545, 0.0, 0.0, 1)  # Dark Red
        self.dark = not self.dark

def run_kivy():
    KivyWindow().run()

if __name__ == "__main__":
    run_kivy()
