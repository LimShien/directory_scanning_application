"""
The menu module can be tested in with the command line.

1:main menu -> test -d (directory) 

    #invalid directory
    python3 dir_scan.py -d aaaaa

    #priveleged directory
    python3 dir_scan.py -d /root

    #empty directory
    python3 dir_scan.py -d /home/kali/Documents/

    #valid directory:
    python3 dir_scan.py -d /home/kali/Downloads

2: API key: 

    #to test the api key option, the configuration of API key in config is removed for the test cases
    
    #No api key provided - > Error
    python3 dir_scan.py -d /home/kali/Downloads

    #random string for api key -> ERror: invalid API key
    python3 dir_scan.py -d /home/kali/Downloads -k abc

    #configuring the api key in config/   -> success operation
    python3 dir_scan.py -d /home/kali/Downloads 

3: NIST SERVER:
    #without specifying server ip (configured in config folder)

    #invalid server ip trigger connection timeout
    python3 dir_scan.py -d /home/kali/Documents -s 111 

    #invalid port number trigger error
    python3 dir_scan.py -d /home/kali/Documents -s 127.0.0.1 -p 0023

4:
    output:

    #invalid directory for output the report -> trigger error
    python3 dir_scan.py -d /home/kali/Downloads -oD /rr/kali/home

    #permission to write
    python3 dir_scan.py -d /home/kali/Downloads -oD /root 





"""