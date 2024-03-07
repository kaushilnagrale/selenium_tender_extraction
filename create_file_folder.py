import os
import pandas as pd


# Your base directory
#base_directory = r'D:\Project\EtenderLoad\Tender_Data'
#loc = "kolhapur"

def get_download_path(bd,loc,sl_no):
    # Combine base directory with variable folder name
    folder_path = os.path.join(bd, loc)
    # Path to the Excel file
    excel_file_path = 'D:/Project/EtenderLoad/'+ loc + '.xlsx'
    # Load the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file_path)
    # Select the cell in the 5th column (column index 4) and 2nd row (row index 1)
    selected_value = df.iloc[int(sl_no), 4]
    selected_value = str(int(sl_no)+1) + '_Sl_no_' + selected_value[:150]
    selected_value = selected_value.replace("\\", "_").replace("/", "_").replace(".", "_").strip()
    sub_folder_path = os.path.join(folder_path, selected_value)
    # Create the folder if it doesn't exist
    if not os.path.exists(sub_folder_path):
        os.makedirs(sub_folder_path)
    download_path = sub_folder_path
    return download_path


