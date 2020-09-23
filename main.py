from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.button import Button
from kivy.lang import Builder

from kivy.properties import ObjectProperty

from kivy.uix.popup import Popup

class P(FloatLayout):
    pass

class MainPage(FloatLayout):

    state = 'Duke kalkuluar lambdën'

    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)

        input_label = ObjectProperty(None)
        result_label = ObjectProperty(None)

        x1_value = ObjectProperty(None)
        x2_value = ObjectProperty(None)

        state_label = ObjectProperty(None)
        third_input_label = ObjectProperty(None)

        self.btn = Button(text='Kalkulo pikën', size_hint=(0.4, 0.07), font_size = 18,
                          pos_hint={'right': 0.94, 'y': 0.03}, on_release = toggle)
        self.add_widget(self.btn)
        
    def calculate(self):
        try:
            if self.state == 'Duke kalkuluar lambdën':
                x1 = float(self.x1_value.text)
                x2 = float(self.x2_value.text)

                point_p = float(self.input_label.text)

                if point_p > x2 or point_p < x1:
                    self.result_label.text = f'Vlerë e pamundur për P!'
                elif point_p == x2:
                    self.result_label.text = f'Rezultati: Infinit'
                else:

                    lambda_result = (x1 - point_p)/(point_p - x2)

                    if str(lambda_result).endswith('.0'):
                        self.result_label.text = f'Rezultati: {str(round(lambda_result))}'
                    else:
                        self.result_label.text = f'Rezultati: {str(lambda_result)}'

            elif self.state == 'Duke kalkuluar pikën':
                x1 = float(self.x1_value.text)
                x2 = float(self.x2_value.text)

                lambda_value = float(self.input_label.text)

                if lambda_value < 0:
                    self.result_label.text = 'Vlerë e pamundur për lambda!'
                else:
                    result = (x1 + lambda_value * x2) / (1 + lambda_value)
                    if str(result).endswith('.0'):
                        self.result_label.text = str(f'Rezultati: {round(result)}')
                    else:
                        self.result_label.text = str(f'Rezultati: {result}')
        except:
            show_popup()

    def clear(self):
        self.x1_value.text = ''
        self.x2_value.text = ''
        self.input_label.text = ''
        self.result_label.text = 'Rezultati: '

def toggle(self):

    if self.text == 'Kalkulo lambdën':
        self.text = 'Kalkulo pikën'
        self.parent.state = 'Duke kalkuluar lambdën'
        self.parent.third_input_label.text = 'Pika'
        self.parent.third_input_label.pos_hint = {'x': 0.75, 'y': 0.9}

    elif self.text == 'Kalkulo pikën':
        self.text = 'Kalkulo lambdën'
        self.parent.state = 'Duke kalkuluar pikën'
        self.parent.third_input_label.text = 'Lambda'
        self.parent.third_input_label.pos_hint = {'x': 0.79, 'y': 0.9}

    self.parent.state_label.text = str(self.parent.state)

def show_popup():
    show = P()
    popup_window = Popup(title="Gabim vlere", content=show, size_hint=(None, None), size=(400, 250),
                             auto_dismiss=False)
    popup_window.open()

kv = Builder.load_file('Design.kv')

class MyApp(App):
    def build(self):
        return MainPage()

if __name__ == '__main__':
    MyApp().run()