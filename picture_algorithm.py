import cv2
import numpy as np

# How many lines do we want to identify
number_of_lines = 3
# Opening the image that is going to be analyzed
img_original = cv2.imread('line2.PNG')
resized_image = cv2.resize(img_original, (1000, 800))

# Creating a Grey-scale version of the original image
img_greyscale = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Convolving the Grey-scale image with a kernel of 2 by 20px.
kernel = np.matrix([[1, 0, -1]])
img_lines = cv2.filter2D(img_greyscale, -1, kernel)

vertical_structure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 20))
img_line1 = cv2.erode(img_lines, vertical_structure, iterations=2)
img_lin2 = cv2.dilate(img_line1, vertical_structure, iterations=2)

(thresh, im_bw) = cv2.threshold(img_lin2, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
lines = cv2.HoughLinesP(im_bw, rho=1, theta=np.pi / 180, threshold=1, minLineLength=10, maxLineGap=200)

chunks = [[[[293, 788, 310, 569]]],
          [[[293, 788, 293, 569]]]]

x_sum = [0, 0, 0]
x = 0
try:
    for lines in chunks:
        for line in lines:
            print line
            for x1, y1, x2, y2 in line:
                x_sum[x] = x_sum[x] + x1
                cv2.line(resized_image, (x1, 800), (x2, 0), (0, 0, 255), 1)

        # Drawing line and rectangle
        x_average = x_sum[x] / len(chunks[x])

        x = x + 1
except TypeError:
    pass


cv2.imshow('Example of Power Lines', resized_image)
cv2.imshow('Binary Image', im_bw)
cv2.waitKey(0)
cv2.destroyAllWindows()
