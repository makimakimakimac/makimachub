import os
from PIL import Image

bairitsu = 4

folder_a = "C:~/~/image"
list1 = os.listdir(folder_a)
imagefile = os.path.join(folder_a, list1[i])
imagedata = Image.open(imagefile)

width, height = imagedata.size
width2 = width/bairitsu
height2 = height/bairitsu
imagedata2= imagedata.resize((int(width2),int(height2)))

newimage = folder_a + "new" + list1[i]
imagedata2.save(newimage, quality=85,optimize=True)