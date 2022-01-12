import hashlib
import os

def scan_file_system(dir_to_scan=os.getcwd()):
    """
    The function scan through file system and get the MD5 hash value of each file.
    The function takes an optional arguments to specify the directory to scan, it is the current working directory by default.
    The function exclude zip files that causes error to the application, zip files exceeds the buffer memory, and will kill the application
    The function returns a dictionary pair {filename(fullpath)->MD5hashvalue} 
    """
    output={}
    file_hash = ""
    try:
        if os.path.exists(dir_to_scan):
            print("Directory OKAY!")
            print("Start scanning. " + dir_to_scan)
        else:
            print("Error: Invalid directory!")
            return None
    except:
        print("Error: Invalid Input!")
        return None

    for root, dirs, files in os.walk(dir_to_scan):
        #if there is files in the directory
        if files:
            for i in files:

                #avoid reading zip file which causes error 
                if i.endswith(".zip"):
                    continue

                file_path =  root + "/" + i

                #getting hash value of a file #code reference: https://www.kite.com/python/answers/how-to-generate-an-md5-checksum-of-a-file-in-python
                try:
                    md5_hash = hashlib.md5()
                    read_file = open(file_path, "rb")
                    content = read_file.read()
                    md5_hash.update(content)
                    file_hash = md5_hash.hexdigest()

                except:
                    print("Could not open " + file_path + ". Skipped. ")
                    continue

                #update the dictionary with the filepath (key) and MD5 hash (value)
                output.update({file_path:file_hash}) 

    print("Finished Scanning.  ")
    return output