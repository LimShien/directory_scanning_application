import config.nist_server_configuration as nist_server_configuration
import socket



def connect_server():
    """
    The function uses socket to connect to the NIST NSRL server.
    It uses the configuration in nist_server_configuration.py.
    It returns a socket instance.
    """
    try:
        #make socket instance 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #conencting to NSRL server
        s.connect((nist_server_configuration.nsrl_server, nist_server_configuration.nsrl_port))
        #try ro query the database with a hash
        return s
    except:
        return False
        
 
def query_hashed_db(s, md5_hashes):
    """
    The function queries the NIST NSRL server, with a list of hash value as the input.
    the function return a string which contains series of 1 (match is found) and 0 (not found)
    """
    try:
        #code from line 35 - line 52 referenced from : https://books.google.ie/books?id=ofl_CwAAQBAJ&pg=PA23&lpg=PA23&dq=nist+nsrl+python&source=bl&ots=UgwO7iQkcT&sig=ACfU3U3RFeJ8w8-gYkvrlhxl2GRizhMVCQ&hl=en&sa=X&ved=2ahUKEwjznuLRyp_1AhVrQ0EAHdEsBdQQ6AF6BAgNEAM#v=onepage&q=nist%20nsrl%20python&f=false
        f = s.makefile('r')
        
        #version for initial handshake between client and server, the server will respond with "OK" if successful
        s.sendall("version: 2.0\r\n".encode("UTF-8"))

        #read the response
        r = f.readline()
        if r.strip() != "OK":
            raise RuntimeError("Error connecting to NSRL server. ")
        
        #construct query statement 
        query_statement = "query " + " ".join(md5_hashes) + "\r\n"

        #execute query statement
        s.sendall(query_statement.encode("UTF-8"))
        #read response
        r = f.readline()
        if r[:2] != "OK":
            raise RuntimeError("NSRL server query error.")
        
        return r
    except:
        print("Error querying database. ")
        
        
def close_connection(s):
    """
    the function closes the connection
    """
    #close socket
    s.close()

def test_server():
    """
    The function test the connection to the NIST NSRL server by running a hash query.
    It returns boolean as a result
    """
    try:
        s = connect_server()

        #testing the connection to the hashed  database using the hash value from the first entry.
        print(query_hashed_db(s, ["344428FA4BA313712E4CA9B16D089AC4"]))

        s.close()

        return True
    except:
        return False

def filter_dataset(dictionary_output, query_result):
    """
    The function filter the dataset to remove the entries that match the data in NIST database.
    The function takes two arguments:
        dictionary_output: the full dictionary containing the filename and hashes pair,
        query_result: the series of zeros and ones indicating found/not found 
    The function returns a dictionary which contain only the hashes pair that are not found in NIST database.
    """
    #remove white space and trim the query result
    query_result = query_result[3:].split()
    query_result = list(query_result[0])

    key_list = list(dictionary_output)

    #check the length of the dictionary and query result
    if len(dictionary_output) == len(query_result):

        for i in range (0, len(query_result)):
            #move the entry that  match to NIST database
            if query_result[i] == '1':
                dictionary_output.pop(key_list[i]) # remove from the dictionary

    return (dictionary_output)