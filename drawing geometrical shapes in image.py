import cv2
import numpy as np


#img = cv2.imread('lena.jpg',1)
#create img using numpy zeros method
img = np.zeros([512,512,3], np.uint8) #creating a black img
#np.uint8 is data type


#draw line on the image
img = cv2.line(img,(0,0), (255,255),(0,0,255),5)#args-> image var,starting co-ordinate, end co-ordinate,BGR color format,thickness
#**** BGR -> blue,green,red


img = cv2.arrowedLine(img,(5,80), (255,255),(0,0,255),5)#args-> image var,starting co-ordinate, end co-ordinate,BGR color format,thickness
img = cv2.rectangle(img,(3,300),(519,200),(0,255,0),5) #img, top left vertex, lower left vertex,color,thickness= -1 will be filled by the color.
img = cv2.circle(img,(300,230),89,(0,255,0),-1) #img, top left vertex, lower left vertex,color,thickness= -1 will be filled by the color.

#put some text on image
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
img = cv2.putText(img,'Python',(3 ,500),font,4,(255,255,230),4,cv2.LINE_AA)


cv2.imshow('image',img)


cv2.waitKey(0)
cv2.destroyAllWindows()
