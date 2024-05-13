from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
import os

class CafeLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.active_button = None
        self.info_label = Label(text='', size_hint=(0.8, 0.1), pos_hint={'center_x': 0.5, 'top': 1})
        self.add_widget(self.info_label)
        self.create_ui_elements()

    def create_ui_elements(self):
        button_specs = {
            'Entrance': {'center_x': 0.5, 'center_y': 0.9, 'module': 'entrance'},
            'Exit': {'center_x': 0.5, 'center_y': 0.1, 'module': 'exit'},
            'Main Hall': {'center_x': 0.5, 'center_y': 0.5, 'module': 'main_hall'},
            'Table 1': {'center_x': 0.25, 'center_y': 0.7, 'module': 'table1'},
            'Table 2': {'center_x': 0.75, 'center_y': 0.7, 'module': 'table2'},
            'Table 3': {'center_x': 0.25, 'center_y': 0.3, 'module': 'table3'},
            'Table 4': {'center_x': 0.75, 'center_y': 0.3, 'module': 'table4'}
        }
        for name, info in button_specs.items():
            btn = Button(text=name, size_hint=(0.1, 0.05), pos_hint={'center_x': info['center_x'], 'center_y': info['center_y']}, background_color=[1, 0.5, 0, 1])
            btn.bind(on_press=lambda instance, module=info['module']: self.handle_button_press(instance, module))
            self.add_widget(btn)

    def handle_button_press(self, instance, module):
        if self.active_button and self.active_button != instance:
            self.info_label.text = "Another button is active"
            return
        if self.active_button is instance:
            instance.background_color = [1, 0.5, 0, 1]  # Reset to original color orange
            self.active_button = None
            self.info_label.text = ''
        else:
            instance.background_color = [0, 0, 1, 1]  # Change color to blue when active
            self.active_button = instance
            try:
                module_run = __import__(module).run
                module_run()
                self.info_label.text = f'{module.capitalize()} activated.'
            except ImportError:
                self.info_label.text = f'Error: Module {module} not found.'

class CafeApp(App):
    def build(self):
        return CafeLayout()

if __name__ == '__main__':
    CafeApp().run()
