from PIL import Image, ImageOps
import cv2
import os #imports the ability to navegate through the file sistem
'''
This simple program converts an image to an image made of ascii characters.
This version is very crude. Some refacturing must be done

current version: 0.35
date: 31/01/2023
'''
Downscale = 3
#in my tests, those can give you the best result. Feel free to experiment
imageMap =  ("   ", " . ", ". .", "...", ".:.", ":.:", ":::", ":|:", "|:|", "|||", "|#|", "#|#", "###", "#$#", "$#$", "$$$")#map for converting and image to asci. Add as much as you need

#try using the map below
#imageMap = ("   ", " . ", ". .", "...",".,.",",.,",",,,",",-,","-,-","---","-~-","~-~","~~~","~:~",":~:",":::",":;:",":;:",";;;",
#             ";=;","=;=","===","=!=","!=!","!!!","###","#$#","$#$", "$$$","$@$","@$@","@@@")


tryAgain = True
webCam = cv2.VideoCapture(0)#creates a webCam object
exit = False

while True:

    successful, frame = webCam.read()#creates the webCam object and a flag to signal the successin reading the data from Webcam

    if not successful:#if an error had acurred, exit with a message
        print("Unable to access the WebCam.")
        break
        
    cv2.imshow("Press SPACE to take a picture.", frame)#open a window that prompts you to press SPACE

    key = cv2.waitKey(1)#Waits a key press

    if key%256 == 27:#waits esc key
        print("Closing the app.")
        exite = True
        break
    elif key%256 == 32:#takes a picture if space is pressed
        print("Photo Taken.")
        cv2.imwrite("Frame_1.png", frame)
        exit = False #belts, bracers and suspenders
        break
if not exit:
    try:
        img = Image.open("Frame_1.png")
        print("Image loaded successfully.")
        print("Image dimensions: " + str(img.size))#print the tuple that holds the dimentions of the object
        #print(img.format)#print the format
        print(img.format_description)#print the discription of the format ex: JPEG (ISO 10918)
        askAgain = True
        
                    
        img = img.resize(tuple(int(t/Downscale) for t in img.size))#resizes the image
        img = img.convert("L")#converts it to gray scale
        img = ImageOps.invert(img)#inverts the image
                    

        
        TextFile = open("Picture_to_ASCII_1.txt", 'w')#Creates the
        print("File openned successfully.")
        singlePixel = img.load() # we load the BIT object into Pixel, making it a PixelAccess object

        for i in range(img.size[1]):# here we generate the image out of chars
            for w in range(2):
                for j in range(img.size[0]):
                    TextFile.write(imageMap[int(singlePixel[j, i]/(256/len(imageMap)))])
                TextFile.write("\n")
        
        TextFile.close()
            
        print("Conversion is done.")
        tryAgain = False
        #BIT.show()
    except:
        print("Sorry, unable to find the picture taken")
        print("\nEnding prgram.")