from PIL import Image
import numpy as np
import cv2

# Read Image 
img= Image.open("new.jpg")  
# Convert Image to Numpy as array 
arr = np.array(img)  
#cv2.imshow("Binary Image",arr)
#cv2.waitKey(0)
#cv2.destroyAllWindows()    
print(len(arr))
print("%d bytes" % (arr.size * arr.itemsize))

