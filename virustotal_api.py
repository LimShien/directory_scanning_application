from vtapi3 import VirusTotalAPIError, VirusTotalAPIFiles
import config.vt_api_key as vt_api_key 
import json  
import requests


def test_api_key(apikey):
    """
    The function test the validity of API key provided by user.
    The function takes in a api key (String), to test if the key is valid.
    if valid, it returns a virustotal connection instance.
    code refrence from Virustotal API  https://developers.virustotal.com/reference/file-info
    """
    url = "https://www.virustotal.com/api/v3/files/7adf6a2d681b41c0e18a8affc3c765c7"

    headers = {
        "Accept": "application/json",
        "x-apikey": apikey
    }

    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        return True
    else:
        return False

def create_instance():
    """
    A function to create a virus total instance, with a verified API key.
    the function returns a VirusTotal connection instance
    """
    #create virustotal object with apikey
    return VirusTotalAPIFiles(vt_api_key.api_key)

def vt_upload(vt, file_path):
    """
    A function that uploads a file to VirusTotal for analysis.
    The function takes in the virustotal API instance created using API key, and a filepath (String) for the upload file.
    The code referenced from VirusTotal API official documentation.
    """
    #upload and analyse file - virustotal
    try:
        respond = vt.upload(file_path)

    #catch and display exception
    except VirusTotalAPIError as err:
        print(err, err.err_code)

    else:
        #check the HTTP status code for last operation 
        if vt.get_last_http_error() == vt.HTTP_OK:

            #serialize to json formated string
            respond = json.loads(respond)
            respond = json.dumps(respond, sort_keys=False, indent=4)

        else:
            #print error
            print("HTTP Error [ " + str(vt.get_last_http_error()) + " ]")

def get_information(vt, file_hash):
    """
    The function query Virustotal with API to retrieve information regarding the scanned file.
    It format the response in JSON format, and parse the response to retrieve some basic information about the scanned file.
    The function takes a Virustotal instance as parameter, and a filehash (String).
    The function returns a LIST which contains some information about the mallicious one.
    code from line 38 to line 45 is referenced from the VirusTotal Api documentation 

    """
    try:
        result = vt.get_report(file_hash) 
        
    except VirusTotalAPIError as err:
        print(err, err.err_code) 
    else:
        if vt.get_last_http_error() == vt.HTTP_OK:
            result = json.loads(result)
            
            #type of the file 
            f_type = result["data"]["attributes"]["type_description"]
            #magic
            f_magic = result["data"]["attributes"]["magic"]
            #reputation
            f_rep = result["data"]["attributes"]["reputation"] 
            #link 
            f_link = result["data"]["links"]["self"]
            #sha-1
            f_sha = result["data"]["attributes"]["sha1"]
            
            #an array that hold information about the engine that detected mallicious
            engine_info= []
            print("Querying Viruatotal for : " + file_hash)
            for i in result["data"]["attributes"]["last_analysis_results"]:
                ##print(i + "\t\t" + result["data"]["attributes"]["last_analysis_results"][i]["category"])
                #if the result is mallicious
                if result["data"]["attributes"]["last_analysis_results"][i]["category"] == "malicious":
                    
                   #retrieve some basic information if the file is mallicious
                    engine = result["data"]["attributes"]["last_analysis_results"][i]["engine_name"]
                    version = result["data"]["attributes"]["last_analysis_results"][i]["engine_version"]
                    update = result["data"]["attributes"]["last_analysis_results"][i]["engine_update"]

                    #check if r value is null, if not get the value
                    if result["data"]["attributes"]["last_analysis_results"][i]["result"]:
                        r = result["data"]["attributes"]["last_analysis_results"][i]["result"]

                    else: 
                        r = ""
                    
                    engine_info.append([engine, version, r, update])

            return [[file_hash, f_sha ,f_type, f_magic, f_rep, f_link ],engine_info]

        else:
            print('HTTP Error [' + str(vt.get_last_http_error()) +']')

