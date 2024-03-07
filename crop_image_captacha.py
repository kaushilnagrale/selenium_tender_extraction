from PIL import Image
import cv2
import numpy as np

def crop_and_save(input_image_path, output_image_path, coordinates):
    # Open the image file
    original_image = Image.open(input_image_path)

    # Crop the image using coordinates (left, top, right, bottom)
    cropped_image = original_image.crop(coordinates)

    # Save the cropped image
    cropped_image.save(output_image_path)
    
    # Open the screenshot using Pillow (PIL)
    #img = Image.open(output_image_path)
    #img.show()  # Opens the screenshot using the default image viewer

# Example usage
input_image_path = "D:\Project\EtenderLoad\screenshot\Screenshot 2024-02-22 195049.png"  # Replace with your input image path
output_image_path = "D:\Project\EtenderLoad\output_image.jpg"  # Replace with your desired output image path
crop_coordinates = (1300, 810, 1485, 860)  # Example coordinates (left, top, right, bottom)

#crop_and_save(input_image_path, output_image_path, crop_coordinates)

from PIL import Image
import pytesseract

# Specify the Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with your Tesseract path


def image_to_text(image_path):

    # Read the image using OpenCV
    original_image = cv2.imread(image_path)

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)


    # Apply adaptive thresholding to create a binary image
    _, binary_image = cv2.threshold(grayscale_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Invert the binary image to have text in black on a white background
    inverted_image = cv2.bitwise_not(binary_image)

    # Display the inverted image (optional)
    cv2.imshow("Inverted Image", inverted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    cv2.imwrite(output_image_path,inverted_image)



    # Use pytesseract to perform OCR on the image
    text = pytesseract.image_to_string(output_image_path,  config='--psm 6 --oem 3')

    return text

def process_individual_characters(image):
    # Find contours in the image
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through each contour
    for contour in contours:
        # Get bounding box coordinates
        x, y, w, h = cv2.boundingRect(contour)

        # Extract individual character from the image
        char_image = image[y:y+h, x:x+w]

        # Perform OCR on the individual character
        char_text = pytesseract.image_to_string(char_image)

        # Print the OCR result for each character
        print("Extracted Character:", char_text)

        # Draw bounding box around the character (optional)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display the image with bounding boxes (optional)
    cv2.imshow("Image with Bounding Boxes", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

extracted_text = image_to_text(output_image_path)
print("Extracted Text:")
print(extracted_text)
#process_individual_characters(image_to_text(output_image_path))