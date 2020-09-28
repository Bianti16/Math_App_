## Kivy imports
from kivy.config import Config

Config.set('graphics', 'width', 450)
Config.set('graphics', 'height', 860)

from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button

## KivyMD imports
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog

# Dependencies:
import math


## App:
class MainMenu(Screen):
    pass

class Points(Screen):
    pass

class P_in_Line(Screen):
    state = 'Duke kalk. lambdën'

    def __init__(self, **kwargs):
        super(P_in_Line, self).__init__(**kwargs)

        input_label = ObjectProperty(None)
        result_label = ObjectProperty(None)

        x1_value = ObjectProperty(None)
        x2_value = ObjectProperty(None)

        state_label = ObjectProperty(None)
        third_input_label = ObjectProperty(None)

        self.btn = MDRectangleFlatButton(text='Kalkulo pikën', size_hint=(0.4, 0.07), font_size='16',
                                         pos_hint={'right': 0.94, 'y': 0.03}, on_release=toggle)
        self.add_widget(self.btn)

    def calculate(self):
        try:
            if self.state == 'Duke kalk. lambdën':
                x1 = float(self.x1_value.text)
                x2 = float(self.x2_value.text)

                point_p = float(self.input_label.text)

                if point_p > x2 or point_p < x1:
                    self.result_label.text = f'Vlerë e pamundur për P!'
                elif point_p == x2:
                    self.result_label.text = f'Rez: Infinit'
                else:

                    lambda_result = (x1 - point_p) / (point_p - x2)

                    if str(lambda_result).endswith('.0'):
                        self.result_label.text = f'Rez: {str(round(lambda_result))}'
                    else:
                        self.result_label.text = f'Rez: {str(lambda_result)}'

            elif self.state == 'Duke kalk. pikën':
                x1 = float(self.x1_value.text)
                x2 = float(self.x2_value.text)

                lambda_value = float(self.input_label.text)

                if lambda_value < 0:
                    self.result_label.text = 'Vlerë e pamundur për lambda!'
                else:
                    result = (x1 + lambda_value * x2) / (1 + lambda_value)
                    if str(result).endswith('.0'):
                        self.result_label.text = str(f'Rez: {round(result)}')
                    else:
                        self.result_label.text = str(f'Rez: {result}')
        except:
            toast('Informacion i gabuar për një ose më shumë fusha')

    def clear(self):
        self.x1_value.text = ''
        self.x2_value.text = ''
        self.input_label.text = ''
        self.result_label.text = 'Rez: '

class P_in_Plane(Screen):
    x_one = ObjectProperty(None)
    y_one = ObjectProperty(None)
    x_two = ObjectProperty(None)
    y_two = ObjectProperty(None)

    result_label_plane = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(P_in_Plane, self).__init__(**kwargs)

    def calculate_distance_plane(self):
        try:
            x1 = float(self.x_one.text)
            y1 = float(self.y_one.text)
            x2 = float(self.x_two.text)
            y2 = float(self.y_two.text)

            result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            if str(result).endswith('.0'):
                self.result_label_plane.text = f'D: {round(result)}'
            else:
                self.result_label_plane.text = f'D: {result}'
        except:
            toast('Informacion i gabuar për një ose më shumë fusha')

    def clear(self):
        self.x_one.text = ''
        self.y_one.text = ''
        self.x_two.text = ''
        self.y_two.text = ''
        self.result_label_plane.text = 'D: '

def toggle(self):
    if self.text == 'Kalkulo lambdën':
        self.text = 'Kalkulo pikën'
        self.parent.state = 'Duke kalk. lambdën'
        self.parent.third_input_label.text = 'Pika'
        self.parent.third_input_label.pos_hint = {'x': 0.72, 'y': 0.89}

    elif self.text == 'Kalkulo pikën':
        self.text = 'Kalkulo lambdën'
        self.parent.state = 'Duke kalk. pikën'
        self.parent.third_input_label.text = 'Lambda'
        self.parent.third_input_label.pos_hint = {'x': 0.77, 'y': 0.89}

    self.parent.state_label.text = str(self.parent.state)

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = '700'
        self.theme_cls.theme_style = 'Dark'
        screen = Builder.load_file('Design.kv')

        return screen

MyApp().run()