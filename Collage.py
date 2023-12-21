import cv2
import numpy as np

def projectImageonCanvas(src, canvas, cornerY, cornerX, projHeight, projWidth):

    botX = cornerX + projWidth
    botY = cornerY + projHeight

    if botX > canvas.shape[1]:
        botX = canvas.shape[1]

    if botY > canvas.shape[0]:
        botY = canvas.shape[0]

    pts1 = np.float32([[0, 0], [src.shape[1], 0],
                       [0, src.shape[0]], [src.shape[1], src.shape[0]]])

    pts2 = np.float32([[cornerX, cornerY], [botX, cornerY],
                       [cornerX, botY], [botX, botY]])

    #computing perspective transform and applying it to the src image
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(src, matrix, (canvas.shape[0], canvas.shape[1]))

    #applying warped image to canvas
    for row in range(cornerY, botY):
        for col in range(cornerX, botX):
            for z in range(3):
                canvas[row, col, z] = result[row, col, z]

