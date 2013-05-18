#!/usr/bin/env python

from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)


#for i in range(0,90):
#	imgLabel = "%05d" % i
#	imgName = "snap_"+imgLabel+".jpeg"
	 
#	os.system('fswebcam '+imgName)
#	sleep(1)


imgIndex=0

while True:

	imgLabel = "%05d" % imgIndex
	imgName = "snap_"+imgLabel+".jpeg"
        if ( GPIO.input(25)== True ):
                #os.system('mpg321 vader.mp3 &')
                #os.system('fswebcam test.jpeg')
                #print "Switch connected"
                os.system('fswebcam '+imgName)
		imgIndex=imgIndex+1
		sleep(2)
        #else:
                #print "Switch disconnected"
        sleep(0.1);
