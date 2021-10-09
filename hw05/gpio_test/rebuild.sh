#!/bin/bash

sudo rmmod gpio_test
make clean
make
sudo insmod gpio_test.ko
