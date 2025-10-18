import serial
from serial.tools.list_ports import comports

# Main
if __name__ == "__main__":

    # List available ports
    ports = comports()
    print(f"{len(ports)} available ports found:")
    for port in ports:
        print(f"\t{port.device}")

    