import cv2


print("Allahu Mohan")

img = cv2.imread('lena.jpg',1)

print(img)
cv2.imshow('image',img)
key = cv2.waitKey(0) & 0xFF  #if we press a escape button then image will not save and all the windows will be destroyed
#0xFF for 64 bit machine.

if key == 27: #27 for escape key.
    cv2.destroyAllWindows()
elif key == ord('s'):   #takes char which will be pressed.
    cv2.imwrite('lena_copy.png',img)
    cv2.destroyAllWindows()
