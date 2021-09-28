## Homework 2

### Buttons and Leds

The code for this part is in buttonled.py. Run with `./buttonled.py`

### Measure a GPIO pin on an Oscilloscope

#### bash/sh

1. Min voltage: 20mV, Max voltage: 3.19V
2. The period is between 238ms - 240ms (~4.2Hz)
3. 240ms is over twice 100ms, so very far
4. The actual period is higher because the code to toggle the pin state takes time to run, on top of the 100ms delay in the loop.
5. With the period argument of 0.1 it uses 20% cpu
6. The lowest period that can be achieved is 40ms. Beyond that changing the sleep time argument has no effect.
    | Sleep Time | Period | CPU Usage |
    |:----------:|:------:|:---------:|
    | 0.1        | 240ms  | 20%       |
    | 0.05       | 138ms  | 31%       |
    | 0.02       | 79ms   | 52%       |
    | 0.005      | 49ms   | 81%       |
    | 0.001      | 40ms   | 100%      |
    | 0.0005     | 40ms   | 100%      |
7. With a sleep time of 0.1 the period is betwen 238 and 240ms, occasionally spiking as high as 248ms.
8. The period is much less stable, more frequently jumping around and going as high as 265ms.
9. I removed the lines where EV was assigned and the code that echoed nothing. The period for a sleep time of 0.1 dropped to 220ms.
10. Changing from bash to sh dropped the period down to 214ms.
11. The lowest period I can get with all of the previous changes is now 14ms, down from 40ms without the changes.

#### Python

The code for this section is togglegpio.py
1. The average period seems to be about 150us, which is 6.7kHz
2. 100% CPU usage
3. A table comparing all of the methods is at the end of this section.

#### C

1. Before modifying the function, the lowest period is about 300us. After changing it to use `lseek()` to reset the file offset to the beginning of the file instead of closing the file and reopening it every time the loop runs the lowest period is about 175us.
2. The max cpu usage is only about 40%.

#### GPIOD

1. Python
    1. Period: 18us, Frequency: 55.5kHz
    2. CPU: 100%
2. C
    1. Period: 3.4us, Frequency: 294kHz
    2. CPU: 100%
3. Python (2 pins)
    1. Period: 19us, Frequency: 52.5kHz
    2. CPU: 100%
4. C (2 pins)
    1. Period: 3.7us, Frequency: 270kHz
    2. CPU: 100%

#### Comparison Table

|   GPIO TOGGLE  |  sh | Python |   C   | C (lseek) | GPIOD Python | GPIOD  C | GPIOD  2 pins Python | GPIOD 2 pins C |
|:--------------:|:---:|:------:|:-----:|:---------:|:------------:|:--------:|:--------------------:|:--------------:|
| Period (ms)    | 40  | 0.150  | 0.300 | 0.175     | 0.018        | 0.0034   | 0.019                | 0.0037         |
| Frequency (Hz) | 25  | 6.7k   | 3.3k  | 5.7k      | 55.5k        | 294k     | 52.5k                | 270k           |
| CPU Usage (%)  | 100 | 100    | 40    | 40        | 100          | 100      | 100                  | 100            |

### Etch-a-sketch

etchasketch_buttons.py runs the etch-a-sketch program from hw01, but the cursor is moved around with buttons instead of the arrow keys. Spacebar is still used to clear the screen and escape to quit.
Run with `./etchasketch_buttons.py [height] [width]` where height and width are the desired size of the drawing area in characters. Ensure that your terminal window is large enough for that size area.


# hw02 grading

| Points      | Description |
| ----------- | ----------- |
|  2/2 | Buttons and LEDs 
|  7/7 | Etch-a-Sketch works
|      | Measuring a gpio pin on an Oscilloscope 
|  2/2 | Questions answered
|  4/4 | Table complete
|  2/2 | gpiod
|      | Security - missing
|  0/1 | ssh port
|  0/1 | iptables 
|  0/1 | fail2ban
| 17/20   | **Total**
Video missing -5 
