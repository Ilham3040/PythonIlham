

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image


class MyApp(App):

    def build(self):
        layout = AnchorLayout(anchor_x ="center" , anchor_y = "center" ,)
        btn = Button(size_hint=(0.18,0.22),background_normal = 'voice.png' )
        layout.add_widget(btn)
        return layout

MyApp().run()