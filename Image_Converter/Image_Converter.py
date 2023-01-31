from PIL import Image
'''
This simple program converts an image to an image made of ascii characters.
This version is very crude. Some refacturing must be done

TO DO:

1 - make it possible for to output a char array
2 - make this entire thing into a file to be included in another .py file
3 - the function must accept the resizing divider and the name of the file as parameters
4 - make another function that is able to print this to a .txt

current version: 0.1
date: 31/01/2023
'''

imageMap = ("   ", " . ", ". .", "...", ".:.", ":.:", ":::", ":|:", "|:|", "|||", "|#|", "#|#", "###", "#$#", "$#$", "$$$")#map for converting and image to asci. Add as much as you need
tryAgain = True

''' Create an object called porn1 and assign all the caracteristics of the real porn file "porn1.jpg" '''
while(tryAgain):
    imgFile = input("\nEnter the image file name with the extension. (.jpg, .jpeg, .png, etc): ")
    try:
        img = Image.open(imgFile)
        print("Image loaded successfully.")
        print("Image dimensions: " + str(img.size))#print the tuple that holds the dimentions of the object
        #print(img.format)#print the format
        print(img.format_description)#print the discription of the format ex: JPEG (ISO 10918)
        tryScalingAgain = True
        while(tryScalingAgain):
            try:
                downSizer = int(input("We need to downsize the image. Type the Amount: "))
                BIT = img.resize(tuple(int(t/downSizer) for t in img.size))
                BIT = BIT.convert("L")
                tryScalingAgain = False
            except:
                print("Sorry, invalid value typed. Please try again.")
                tryScalingAgain = True

        print(BIT.size)


        singlePixel = BIT.load() # we load the porn1 object into Pixel, making it a PixelAccess object

        for i in range(BIT.size[1]):# here we generate the image out of chars
            for j in range(BIT.size[0]):
                print(imageMap[int(singlePixel[j, i]/len(imageMap))], end = '')     
            print()
        
        print("Conversion is done.")
        tryAgain = False
        #BIT.show()
    except:
        print("Sorry, no file named " + imgFile + " was found.")
        print("\nPlease try again.")
        tryAgain = True




