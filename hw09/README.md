# Homework 9

## MAX31820 Temperature Sensors

read_temp.py reads three temp sensors wired to the bone. It first checks that the sensors exists in the sysfs, and if they do it reads them, and prints the temperature in celcius to the terminal. Run with `./read_temp.sh`.

## Logging in Sheets

Logtemp.py reads the sensors every five seconds and logs the data to a Google sheet. Run with `logtemp.py`, assuming there is a credentials.json for the sheets API in the folder. I ran it for a few hours and recorded the data in the sheet here:

https://docs.google.com/spreadsheets/d/1lRBoDwy2f_RQIS3q_zubzs_EQBxOlWuSxRg0qVEB7Uc/edit?usp=sharing

This is the data in a plot:

![plot](plot.jpg)

The activity at the beginning was me holding and blowing on the sensors to change their temperature to check that it was working properly. The dip in temperature in the middle of the graph was either the sun going down or my roommates lowering the thermostat. 
