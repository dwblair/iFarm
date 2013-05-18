#!/usr/bin/env python

import gaugette.ssd1306
import time
import sys
import os
import RPi.GPIO as GPIO
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)

#from SimpleCV import *

RESET_PIN = 4 
DC_PIN    = 5 

led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN)
led.begin()
led.clear_display()

offset = 0 # flips between 0 and 32 for double buffering

while True:
    #write the current time to the display on eveother cycle
    if ( GPIO.input(25)== True ):
	led.clear_display()
       	text="SNAP!" 
	led.draw_text2(0,0,text,3)
        led.display()
	
	dt = datetime.datetime.now()
	filename_prefix=dt.strftime("%Y-%m-%d_%H_%M_%S")
	filename=filename_prefix+"_snap.jpeg"
	print filename
	os.system('fswebcam '+filename)

        time.sleep(1)
	led.clear_display()
    else:
	text = "ready."
	led.draw_text2(0,0,text,2)
	text = "temp=30.2 C; RH=33%"
	led.draw_text2(0,18,text,1)	
	led.display()	
        
    # vertically scroll to switch between buffers
    #for i in range(0,32):
    #    offset = (offset + 1) % 64
    #    led.command(led.SET_START_LINE | offset)
