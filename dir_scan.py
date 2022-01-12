#/bin/python3
from requests.api import get
import menu
from scan_filesystem import scan_file_system
from query_nist import connect_server, close_connection, query_hashed_db, filter_dataset
from virustotal_api import create_instance, vt_upload, get_information
from reporting import create_file, append_to_report, close_file

#create menu, test parameter and configuration 
instance = menu.create_menu()

if menu.test_parameter(instance):

    ####start with scanning the file system 

    #if the directory to scan is specified, pass the value to the function
    
    if instance.directory:
        file_hash_pair  = scan_file_system(dir_to_scan=instance.directory)
    
    else:
        #use the default value for directoy, which is the current working directory
        file_hash_pair  = scan_file_system()
    
    ####query the NIST NSRL database with the dictionary of file:hash pair as arguments

    #initiate connection to the server
    server_instance = connect_server()

    #query database with list of hasheh, retrieved from the file_hash_pair dictionary
    query_result = query_hashed_db(server_instance, file_hash_pair.values())

    #close connection
    close_connection(server_instance)

    #filter dataset -> to remove the data that are found in NSRL database
    file_hash_pair = filter_dataset(file_hash_pair, query_result)

    ####upload the updated dictionary set (the files) to Virustotal for analysis

    #create virustotal API connection instance
    vt_instance = create_instance()

    #create file instance 
    if instance.directory:  #only directory scanned is presence
        file_instance = create_file(root_path_scanned = instance.directory)

        if instance.output_dir: #directory scanned and directory to save
            file_instance = create_file(root_path_scanned = instance.directory, path_to_save=instance.output_dir)

            if instance.output_file: #three optional arguments are presence              
                file_instance = create_file(root_path_scanned = instance.directory, path_to_save=instance.output_dir, f_name= instance.output_file )
        
        elif instance.output_file: #only directory scanned and file name to save are presence
            file_instance = create_file(root_path_scanned = instance.directory, f_name= instance.output_file )
        
    elif instance.output_dir: #directory to save
        file_instance = create_file(path_to_save=instance.output_dir)
        
        if instance.output_file: #directory to save and file name to save are presence
            file_instance = create_file(f_name= instance.output_file )
    
    elif instance.output_file: #only file name to save are presence
        file_instance = create_file(f_name= instance.output_file )
    
    else: # no optional arguments is passed 
        file_instance = create_file()
        

    #iterate through the file:hash pair to submit to virustol, retrieve information and write to report
    for i in file_hash_pair:
        #full_path = i,#hash = file_hash_pair[i]

        #upload the file for analysis
        vt_upload(vt_instance,i)

        #retrieve information of the file
        m_file_info = get_information(vt_instance, file_hash_pair[i])

        #write result to the file
        if m_file_info:
            print("Writting data to report. ")
            append_to_report(file_instance, i , m_file_info )

    close_file(file_instance)
    
else:
    print("Error.")