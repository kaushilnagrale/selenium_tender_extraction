from PIL import Image
import cv2
import numpy as np

import pytesseract

# Specify the Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with your Tesseract path

def image_to_text(image_path):
    res = ''

    for x in range(1,7):
        temp = image_path + str(x) + '.png' 
        # Read the image using OpenCV
        original_image = cv2.imread(temp)

        # Convert the image to grayscale
        grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

        # Apply a median filter to remove small dots
        filtered_image = cv2.medianBlur(grayscale_image, 3)  # Adjust the kernel size as needed

        # Display the inverted image (optional)
        #cv2.imshow("Inverted Image", filtered_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite(temp,filtered_image)

        # Use pytesseract to perform OCR on the image
        text = pytesseract.image_to_string(temp,  config='--psm 6 --oem 3')
        text= text.strip()
        text = text[0].upper()
        if text == ')':
            text = 'D'
        res += text
    return res


#image_path = 'D:\Project\EtenderLoad\screenshot\captcha_attempt\section\section_'
#result = image_to_text(image_path)