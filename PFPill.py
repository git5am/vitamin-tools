from PIL import Image

image_1_directory = input("Please enter the directory of the pill png: ")
image_2_directory = input("Please enter the directory of you pfp: ")

x_coord = int(input("Please enter the x coordinate: "))
y_coord = int(input("Please enter the y coordinate: "))

img1 = Image.open(image_1_directory)

img2 = Image.open(image_2_directory)

img1.paste(img2, (x_coord,y_coord), mask = img2)

img1.show()

# /Users/sam/Desktop/IMG_3185.png

# /Users/sam/Desktop/5am_Profile_Pic_PFP.png
