#!/bin/bash

cd /sys/class/i2c-adapter/i2c-2

# If the device doesnt exist then create it
if [ ! -d "2-0049" ]
then
    echo tmp101 0x49 > new_device
fi
cd 2-0049/hwmon/hwmon0

# Break temp into whole number and decimals
temp=$(cat temp1_input)
temp1=$((temp/1000))
temp2=$((temp%1000))

echo "The temperature is $temp1.$temp2 degrees Celcius"
