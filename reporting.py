import os
from datetime import datetime

def create_file(root_path_scanned=os.getcwd(), path_to_save=os.getcwd(), f_name="dir_report"):
    """
    The function check if the directory has the file , by default, it is named "dir_report".
    if the file already exist, the file will be saved as filename(n), where n > 0.

    The optional parameters are:
    -the path scanned, if not specified, it is the curretn directory
    -the path to save the file, by default, it is the current directory of the application.
    -the file name to be saved as, by default, dir_report or dir_report(n)
    """
    #checks if the filename exist
    is_f_exist = os.path.exists(os.getcwd() + "/" + f_name)

    #append the n value of file copy
    i = 1 
    while is_f_exist:
        f_name = "dir_report(" + str(i) +")"
        is_f_exist = os.path.exists(os.getcwd() + "/" + f_name)
        i +=1 
    
    try:
        #create a new file with the latest n value and add tile, scanned date, and scanned directory.
        f = open(f_name, "a+")

        f.write("File System Scanning Report \n\n")
        f.write("Scanned Date: " +  datetime.today().strftime('%Y-%m-%d-%H:%M:%S') + "\n")
        f.write("Scanned directory: " + root_path_scanned + "\n\n")
        print(f_name + " created successfully. ")
    except:
        print("Report file failed to create. ")

    return f 

def append_to_report(file_object, file ,data):
    """
    The function takes in a file instance,  and writes data to the file. 
    the arguments that the function takes are the file instance, the file directory that has scanned and a list of data
    """

    file_object.write("\nMalicious file (full path):\t"  + file)
    file_object.write("\nFile hash (MD5):\t" + data[0][0])
    file_object.write("\nFile hash (SHA1):\t" + data[0][1])
    file_object.write("\nFile type:\t" + data[0][2])
    file_object.write("\nFile identifier (magic):\t" + data[0][3])
    file_object.write("\nReputation:\t" + str(data[0][4]))
    file_object.write("\nDetails available at:\t" + data[0][5])
    file_object.write("\n\nVirusTotal Engine That Detected Malicious: ")
    for i in data[1]:
        file_object.write("\n\tEngine Name:\t" + i[0])
        file_object.write("\n\tEngine Version:\t" + i[1])
        file_object.write("\n\tResult:\t" + i[2])
        file_object.write("\n\tEngine Update:\t" + str(i[3])[:4]+"-"+str(i[3])[4:6]+"-"+ str(i[3])[6:8]) #format string to date 
        file_object.write("\n")

    file_object.write("\n\n")
def close_file(file_object):
    """
    the function closes the file object 
    """
    print("Closing Report. ")
    file_object.close()