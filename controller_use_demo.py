from hyperkin_trooper2_controller import HyperkinTrooper2Controller

if __name__ == "__main__":

    htc = HyperkinTrooper2Controller()

    while True:
        controller_state = htc.get_controller_state()
        print(controller_state)