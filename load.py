from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import bypass_cap
import pandas as pd
import os
import create_file_folder
from selenium.webdriver.chrome.options import Options
import zipfile

# Set the path to your webdriver executable (e.g., chromedriver.exe for Chrome)
webdriver_path = r"C:\Users\kaush\chromedriver-win64\chromedriver.exe"

# Create a new instance of the ChromeOptions class
chrome_options = webdriver.ChromeOptions()

# Add the path to ChromeDriver executable to the 'executable_path' option
chrome_options.add_argument(f"webdriver.chrome.driver={webdriver_path}")

# Create a new instance of the Chrome driver with ChromeOptions
driver = webdriver.Chrome(options=chrome_options)

# Navigate to Google Search
driver.get('https://mahatenders.gov.in/nicgep/app')

# Maximize the browser window
driver.maximize_window()


def button_click(button_selector):
    # Wait for the button to be clickable
    go_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector))
    )
    # Click the button
    go_button.click()

button_click("#PageLink_2")
time.sleep(2)

loc = "kadavi khore"

# Your base directory
base_directory = r'D:\Project\EtenderLoad\Tender_Data'

# Combine base directory with variable folder name
new_folder_path = os.path.join(base_directory, loc)
# Create the folder if it doesn't exist
if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)

# Set the value of the element with id "Location" to "kolhapur"
location_element = driver.find_element(By.ID, "Location")
location_element.clear()  # Clear any existing value
location_element.send_keys(loc)
max_attempts = int(5)
time.sleep(2)
#1 for login
bypass_cap.bypass_captcha(driver,2)
time.sleep(1)
button_click("#submit")
time.sleep(2)
for x in range(1,max_attempts +1):
    try:
        driver.find_element(By.ID,'submit')
        bypass_cap.bypass_captcha(driver,2)
        time.sleep(1)
        button_click("#submit")
    except:
        pass
time.sleep(2)
links1 = ["#DirectLink_0_0","#DirectLink_0_1","#DirectLink_0_2","#DirectLink_0_3","#DirectLink_0_4","#DirectLink_0_5","#DirectLink_0_6","#DirectLink_0_7","#DirectLink_0_8","#DirectLink_0_9","#DirectLink_0_10","#DirectLink_0_11","#DirectLink_0_12","#DirectLink_0_13","#DirectLink_0_14","#DirectLink_0_15","#DirectLink_0_16","#DirectLink_0_17","#DirectLink_0_18"]
links2 = ["#DirectLink_0","#DirectLink_0_0","#DirectLink_0_1","#DirectLink_0_2","#DirectLink_0_3","#DirectLink_0_4","#DirectLink_0_5","#DirectLink_0_6","#DirectLink_0_7","#DirectLink_0_8","#DirectLink_0_9","#DirectLink_0_10","#DirectLink_0_11","#DirectLink_0_12","#DirectLink_0_13","#DirectLink_0_14","#DirectLink_0_15","#DirectLink_0_16","#DirectLink_0_17","#DirectLink_0_18"]
links = ["DirectLink_0","DirectLink_0_0","DirectLink_0_1","DirectLink_0_2","DirectLink_0_3","DirectLink_0_4","DirectLink_0_5","DirectLink_0_6","DirectLink_0_7","DirectLink_0_8","DirectLink_0_9","DirectLink_0_10","DirectLink_0_11","DirectLink_0_12","DirectLink_0_13","DirectLink_0_14","DirectLink_0_15","DirectLink_0_16","DirectLink_0_17","DirectLink_0_18"]
n = 15
counter = int(0)
for x in range(n):
    # Get the headers of the table
    headers = ["S.No","e-Published Date","Closing Date","Opening Date","Title and Ref.No./Tender ID","Organisation Chain"]
    header_excel = ["S.No","e-Published Date","Closing Date","Opening Date","Title and Ref.No./Tender ID","Organisation Chain","Link"]
    # Wait for the table to be present on the page
    # Locate the table on the webpage
    table_xpath = "//table[@id='table']" 
    table = driver.find_element(By.XPATH, table_xpath)
    # need to develop below code
    # Get the rows of the table
    rows = []
    count = int(0)
    string_list = []
    #print(table.find_elements(By.TAG_NAME, "tr"))
    for row in table.find_elements(By.TAG_NAME, "tr"):   
        #print(js_code_link_fetch)
        try:
            js_code_link_fetch = f'''return document.getElementById("{links[count]}").getAttribute("href");'''
            link_value = driver.execute_script(js_code_link_fetch)
            link_value = 'https://mahatenders.gov.in/' + link_value
            string_list.append(link_value)   
        except:
            pass 
        count += 1
        row_data = [cell.text for cell in row.find_elements(By.TAG_NAME, "td")]
        #href_value = row.find_elements(By.TAG_NAME, "td")[4].find_element(By.TAG_NAME, "a").get_attribute("href")
        #row_data.append(href_value)
        rows.append(row_data)

    df_links = pd.DataFrame(string_list, columns=['Links'])
    #print(df_links)

    df = pd.DataFrame(rows[1:-1], columns=headers)    
    df_final = pd.concat([df, df_links], axis=1)
        #print(df_final)
    # Save the DataFrame to an Excel file
    excel_filename = loc + ".xlsx"



    #end of download code
    # Load the existing Excel file
