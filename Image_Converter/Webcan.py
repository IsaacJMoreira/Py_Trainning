import cv2

cam = cv2.VideoCapture(0)

#cv2.namedWindow("Python WEBCAM")

frameCounter = 0

while True:
    
    ret,frame = cam.read()

    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Test", frame)

    key = cv2.waitKey(1)

    if key%256 == 27:
        print("Closing the app.")
        break
    elif key%256 == 32:
        print("Photo Taken.")
        testImage = "WebcamTest_{}.png".format(frameCounter)
        cv2.imwrite(testImage, frame)
        frameCounter += 1

    

if cv2.waitKey(1) & 0xFF == ord('q'):#black magic fuckery
        cam.release()
        cv2.destroyAllWindows()
        