#!/usr/bin/env python3

import blynklib
# import blynklib_mp as blynklib # micropython import

BLYNK_AUTH = 'SUO_uUitqGqFpkU0gZ6b66zuNvPH5vCL' #insert your Auth Token here
# base lib init
blynk = blynklib.Blynk(BLYNK_AUTH, port=8442)

while True:
   blynk.run()
