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
from adafruit_seesaw.pwmout import PWMOut

# Initialize I2C
import busio
i2c = busio.I2C(board.SCL, board.SDA)
qt = Seesaw(i2c, addr=0x3A)

# Buttonsi
BUTTON_PINS = (18, 19, 20, 2)
btns = []
for btnPin in BUTTON_PINS:
    btn = DigitalIO(qt, btnPin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    btns.append(btn)

# LEDs
LED_PINS = (12, 13, 0, 1)
leds = []
for ledPin in LED_PINS:
    led = PWMOut(qt, ledPin)
    leds.append(led)

# Loop
while True:
    for ledNumber, button in enumerate(btns):
        if not button.value:
            qt.digital_write(LED_PINS[ledNumber], True)
        else:
            qt.digital_write(LED_PINS[ledNumber], False)

#            for cycle in range(0, 65535, 8000):
#                leds[ledNumber].duty_cycle = cycle
#                time.sleep(0.01)
#            for cycle in range(65534, 0, -8000):
#                leds[ledNumber].duty_cycle = cycle
#                time.sleep(0.01)



