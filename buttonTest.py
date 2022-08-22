# Python script to handle I2C button input and output
# Created by Justin Miller on 8.21.2022

# Install packages (bash)
# sudo apt-get update
# sudo apt-get upgrade
# sudo apt-get install python3-pip
# sudo pip3 install --upgrade adafruit-blinka adafruit-circuitpython-seesaw

# Import Libraries (python)
import time
import board
import digitalio
from adafruit_seesaw.seesaw import Seesaw
from adafruit_seesaw.digitalio import DigitalIO
#from adafruit_seesaw.pwmout import PWMOut

# Initialize I2C
import busio
i2c = busio.I2C(board.SCL, board.SDA)
qt = Seesaw(i2c, addr=0x3A)

# Buttons
BUTTON_COLORS = ("RED", "WHITE", "GREEN", "BLUE")
BUTTON_PINS = (18, 19, 20, 2)
btns = []
for btnPin in BUTTON_PINS:
    btn = DigitalIO(qt, btnPin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    btns.append(btn)

# LEDs
LED_PINS = (12, 13, 0, 1)


try:
    while True:
        for ledNumber, button in enumerate(btns):
            if not button.value:
                print("Button pushed:", BUTTON_PINS[ledNumber], BUTTON_COLORS[ledNumber])
                print("Light color:", LED_PINS[ledNumber], BUTTON_COLORS[ledNumber])
#            qt.digital_write(LED_PINS[ledNumber], True)

except KeyboardInterrupt:
    pass


print("Stopping...")
exit()




