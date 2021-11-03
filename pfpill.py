from PIL import Image
# defines the images
image_1_directory = input("Please enter the directory of the pill png: ")
image_2_directory = input("Please enter the directory of you pfp: ")
# decalres resizes of pfp
resize_x = int(input("Please enter the desired new x value: "))
resize_y = int(input("Please enter the desired new y value: "))
size = (resize_x, resize_y)
# defines x & y coords
x_coord = int(input("Please enter the x coordinate: "))
y_coord = int(input("Please enter the y coordinate: "))
# opens the images
img1 = Image.open(image_1_directory)
img2 = Image.open(image_2_directory)
# resizes the pfp
img2_resize = img2.resize(size)
# pastes them together
img1.paste(img2_resize, (x_coord,y_coord), mask = img2_resize)
# displays the end result
img1.show()
