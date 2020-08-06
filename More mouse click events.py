import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in  i]
#print(events) #printing all the events

def click_event(event, x, y, flags, param): #these parameters are fixed
    if event == cv2.EVENT_LBUTTONDOWN: #NEED TO CLICK IN THE LEFT BUTTON OF THE MOUSE
        #create a circle for each click and then join those circles using a line
       # cv2.circle(img, (x,y), 3, (0,0,255),-1)
       # points.append((x,y))
        #if len(points) >= 2:
          #  cv2.line(img,points[-1], points[-2], (255,0,0),5) #index -1 means the last index
        blue = img[x,y,0]
        green = img[x,y,1]
        red =  img[x,y,2]

       # cv2.circle(img,(x,y),3,(0,0,255),-1)
        mycolorImage = np.zeros((512,512,3), np.uint8)
        mycolorImage[:] = [blue,green,red]

        cv2.imshow('Color', mycolorImage)

#click on an image and show the color of that place


#img = np.zeros((512, 512, 3), np.uint8)  #for creating the black image
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)

points = []

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
