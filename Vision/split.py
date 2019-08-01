import cv2
 

def printInfo(cap):
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # float

        # or
        #width = vcap.get(3)  # float
        #height = vcap.get(4) # float

        # it gives me 0.0 :/
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("width is {}, height: {}, fps: {}".format(width, height, fps))
    
    
# Opens the Video file
cap= cv2.VideoCapture('c:/Users/sujoe/Downloads/videoplayback.mp4')
i=0
interval = 3
begin=0
end=30

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False or i > end:
        break
    
    if i % interval == 0 and i >= begin:
        cv2.imwrite('img/run_{:06d}.jpg'.format(i*33), frame)
    print("i is: " + str(i))
    i+=1

printInfo(cap)

cap.release()
cv2.destroyAllWindows()