# Try to read the existing Excel file
    
    try:
        existing_df = pd.read_excel(excel_filename)
    except FileNotFoundError:
        # If the file doesn't exist, create a new one with the existing DataFrame
        df_final.to_excel(excel_filename, index=False,header=header_excel)
    else:
        # Append the existing DataFrame to the existing sheet (you can specify sheet_name if needed)
        with pd.ExcelWriter(excel_filename, engine='openpyxl', mode='a',if_sheet_exists='overlay') as writer:
         df_final.to_excel(writer, index=False, header=False, startrow=len(existing_df)+1)
    
    if x == 0:
        #download all the files code
        button_click("#DirectLink_0")
        time.sleep(2)
        string_down_list = []
        button_click('#DirectLink_8')  
        time.sleep(2)
        bypass_cap.bypass_captcha(driver,2)
        time.sleep(1)
        button_click('#Submit') 
        time.sleep(2)
        for x in range(1,max_attempts +1):
            try:
                driver.find_element(By.ID,'Submit')
                bypass_cap.bypass_captcha(driver,2)
                time.sleep(1)
                button_click("#Submit")
            except:
                pass
        temp_path = create_file_folder.get_download_path(base_directory,loc,counter)
        #print(temp_path)
        # Create Chrome options
        prefs = {"download.default_directory": temp_path}
        chrome_options.add_experimental_option("prefs",prefs)

        # Assuming you already have an existing WebDriver instance called 'driver'
        # Update the Chrome options for the existing WebDriver instance
        driver.execute_cdp_cmd('Page.setDownloadBehavior', {'behavior': 'allow', 'downloadPath': temp_path})

        #7 for Zip and 0 for tender notice
        button_click('#DirectLink_7')
        button_click('#DirectLink_0')
        time.sleep(2)
        counter += 1
        button_click('#DirectLink_11')
        time.sleep(2)
  
        #print(df_down_links)
        for y in links1:
            button_click(y)
            time.sleep(2)
            #7 for Zip and 0 for tender notice
            temp_path = create_file_folder.get_download_path(base_directory,loc,counter)

            prefs = {"download.default_directory": temp_path}
            chrome_options.add_experimental_option("prefs",prefs)
            driver.execute_cdp_cmd('Page.setDownloadBehavior', {'behavior': 'allow', 'downloadPath': temp_path})

            button_click('#DirectLink_7')
            button_click('#DirectLink_0')
            time.sleep(2)
            counter += 1
            button_click('#DirectLink_11')
            time.sleep(2)
    else:
        #print(df_down_links)
        try:

            for y in links2:
                button_click(y)
                time.sleep(2)
                temp_path = create_file_folder.get_download_path(base_directory,loc,counter)
                prefs = {"download.default_directory": temp_path}
                chrome_options.add_experimental_option("prefs",prefs)
                # Use CDP to update the download path dynamically
                driver.execute_cdp_cmd('Page.setDownloadBehavior', {'behavior': 'allow', 'downloadPath': temp_path})
                #7 for Zip and 0 for tender notice
                button_click('#DirectLink_7')
                button_click('#DirectLink_0')
                time.sleep(2)
                counter += 1
                button_click('#DirectLink_11')
                time.sleep(2) 
        except:
                print("ALL the Tenders are extracted")
                break

    try:
        button_click("#linkFwd")
        time.sleep(2)
    except:
        break


def unzip_files_in_subfolders(root_path):
    # Iterate through each subfolder in the given root path
    for folder_name in os.listdir(root_path):
        folder_path = os.path.join(root_path, folder_name)

        # Check if the item in the path is a directory
        if os.path.isdir(folder_path):
            # Iterate through each file in the subfolder
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)

                # Check if the file is a zip file
                if file_name.endswith('.zip'):
                    # Create a subfolder for each zip file
                    subfolder_name = file_name.replace('.zip', '_extracted')
                    try:
                        subfolder_path = os.path.join(folder_path, subfolder_name)
                    except:
                        pass

                    # Create the subfolder if it doesn't exist
                    if not os.path.exists(subfolder_path):
                        os.makedirs(subfolder_path)
                    try:
                        # Unzip the contents of the zip file into the subfolder
                        with zipfile.ZipFile(file_path, 'r') as zip_ref:
                            zip_ref.extractall(subfolder_path)
                    except:
                        pass

    
unzip_path = 'D:/Project/EtenderLoad/Tender_Data/'+ 'kolhapur'
unzip_files_in_subfolders(unzip_path)