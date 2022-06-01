import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

Window.size = (640,620)
kivy.require('1.9.0')
tem = []
class myroot(BoxLayout):
    def __init__(self):
        super(myroot,self).__init__()

    def clear(self):
        self.strings.text = ""

    def adding(self):
        global tem 
        tem.append(eval(self.strings.text))
        self.strings.text = str(eval(self.strings.text))
    
    def grand_total(self):
        global tem
        total = 0
        for i in tem:
            total +=i
        self.strings.text = str(total)
        tem = []

    def get_result(self):
        self.strings.text = str(eval(self.strings.text))

    def cal_symbol(self,symbol):
        self.strings.text += symbol

    def black_space(self):
        self.strings.text = self.strings.text.rstrip(self.strings.text[-1])

class calculater(App):
    def build(self):
        return myroot()

cal = calculater()
cal.run()