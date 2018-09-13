import cv2
import numpy as np

cap = cv2.VideoCapture('video3.mp4')

while 1:
    _, resized_image = cap.read()
    # Opening the image that is going to be analyzed
    # img_original = cv2.imread('test.jpg')
    # resized_image = cv2.resize(img_original, (1000, 800))

    # Creating a Grey-scale version of the original image
    img_greyscale = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    # Convolving the Grey-scale image with a kernel of 2 by 20px.
    kernel = np.matrix([[1, 0, -1]])
    img_lines = cv2.filter2D(img_greyscale, -1, kernel)

    vertical_structure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 20))
    img_line1 = cv2.erode(img_lines, vertical_structure, iterations=1)
    img_lin2 = cv2.dilate(img_line1, vertical_structure, iterations=1)

    (thresh, im_bw) = cv2.threshold(img_lin2, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    lines = cv2.HoughLinesP(im_bw, rho=1, theta=np.pi / 180, threshold=30, minLineLength=100, maxLineGap=200)
    print len(lines/4)

    try:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(resized_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    except TypeError:
        pass

    cv2.imshow('res', resized_image)
    cv2.imshow('canny', im_bw)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
