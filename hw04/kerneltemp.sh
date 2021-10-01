#!/bin/bash

cd /sys/class/i2c-adapter/i2c-2
echo tmp101 0x49 > new_device
cd 2-0049/hwmon/hwmon0
cat temp1_input