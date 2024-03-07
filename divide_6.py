from PIL import Image
import cv2
import numpy as np


def divide_image_vertical(image_path):
    # Open the image
    img = Image.open(image_path)

    # Get the size of the image
    width, height = img.size

    # Calculate the width of each section
    section_width = width // 6

    # Iterate through each section and save it as a new image
    for i in range(6):
        left = i * section_width
        right = (i + 1) * section_width
        section = img.crop((left, 0, right, height))

        # Save or display the section
        section.save(f'screenshot\captcha_attempt\section\section_{i + 1}.png')  # Save with a unique filename
        #section.show()

# Example usage
#image_path = 'D:\Project\EtenderLoad\screenshot\captcha_attempt\captcha_cropped.png'  # Replace with the actual filename of your image
#divide_image_vertical(image_path)
