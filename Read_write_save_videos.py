import cv2

print('Bisillah Hir Rahmanir Rahim')

#creating video , we use video capture class
captureVideo = cv2.VideoCapture(0) # arg can a file name, from where we can feed videos. or default arg 0(which is for system
#camera. If u have multile camera then use 0,1,2 etc..

#saving a video ,we need to create a video writer class

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 30.0,(1280,720)) #output file name, fourcc,frame par sec,frame passed as a tuple
# 1280 * 720. Frame should be width then height

#while(True):
while(captureVideo.isOpened()): # when we give the file name but it is not present then it will return false.also works for default camera arg.
    ret,frame = captureVideo.read() # if frame is available then this func will return true which is store in ret and frame will store in frame var.
    if ret==True:

        print(captureVideo.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(captureVideo.get(cv2.CAP_PROP_FRAME_WIDTH))

        out.write(frame) #write the frame of captured video

        # cv2.imshow('frame',frame) #will show the RGB video.
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #convert our image to gray scale.

        cv2.imshow('frame',gray) #'frame' is the name of the camera frame;

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

captureVideo.release()
out.release()
cv2.destroyAllWindows()
