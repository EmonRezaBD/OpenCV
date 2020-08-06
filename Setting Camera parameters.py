import cv2

#setting camera parameters
#we can set any values


cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#we can set any value but camera will take the precise value for it.
# for my camera max 1280*720 , 640*480

cap.set(3, 640) #weidth will be 640 , 3 is for weidth
cap.set(4, 480) #height will be 480 , 4 is for height


print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        #else:
           #break
cap.release()
cv2.destroyAllWindows()

print('ok')

