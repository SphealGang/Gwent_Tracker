from kivy.app import App,Widget
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup 
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle

from custom_widgets import *
from functions import *

Window.size = (600,900)

class Unit():
    def __init__(self,name,power,is_hero,special_effect):
        self.name = name
        self.power = power
        self.is_hero = is_hero
        self.special_effect = special_effect

class Handler(BoxLayout):
    def __init__(self,type,update_score_function, **kwargs):
        super().__init__(orientation='horizontal', **kwargs)

        self.unit_list = []
        self.faction_power = 0

        self.weather_status = False
        self.commander_horn_status = False

        self.add_card_button = ClickableImage(
            source=r"Gwent Tracker\card_back.png",
            action=lambda instance: add_card(type,self.card_view,self.unit_list,self,self.weather_status,self.commander_horn_status,update_score_function), 
            size_hint = (None,None),
            size = (75,130),
            mipmap=True,
            allow_stretch=False,
            keep_ratio=True
        )
        self.add_widget(self.add_card_button)

        self.battle_horn = ClickableImage(
            source = r"C:\Users\Mihai\OneDrive\Desktop\Projects\Gwent Tracker\page_45_card_2.png",
            size_hint = (None,None),
            size = (75,130)     ,
            mipmap=True,
            allow_stretch=False,
            keep_ratio=True
        )
        self.add_widget(self.battle_horn)

        self.card_scroll_view = ScrollView(
            do_scroll_x=True, 
            do_scroll_y=False, 
            bar_width = 0
            )
        self.add_widget(self.card_scroll_view)

        self.card_view = GridLayout(rows=1,size_hint_x=None)
        self.card_scroll_view.add_widget(self.card_view)

        self.weather_button = ClickableImage(
            source=choose_weather_card(type),
            action= lambda instace: weather_effect(update_score_function,self),
            size_hint = (None,None),
            size = (75,130),
            mipmap=True,
            allow_stretch=False,
            keep_ratio=True
        )
        self.add_widget(self.weather_button)

class PlayerWidget(BoxLayout):
    def __init__(self,top, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        def update_score():
            total = close_combat_handler.faction_power + ranged_combat_handler.faction_power + siege_handler.faction_power
            self.score_label.text = str(total)

        self.total_power = 0

        self.score_label = Label(
            text = '0',
            size_hint = (1, None),
            height = 40,
            font_size = 30
            )

        close_combat_handler = Handler('Close Combat',update_score)
        ranged_combat_handler = Handler('Ranged Combat',update_score)
        siege_handler = Handler('Siege',update_score)

        if top:
            self.add_widget(self.score_label)
        self.add_widget(close_combat_handler)
        self.add_widget(ranged_combat_handler)
        self.add_widget(siege_handler)
        if not top:
            self.add_widget(self.score_label)





class MainApp(App):
    def build(self):
        root = BoxLayout(
            orientation = 'vertical',
            # size_hint_y = .95
            )
        
        root.add_widget(PlayerWidget(top=False))
        root.add_widget(PlayerWidget(top=True))
        

        return root
    
if __name__ == "__main__":
    MainApp().run()