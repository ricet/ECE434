#!/bin/bash

sudo rmmod led
make clean
make
sudo insmod led.ko
