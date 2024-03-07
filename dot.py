import cv2
import numpy as np

# Load the image
image = cv2.imread('D:\Project\EtenderLoad\screenshot\Captcha\done\img_2.png')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a median filter to remove small dots
filtered_image = cv2.medianBlur(gray, 3)  # Adjust the kernel size as needed

# Save the result or display it
cv2.imwrite('output_image.jpg', filtered_image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()