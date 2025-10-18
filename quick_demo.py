import inputs
import time
import sys

if __name__ == "__main__":

    expected_name = "Trooper V2     Trooper V2"

    gamepad = inputs.devices.gamepads
    gp = gamepad[0]

    while True:
        events = gp.read()
        for event in events:
            if event.ev_type == "Absolute":
                if event.state == 127:
                    print("Joystick: HOME")
                elif event.code == "ABS_X":
                    if event.state == 0:
                        print(f"Joystick: LEFT")
                    elif event.state == 255:
                        print(f"Joystick: RIGHT")
                elif event.code == "ABS_Y":
                    if event.state == 0:
                        print(f"Joystick: UP")
                    elif event.state == 255:
                        print(f"Joystick: DOWN")
            elif event.ev_type == "Key":
                if event.state != 0:
                    if event.code == "BTN_TRIGGER":
                        print(f"Left Button Pressed")
                    elif event.code == "BTN_THUMB":
                        print(f"Right Button Pressed")
                    elif event.code == "BTN_TOP2":
                        print(f"SELECT Button Pressed")
                    elif event.code == "BTN_PINKIE":
                        print(f"START Button Pressed")

                
                

        
