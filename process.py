#from imgproc import *
import glob
import os
import time
from SimpleCV import *

#my_images_path="./"
extension="*.jpeg"


path=os.getcwd()
directory=os.path.join(path,extension)
files=glob.glob(directory)
print files
index=1
for file in files:
	print file
	new_img = Image(file)
	pixel=new_img[120,64]
	print pixel
	red,green,blue=pixel
	
	outfilename=str(index)+".jpeg"
	new_img.save(outfilename)	
	time.sleep(1)
