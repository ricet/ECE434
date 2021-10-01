#!/bin/bash

SIZE=320x240
TMP_FILE=/tmp/frame.png

convert rice.png -gravity Center \
          -stroke '#000C' -pointsize 40 -font Candice -strokewidth 20 -annotate 10 'Tiarnan Rice' \
          -stroke  none   -fill white    -annotate 10 'Tiarnan Rice' \
          -size $SIZE $TMP_FILE

sudo fbi -noverbose -T 1 -a $TMP_FILE