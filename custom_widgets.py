from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image


class ClickableImage(ButtonBehavior, Image):
    def __init__(self, action=None, action_args = (), **kwargs):
        super().__init__(**kwargs)
        self.action = action
        self.action_args = action_args

    def on_press(self):
        if self.action:
            self.action(self, *self.action_args)

class UnitCard(ButtonBehavior, Image):
    def __init__(self, is_hero, power, special_effect, name, action=None, action_args = (), **kwargs):
        super().__init__(**kwargs)
        self.action = action
        self.action_args = action_args
        self.is_hero = True if is_hero == 1 else False
        self.power = power
        self.special_effect = special_effect
        self.name = name

    def on_press(self):
        if self.action:
            self.action(self, *self.action_args)
