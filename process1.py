import glob
import os
import time
print "loading SimpleCV ..."
from SimpleCV import *
import matplotlib.pyplot as plt

#my_images_path="./"
extension="*.jpeg"

imgIndex=1
for i in range (0,2):

	imgLabel = "%05d" % imgIndex
        imgName = "./snap_"+imgLabel+".jpeg"
	NDVI_imgName="./snap_NDVI"+imgLabel+".jpeg"	
	#my_camera=Camera()
	#my_image=my_camera.getImage()
	#imgName='./test.jpeg'
	os.system('fswebcam '+imgName)

	print "loading in image ..."
	#print 
	img=Image(imgName)
	channels=img.splitChannels()
	array_r=channels[0].getNumpy()[:,:,0].astype(np.float64) #red channel
	array_b=channels[2].getNumpy()[:,:,2].astype(np.float64) #blue channel
	num = (array_r - array_b)
	denom= (array_r + array_b)
	arr_ndvi = num / denom
	#fig = plt.figure()
	#fig.set_frameon(false)
	#ax=fig.add_supbplot(111)
	#ax.set_axis_off()
	#ax.patch.set_alpha(0.0)
