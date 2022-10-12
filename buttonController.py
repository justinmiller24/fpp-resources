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
import subprocess
from adafruit_seesaw.seesaw import Seesaw
from adafruit_seesaw.digitalio import DigitalIO
from adafruit_seesaw.pwmout import PWMOut

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
leds = []
for ledPin in LED_PINS:
    led = PWMOut(qt, ledPin)
    leds.append(led)


# Main Loop
try:
    while True:
        for ledNumber, button in enumerate(btns):
            if not button.value:
                print("Button Pressed:", BUTTON_COLORS[ledNumber])
                leds[ledNumber].duty_cycle = 65535

                # RED
                # Turn off playlist and lights
                if BUTTON_COLORS[ledNumber] == "RED":
                    
                    # Stop running playlist
                    out = subprocess.run(["/opt/fpp/src/fpp", "-c", "stop"], capture_output=True, text=True)
                    print(out.stdout)

                    # Turn off all the channels in the model
                    out = subprocess.run(["/opt/fpp/src/fppmm", "-m", "All", "-s", "0"], capture_output=True, text=True)
                    print(out.stdout)

                    # Turn off the model in overlay mode (just in case)
                    out = subprocess.run(["/opt/fpp/src/fppmm", "-m", "All", "-o", "off"], capture_output=True, text=True)
                    print(out.stdout)


                # GREEN
                # Start Playlist
                elif BUTTON_COLORS[ledNumber] == "GREEN":
                    out = subprocess.run(["/opt/fpp/src/fpp", "-p", "Xmas2022"], capture_output=True, text=True)
                    print(out.stdout)


                # WHITE
                # All lights ON
                elif BUTTON_COLORS[ledNumber] == "WHITE":
                    out = subprocess.run(["/opt/fpp/src/fppmm", "-m", "All", "-o", "on"], capture_output=True, text=True)
                    print(out.stdout)
                    out = subprocess.run(["/opt/fpp/src/fppmm", "-m", "All", "-s", "255"], capture_output=True, text=True)
                    print(out.stdout)


                # BLUE
                # All lights OFF
                elif BUTTON_COLORS[ledNumber] == "BLUE":
                    out = subprocess.run(["/opt/fpp/src/fppmm", "-m", "All", "-s", "0"], capture_output=True, text=True)
                    print(out.stdout)
                    out = subprocess.run(["/opt/fpp/src/fppmm", "-m", "All", "-o", "off"], capture_output=True, text=True)
                    print(out.stdout)


            # Turn off LEDs when button is not pressed
            else:
                leds[ledNumber].duty_cycle = 0


#            qt.digital_write(LED_PINS[ledNumber], True)

except KeyboardInterrupt:
    pass


print("Stopping...")
exit()




