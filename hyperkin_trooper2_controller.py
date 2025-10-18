import inputs

class HyperkinTrooper2Controller:
    """
    A class for interfacing the the Hyperkin Trooper 2 Controller. 
    
    The controller must be plugged in for this class to construct properly!
    """

    # Attributes
    __gamepad_name = "Trooper V2     Trooper V2"

    # Constructor
    def __init__(self):
        available_gamepads = inputs.devices.gamepads
        is_controller_found = False
        for gamepad in available_gamepads:
            if gamepad.name == self.__gamepad_name:
                self.gamepad = gamepad
                is_controller_found = True
        if is_controller_found == False:
            raise ValueError("Hyperkin Trooper 2 Controller not detected!\n\nDouble-check that it is plugged in!")
        self.__controller_state = "IDLE"

    # Get controller state
    def get_controller_state(self) -> str:
        """
        This function reads the ongoing event and parses the event type, code, and state
        to determine the actual state of the controller.
        """
        event = self.gamepad.read()
        for event in events:
            action = self.__parse_event_data(event)
        

    # Parse event data
    def __parse_event_data(self, event) -> str:
        """
        This fuction parses the data in the event object
        """
        match event.ev_type:
            case "Key":
                match event.code:
                    case "BTN_PINKIE":
                        action = "START BUTTON PRESSED"
                    case "BTN_TOP2":
                        action = "SELECT BUTTON PRESSED"
                    case "BTN_TRIGGER":
                        action = "LEFT BUTTON PRESSED"
                    case "BTN_THUMB":
                        action = "RIGHT BUTTON PRESSED"
                    case "BTN_THUMB2":
                        action = "LEFT TRIGGER PRESSED"
                    case "BTN_TOP":
                        action = "RIGHT TRIGGER PRESSED"
            case "Absolute":
                if event.state == 127:
                    action = "IDLE"
                else:
                    match event.code:
                        case "ABS_X":
                            match event.state:
                                case 0:
                                    action = "JOYSTICK LEFT"
                                case 255:
                                    action = "JOYSTICK RIGHT"
                        case "ABS_Y":
                            match event.state:
                                case 0:
                                    action = "JOYSTICK UP"
                                case 255:
                                    action = "JOYSTICK DOWN"
            case _:
                action = "IDLE"
        return action



    