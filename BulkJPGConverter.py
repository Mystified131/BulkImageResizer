
from PIL import Image
import os

for subdir, dirs, files in os.walk("C:\\Users\\mysti\\Coding\\BulkImageResizer\\static\\"):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".png")) :
            im = Image.open(filepath)
            rgb_im = im.convert('RGB')
            file2 = 'CONV' + file[:-4] + ".jpg"
            filepath2 = subdir + os.sep + file2
            rgb_im.save(filepath2)
            
