#!/bin/bash

SIZE=320x240
TMP_FILE=frame.png

convert rice.png -stroke '#000C' -strokewidth 2 -annotate 0 'TIARNAN RICE' \
          -stroke  none   -fill white    -annotate 0 'TIARNAN RICE' \
          $TMP_FILE

sudo fbi -noverbose -T 1 $TMP_FILE