import import_func
from main_application import scan_filesystem

#test scan file system with several cases


#no parameter passed
print(scan_filesystem.scan_file_system()) # scan the current directory as the default


#pass valid directory
print(scan_filesystem.scan_file_system("/home/kali/Downloads")) #scan the specified dir 

#pass invalid directory
print(scan_filesystem.scan_file_system("/home/kali/randomfir")) #prompt invalid input dir

#pass random string
print(scan_filesystem.scan_file_system("randomstring")) ##prompt invalid input dir

#pass integer
print(scan_filesystem.scan_file_system(123))#prompt invalid input dir

#pass list
print(scan_filesystem.scan_file_system(["asd","asd"])) ##prompt invalid input dir
