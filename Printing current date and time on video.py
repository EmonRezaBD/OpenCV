import cv2
import datetime #for date time

#show date and time on video

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#we can set any value but camera will take the precise value for it.
# for my camera max 1280*720 , 640*480

cap.set(3, 640) #weidth will be 640 , 3 is for weidth
cap.set(4, 480) #height will be 480 , 4 is for height

print(cap.get(3))
print(cap.get(4))


while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX

        text = 'Width: '+str(cap.get(3))+' '+'Height: '+str(cap.get(4)) #concating the string
        currentDate = str(datetime.datetime.now()) #will return the current date and time

        #frame =  cv2.putText(frame, text, (10,50), font, 1, (255,255,255), 2, cv2.LINE_AA )#frame is nothing but image, and video is the combination of images
        frame =  cv2.putText(frame, currentDate, (10,50), font, 1, (255,0,255), 2, cv2.LINE_AA )#frame is nothing but image, and video is the combination of images

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        #else:
        #   break
cap.release()
cv2.destroyAllWindows()

print('ok')

