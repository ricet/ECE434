#!/bin/bash

SIZE=320x240
rm -rf /tmp/frame.png
TMP_FILE=/tmp/frame.png

convert rice.png -size $SIZE $TMP_FILE

sudo fbi -noverbose -T 1 -a $TMP_FILE