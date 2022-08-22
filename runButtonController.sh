#!/bin/bash

# Script to make sure button controller script is running
# Created by Justin Miller on 8.21.2022


# Check if running
if pgrep /home/fpp/media/runButtonController.py >/dev/null 2>&1
then
    # Script is running, nothing to do
    exit

else
    # Script is not running, start script
    python buttonController.py >> /home/fpp/media/logs/runButtonController.log 2>&1 &

fi


