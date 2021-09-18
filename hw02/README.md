## Homework 2

### Buttons and Leds

The code for this part is in buttonled.py. Run with `./buttonled.py`

### Measure a GPIO pin on an Oscilloscope

#### bash/sh

1. Min voltage: 20mV, Max voltage: 3.19V
2. The period is between 238ms - 240ms (~4.2Hz)
3. 240ms is over twice 100ms, so very far
4. reasons
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
9. 
#### Python

#### C

#### GPIOD
