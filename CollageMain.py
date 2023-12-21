import cv2
import numpy as np
import glob
import csv
import Collage

#collecting images
listing = glob.glob('*.jpg')

#storing grid points
with open('GridPoints.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

data_array = np.array(data, dtype=int)

#blank canvas
canvas = np.zeros((400, 400, 3), dtype=np.uint8)

#now making the collage
for i in range(len(listing)):
    src = cv2.imread(listing[i])
    cornerY = data_array[i, 0]
    cornerX = data_array[i, 1]
    projHeight = data_array[i, 2]
    projWidth = data_array[i, 3]

    Collage.projectImageonCanvas(src, canvas, cornerY, cornerX, projHeight, projWidth)

cv2.imshow('result', canvas)
cv2.waitKey()

cv2.imwrite('C:\\Users\\Prady\\PycharmProjects\\MakeCollage\\CollageResult\\Collage.jpg', canvas)
