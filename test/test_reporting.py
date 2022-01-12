import import_func
from main_application import reporting

path_scanned="/home/kali/Downloads"
path_save="/home/kali/Downloads"
name="report_file"


#passing no parameter
#reporting.create_file() # use default value

#one parameter
#passing only the path scanned
reporting.create_file(root_path_scanned=path_scanned)
#passing only the pathto save
reporting.create_file(path_to_save=path_save)
#passing only the f_name
reporting.create_file(f_name=name)

#two parameter
#passing path scanned an#passing all parameter
reporting.create_file(root_path_scanned=path_scanned,path_to_save=path_save, f_name=name)d path to save
reporting.create_file(root_path_scanned=path_scanned,path_to_save=path_save)
#passing path scanned and file name
reporting.create_file(root_path_scanned=path_scanned, f_name=name)
#passing path to save and file aname
reporting.create_file(path_to_save=path_save, f_name=name)


#three parameters
#passing all parameter
reporting.create_file(root_path_scanned=path_scanned,path_to_save=path_save, f_name=name)
