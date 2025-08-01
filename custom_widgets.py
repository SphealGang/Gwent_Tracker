from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.popup import Popup 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class ClickableImage(ButtonBehavior, Image):
    def __init__(self, action=None, action_args = (), **kwargs):
        super().__init__(**kwargs)
        self.action = action
        self.action_args = action_args

    def on_press(self):
        if self.action:
            self.action(self, *self.action_args)

# def delete_card(card,handler,update_score_function):

class UnitCard(ButtonBehavior, Image):
    def __init__(self, is_hero, power, special_effect, name, image_path,delete_card_function, delete_card_function_args = (),**kwargs):
        super().__init__(**kwargs)
        self.is_hero = True if is_hero == 1 else False
        self.power = power
        self.special_effect = special_effect
        self.name = name
        self.image_path = image_path
        self.delete_card_function = delete_card_function
        self.delete_card_function_args = delete_card_function_args

        self.popup_content  = BoxLayout(orientation = 'vertical')

        self.popup = Popup(
            title = 'Card details',
            size_hint=(None, None),
            size=(500, 700),
            content = self.popup_content
        )

        card_image = Image(
            source = self.image_path
        )
        self.popup_content.add_widget(card_image)
        
        delete_button = Button(
            text = 'Delete card',
            size_hint=(1, None),
            height = 50
        )
        self.popup_content.add_widget(delete_button)
        delete_button.bind(on_press=lambda instance: self.delete_card_function(self, *self.delete_card_function_args))

        close_button = Button(
            text = 'Close',
            size_hint=(1, None),
            height = 50
            )
        close_button.bind(on_press = self.popup.dismiss)
        self.popup_content.add_widget(close_button)

    def on_press(self):
        self.popup.open()
