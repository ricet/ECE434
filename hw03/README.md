# Homework 3

### TMP 101

##### readtemp.sh

Reads the temperature from TMP101s on i2c bus 2 at addresses 0x48 and 0x4A. Converts to Fahrenheit and echos it to the terminal. Run with `sudo ./readtemp.sh `.

*I didn't need the sudo*

##### readtemp.py

Does the same thing as readtemp.sh, but also prints the alert state read over i2c. Run with `sudo ./readtemp.py`.

##### settemp.py

Sets the Thigh and Tlow temperature limits on both TMP101s on the bus. The same limits are written to both TMP101s. Run with `sudo ./settemp.py [high] [low]` where high and low are the high and low limits in degrees C. It then will wait for the alert pin on either TMP101 to go low, signaling that Thigh has been exceeded. Once that happens, it will print the temperature of the sensor with the alert.

### Etch-a-sketch

##### etchasketch_matrix.py
etchasketch using the LED matrix and buttons. Run with `sudo ./etchasketch_matrix.py [color]`. Color is the initial color and can be `RED` `GREEN` or `YELLOW`. The buttons are used to move the cursor to draw. Holding down both right and left clears the matrix and holding down both up and down cycles through the colors.

##### etchasketch_encoder.py

Same as etchasketch_matrix.py but uses two rotary encoders to control the x and y position of the cursor. Three buttons are set to change the cursor to a different color and one button clears the screen. First make sure that HDMI is disabled by uncommenting the appropriate line in /boot/uEnv.txt. Then run `./pinconfig.sh` to configure the encoder pins to eQEP. Then run the etchasketch program with `sudo ./etchasketch_encoder.py [color]`. 

# hw03 grading

| Points      | Description |
| ----------- | ----------- |
|  5/5 | TMP101 
|  3/3 |   | setup.sh
|  2/2 |   | Documentation 
|  5/5 | Etch-a-Sketch
|  3/3 |   | setup.sh (pinsetup.sh)
|  2/2 |   | Documentation
| 20/20 | **Total**

Very nicely documented.