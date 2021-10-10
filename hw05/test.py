#!/usr/bin/python3
import time, math
start_time = time.time()

def read_z():
    with open("/sys/class/i2c-adapter/i2c-2/2-0053/iio:device1/in_accel_z_raw") as f:
        return int(f.read())

def read_x():
    with open("/sys/class/i2c-adapter/i2c-2/2-0053/iio:device1/in_accel_x_raw") as f:
        return int(f.read())

def read_y():
    with open("/sys/class/i2c-adapter/i2c-2/2-0053/iio:device1/in_accel_y_raw") as f:
        return int(f.read())

def magnitude():
    return math.sqrt(read_z()**2 + read_x()**2 + read_y()**2)

while(time.time() - start_time < 2):
    print(str(magnitude()))
    time.sleep(0.05)

