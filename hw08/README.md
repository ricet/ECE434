# Homework 8

## Blinking an LED

hello.pru0.c turns pin 9_31 on and off as fast as possible using the ARM gpio registers. Run with `make TARGET=hello.pru0`, and stop with `make TARGET=hello.pru0 stop`.
Below is a scope capture of P9_31 toggling as fast as it can using this method. The fastest that it can toggle is 12.5MHz, and there is a substantial amount of jitter.

![nopru](pics/nopru.png)

## PWM Generator

pwm1.pru0.c toggles P9_31 using the PRU inside the Beaglebone. With no delays the fastest I could make it toggle was about 67MHz. I made the signal symmetric by setting a delay of 1 cycle after turning the pin on, since setting the program counter back to the beginning of the loop after turning the pin off uses 1 clock cycle. With this delay the frequency is 50MHz as shown below. Run with `make TARGET=pwm1.pru0`, and be sure to set the pin to a pru output with `config-pin p9.31 pruout`. The waveform is perfectly stable with no jitter, which is apparent from the ~100ps standard deviation in the period.

![pru](pics/pru.png)

## Controlling the PWM Frequency



![pwm4](pics/pwm4.png)

![pwmtest](pics/pwmtest.png)

## Reading an Input at Regular Intervals

![buttondelay](pics/buttondelay.png)

## Analog Wave Generator

![Sawtooth](pics/sawtooth.png)

![Triangle](pics/triangle.png)

![Sine](pics/sine.png)