# Get file names
# rename each file 

import os
def rename_files():
    file_list = os.listdir("path of folder")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir("path of folder")
    for file_name in file_list:
        os.rename(file_name, file_name.translate (None, "0123456789"))
rename_files()


    
