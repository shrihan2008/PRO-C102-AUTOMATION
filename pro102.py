import cv2
#making the function
def snapshot():
    #initalize cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    #when result will be true
    while (result):
        ret,frame=videoCaptureObject.read()
        #storing image
        cv2.imwrite("Image.png",frame)
        result=False
        #image is deleted
    videoCaptureObject.release()
    cv2.destroyAllWindows()
#call function
snapshot()