import gaugette.ssd1306
import time
import sys

RESET_PIN = 4 
DC_PIN    = 5 

led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN)
led.begin()
led.clear_display()

offset = 0 # flips between 0 and 32 for double buffering

text = "preparing camera ..."
led.draw_text2(0,0,text,1)
text = "(please hold)"
led.draw_text2(0,9,text,1)
led.display()

from SimpleCV import *
led.clear_display()

while True:
    #write the current time to the display on eveother cycle
    if offset == 0:
        text = time.strftime("%A")
	text = "READY!"
        led.draw_text2(0,0,text,1)
        text = time.strftime("%e %b %Y")
	text = "temp=32.3, RH=20.4"
        led.draw_text2(0,9,text,1)
	text = "other stuff"
	led.draw_text2(0,18,text,1)
	## on next screen
        text = time.strftime("%X")
        led.draw_text2(0,32+4,text,3)
        led.display()
        time.sleep(1)
    else:
        time.sleep(1)
        
    # vertically scroll to switch between buffers
    for i in range(0,32):
        offset = (offset + 1) % 64
        led.command(led.SET_START_LINE | offset)
