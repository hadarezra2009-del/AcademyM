import os

path=r"C:\ממריאות"
def scan_directory(path):
    
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        
       
        if os.path.isfile(full_path):
            print("file:", item)
        
        
        elif os.path.isdir(full_path):
            print("dir", item)
            scan_directory(full_path)

scan_directory(path)