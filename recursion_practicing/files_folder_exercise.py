import os

def list_files(current_path):

    for file_name in os.listdir(current_path):
        if not os.path.isdir(os.path.join(current_path, file_name)):
            print(os.path.join(current_path, file_name))
        else:
            nm = os.path.join(current_path, file_name)
            list_files(nm)
    
list_files('C:/Users/Pichau/Documents/ADS2/recursion_practicing/folder1')