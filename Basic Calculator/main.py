import kivy
kivy.require("1.11.1")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from os import system
from kivy.config import Config

Config.set('graphics', 'width', '450')
Config.set('graphics', 'height', '600')

class CalcGridLayout(GridLayout):
    def calculate(self,calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
                system('say {}'.format(self.display.text))
            except Exception:
                self.display.text = "Error"

    def percentage(self,percent):
        if percent:
            try:
                self.display.text=str(eval(percent/100))
            except:
                self.display.text = "Error"

class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()
    
calcapp=CalculatorApp()
calcapp.run()