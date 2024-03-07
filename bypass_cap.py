from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import divide_6
import Recognise_letter


def bypass_captcha(driver,x):
    # Example usage
    input_image_path = 'D:\Project\EtenderLoad\screenshot\captcha_attempt\captcha.png'  # Replace with your input image path
    output_image_path = 'D:\Project\EtenderLoad\screenshot\captcha_attempt\captcha_cropped.png'



    # JavaScript code to execute and get a value
    js_code_right = '''return document.querySelector("#captchaImage").getBoundingClientRect().right;'''
    js_code_top = '''return document.querySelector("#captchaImage").getBoundingClientRect().top;'''
    js_code_bottom = '''return document.querySelector("#captchaImage").getBoundingClientRect().bottom;'''
    # Execute the JavaScript code and get the result
    result = driver.execute_script(js_code_right)
    if x == 1:
     result = result - 26

    js_codeleft = '''return document.querySelector("#captchaImage").getBoundingClientRect().left;'''
    result_left = driver.execute_script(js_codeleft)
    result_top = driver.execute_script(js_code_top)
    result_top = result_top - 8
    result_bottom = driver.execute_script(js_code_bottom)
    #985,300,350
    crop_coordinates = (float(result_left), float(result_top), float(result), float(result_bottom))  # Example coordinates (left, top, right, bottom)
    time.sleep(2)
    driver.save_screenshot(input_image_path)
    # Open the image file
    original_image = Image.open(input_image_path)
    # Crop the image using coordinates (left, top, right, bottom)
    cropped_image = original_image.crop(crop_coordinates)
    # Save the cropped image
    cropped_image.save(output_image_path)
    time.sleep(2)
    divide_6.divide_image_vertical(output_image_path)
    res = Recognise_letter.image_to_text('D:\Project\EtenderLoad\screenshot\captcha_attempt\section\section_')
    print(res)
    # JavaScript code with Python variable submitting into the button
    js_code1 = f'''document.getElementById("captchaText").value = "{res}";'''
    if x == 1:
       js_code1 = f'''document.getElementById("CaptchaText").value = "{res}";'''

    # Execute the JavaScript code
    driver.execute_script(js_code1)
    time.sleep(5)
