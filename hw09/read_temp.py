#!/usr/bin/env python3

import time, math, os, sys

def read_temp(sensor_num):
    if os.path.isdir("/sys/class/hwmon/hwmon" + str(sensor_num)):
        with open("/sys/class/hwmon/hwmon" + str(sensor_num) + "/temp1_input") as f:
            return int(f.read())/1000
    else:
        print("Invalid sensor number")
        return None

def main():

    # Exit if no sensors are found
    if not os.path.isdir("/sys/class/hwmon/hwmon0"):
        sys.exit("No temp sensors found!")

    temp1 = read_temp(0)
    temp2 = read_temp(1)
    temp3 = read_temp(2)
    print("Temp 1: " + str(temp1) + " degrees C\n")
    print("Temp 2: " + str(temp2) + " degrees C\n")
    print("Temp 3: " + str(temp3) + " degrees C\n")


if __name__ == "__main__":
    main()
