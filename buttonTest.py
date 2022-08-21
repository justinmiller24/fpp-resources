# Python script to handle I2C button input and output
# Created by Justin Miller on 8.21.2022


# Install packages (bash)
# sudo apt-get update
# sudo apt-get upgrade
# sudo apt-get install python3-pip
# sudo pip3 install --upgrade setuptools adafruit-python-shell adafruit-blinka circuitpython-i2c-button

# Import Libraries (python)
import time
import board
import busio
from i2c_button import I2C_Button

# Addresses
ADDRS = (0x3A)

# Initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)

#Initialize buttons
btns = []
for addr in enumerate(ADDRS):
    btn = I2C_Button(i2c, addr, name="btn")
    btns.append(btn)
    btn.debounce_ms = 25
    btn.led_bright = btn.led_gran = 0
    btn.led_cycle_ms = btn.led_off_ms = 0

# Clear status of all buttons
def clearAll():
    for cbtn in btns:
        cbtn.clear()


clearAll()
while True:
    clicked = [btn for btn in btns if btn.status.been_clicked]
    nclicked = len(clicked)
    if nclicked == 0:
        continue
    for btn in btns:
        btn.led_bright = 0
    if nclicked == 1:
        wbtn = clicked[0]
        wbtn.led_bright = 255
        print(wbtn.name)
    clearAll()



