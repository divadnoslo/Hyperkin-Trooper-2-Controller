import inputs
import time
import sys

class HyperkinTrooper2Controller(self):
    """
    A class for interfacing the the Hyperkin Trooper 2 Controller
    """
    def __init__(self):
        return self

    self.map = {
        "Absolute ABS_X 127": "JOYSTICK_HOME", 
        "Absolute ABS_X 0": "JOYSTICK_LEFT",
        "Absolute ABS_X 255": "JOYSTICK_RIGHT",
        "Absolute ABS_Y 127": "JOYSTICK_HOME", 
        "Absolute ABS_Y 0": "JOYSTICK_UP",
        "Absolute ABS_Y 255": "JOYSTICK_DOWN",
        "Key BTN_TRIGGER 1": "LEFT_BUTTON_PUSHED",
        "Key BTN_THUMB 1": "RIGHT_BUTTON_PUSHED",
        "Key BTN_TOP2 1": "SELECT_PUSHED",
        "Key BTN_PINKIE 1": "START_PUSHED",
    }