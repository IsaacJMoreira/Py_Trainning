from PIL import Image, ImageOps
import os #imports the ability to navegate through the file siste
'''
This simple program converts an image to an image made of ascii characters.
This version is very crude. Some refacturing must be done

TO DO:

DONE! 1 - make it possible for to output a char array
2 - make this entire thing into a file to be included in another .py file
3 - the function must accept the resizing divider and the name of the file as parameters
DONE! 4 - make another function that is able to print this to a .txt

current version: 0.1
date: 31/01/2023
'''

imageMap = ("   ", " . ", ". .", "...", ".:.", ":.:", ":::", ":|:", "|:|", "|||", "|#|", "#|#", "###", "#$#", "$#$", "$$$")#map for converting and image to asci. Add as much as you need
tryAgain = True

while(tryAgain):
    imgFile = input("\nEnter the image file name with the extension. (.jpg, .jpeg, .png, etc): ")
    try:
        img = Image.open(imgFile)
        print("Image loaded successfully.")
        print("Image dimensions: " + str(img.size))#print the tuple that holds the dimentions of the object
        #print(img.format)#print the format
        print(img.format_description)#print the discription of the format ex: JPEG (ISO 10918)
        askAgain = True
        while(askAgain):
            try:
                downSizer = int(input("We need to downsize the image. Type the Amount: "))
                img = img.resize(tuple(int(t/downSizer) for t in img.size))
                img = img.convert("L")
                img = ImageOps.invert(img)
                askAgain = False
            except:
                print("Sorry, invalid value typed. Please try again.")
                askAgain = True

        askAgain = True
        while(askAgain):
            try:
                fileName = input("Give the text output file a name : ") + ".txt"
                TextFile = open(fileName, 'w')
                print("File openned successfully.")
                askAgain = False
            except:
                print("Unable to name a file with: '" + fileName + "'. Please again.")
                askAgain = True

        print(imgFile + " was downscaled to: " + str(img.size) + "\n")



        singlePixel = img.load() # we load the BIT object into Pixel, making it a PixelAccess object

        for i in range(img.size[1]):# here we generate the image out of chars
            for j in range(img.size[0]):
                TextFile.write(imageMap[int(singlePixel[j, i]/len(imageMap))])     
            TextFile.write("\n")
    
        TextFile.close()
        
        print("Conversion is done.")
        tryAgain = False
        #BIT.show()
    except:
        print("Sorry, no file named " + imgFile + " was found.")
        print("\nPlease try again.")
        tryAgain = True




