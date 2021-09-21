#!/bin/bash
temp=`i2cget -y 2 0x48`
temp2=`i2cget -y 2 0x4a`

tempf=$((temp*9/5+32))
temp2f=$((temp2*9/5+32))
echo "Temp 1 is $tempf degrees F"
echo "Temp 2 is $temp2f degrees F"