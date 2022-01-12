from os import closerange
import import_func
from main_application import virustotal_api
from config import vt_api_key

#
#return a True if successful
print(virustotal_api.test_api_key(vt_api_key.api_key))

#return False for invalid API KEY
print(virustotal_api.test_api_key("abcdefg12345"))
print(virustotal_api.test_api_key(["Asd","asd"]))

#create instance
vt = virustotal_api.create_instance()

#non malicious file
nm_file_path = "/home/kali/Downloads/text"
nm_file_hash = "ba1f2511fc30423bdbb183fe33f3dd0f"
#malicious file
m_file_path = "/home/kali/Downloads/bin.sh"
m_file_hash = "59ce0baba11893f90527fc951ac69912"
hash = "be310a7d1c64742349a6bdc4f2a672af"

##test vt upload 
virustotal_api.vt_upload(vt, nm_file_path) #success
virustotal_api.vt_upload(vt, m_file_path)  #success
virustotal_api.vt_upload(vt, "/home/kali/aa") #Failed -> file not found


print(virustotal_api.get_information(vt, nm_file_hash))
print(virustotal_api.get_information(vt, m_file_hash))
print(virustotal_api.get_information(vt, "abc")) #error
