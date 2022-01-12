import import_func
import argparse
import main_application.virustotal_api as virustotal_api
import config.vt_api_key as vt_api_key
import os
from main_application import query_nist
from config import nist_server_configuration



def create_menu():
    """
    The function utilize the argparse module to create a menu with option for the application.
    """
    #create argument parser object 
    ap = argparse.ArgumentParser()

    #add arguments
    ap.add_argument('-d', '--directory' , help="Specify the directory to scan. Default: current directory. ", action="store")
    conf = ap.add_argument_group('Configuration', "Optional if configured.")
    conf.add_argument('-k', '--apikey' , help="Specify the VirusTotal ApiKey. Required if not configured. ", action="store")
    conf.add_argument('-s', '--server' , help="Specify the NIST NSRL server ip. Local Server: 127.0.0.1 .  Required if not configured. ", action="store")
    conf.add_argument('-p', '--port' , help="Specify the NIST NSRL server port number. Default: 9120. Required if not configured. ", action="store")
    out = ap.add_argument_group('Report output', "Optional:")
    out.add_argument('-oF', '--output_file' , help="Specify the report file name. Default: dir_report", action="store")
    out.add_argument('-oD', '--output_dir' , help="Specify the directory of the report. Default: current directory", action="store")

    args = ap.parse_args(["-s", "127.0.0.1"])

    return args

def test_parameter(args):
    """
    The function execute checks the parameter passed by the user and the configuration for server and externalAPI.
    """

    #change the value of server based on input by the user 
    if args.server and args.port:
        nist_server_configuration.nsrl_server = args.server
        nist_server_configuration.nsrl_port = args.port
    elif args.server and not args.port:
        nist_server_configuration.nsrl_server = args.server
    elif args.port and not args.server:
        nist_server_configuration.nsrl_port = args.port

    #test the server connection with socket
    if query_nist.test_server() == True:
        print("Connection to NIST NSRL server okay.")
    else:
        print("Error: Check NSRL Server IP or port number. ")

        return None

    #Check Virustotal API KEY
    if args.apikey: 
        #check the API key provided by user
        if virustotal_api.test_api_key(args.apikey):
            vt_api_key.api_key = args.apikey
            print("Virustotal API Key Valid. ")
        else:
            print("Error: Invalid API Key. ")
            return None
    else:
        #check the API key in the configuration if no API key provided 
        if virustotal_api.test_api_key(vt_api_key.api_key) == False:
            print("Error: Please provide Virustotal API Key with -k or --apikey options.\nAlternatively, configure the API key in vt_api_key.py ")
            return None
        else:
            print("API Key Valid. ")

    #Check Directory for scanning
    if args.directory:
        #check if the directory for scanning is valid/exist
        if os.path.exists(args.directory) == False:
            print("Error: Invalid Directory for scanning.")
            return None
        #no permission to access i.e. root folder
        if os.access(args.directory, os.R_OK) == False:
            print("Error: Directory require root permission ")
            return None
        #no file in the directory / empty directory
        if not os.listdir(args.directory):
            print("Warning: Directory is empty. No file to scan.\nEnd of operation.")
            return None

    #Check Directory for saving report output
    if args.output_dir:
        #check if the directory for saving report is valid/exist
        if os.path.exists(args.output_dir) == False:
            print("Error: Invalid Directory for saving the report.")
            return None
       #no permission to access i.e. root folder
        if os.access(args.output_dir, os.R_OK) == False:
            print("Error: Directory require root permission ")
            return None

    return True
