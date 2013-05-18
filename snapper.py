#!/usr/bin/env python
import gaugette.ssd1306
import time
import sys
import os
import RPI.GPIO as GPIO
from SimpleCV import *

RESET_PIN = 4 
DC_PIN    = 5 

led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN)
led.begin()
led.clear_display()

offset = 0 # flips between 0 and 32 for double buffering

#text = "preparing camera ..."
#led.draw_text2(0,0,text,1)
#text = "(please hold)"
#led.draw_text2(0,9,text,1)
#led.display()


GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)


imgIndex=0

while True:

    text="Ready!"
    led.draw_text2(0,0,text,2)	   
    imgLabel = "%05d" % imgIndex
    imgName = "snap_"+imgLabel+".jpeg"
    if ( GPIO.input(25)== True):
        os.system('fswebcam '+imgName)
        imgIndex=imgIndex+1
	led.clear_display()
	text="snap!"
	led.draw_text2(0,0,text,3)
	time.sleep(2)	
	led.clear_display()
