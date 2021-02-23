import cv2
import numpy as np
import matplotlib.pyplot as plt
 
img = cv2.imread("Image_path",1)
img_original = img.copy()
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#plt.rcParams["figure.figsize"] = (16,9)
#plt.imshow(img,cmap='gray')

img1 = cv2.GaussianBlur(img,(21,21), cv2.BORDER_DEFAULT)
#plt.rcParams["figure.figsize"] = (16,9)
#plt.imshow(img,cmap='gray')

all_circles = cv2.HoughCircles(img1,cv2.HOUGH_GRADIENT,1,120,param1=50,param2=30,minRadius=60,maxRadius=125)
all_circles_rounded = np.uint16(np.around(all_circles))

#print(all_circles_rounded)
#print(all_circles_rounded.shape)
print('I found '+str(all_circles_rounded.shape[1])+' coins')


'''draw detected circle and center and join by line'''
#count = 1
pre_center_coordinates = (0,0)
for j in all_circles_rounded[0, :]:
    for i in all_circles_rounded[0, :]:
        new_center_coordinates = (i[0],i[1])
        radius =(i[2])
        cv2.circle(img_original, new_center_coordinates, radius, (0,255,0), 5)
        cv2.circle(img_original,new_center_coordinates,5,(255,0,0),3)
        #cv2.putText(img_original,'coin'+str(count),(i[0]-60,i[1]+100),cv2.FONT_HERSHEY_SIMPLEX,1.4,(255,0,0),2)
        img = cv2.line(img_original,(j[0],j[1]),new_center_coordinates,(200,200,50),5)
        #count+= 1

plt.rcParams["figure.figsize"] = (10,9)
plt.imshow(img_original)
