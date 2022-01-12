import import_func
from main_application import query_nist

hash = ["59ce0baba11893f90527fc951ac69912","ba1f2511fc30423bdbb183fe33f3dd0f"]

##test the function in query_nist module

##check the connection with the NSRL server. 
#query_nist.test_server()

##create connection 
s = query_nist.connect_server()

print(query_nist.query_hashed_db(s, "ba1f2511fc30423bdbb183fe33f3dd0f"))