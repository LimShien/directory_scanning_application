# directory_scanning_application
A Python based security tool that scans the directory to identify the 
known file with NIST National Software Reference Library (NSRL), and upload 
the remaining file to Virustotal for analysis through APIv3.
The application generates a report with the malicious file found on the 
directory.

# Prerequires
The application requires NIST NSRL server installed on the local machine,
and a Virustotal API key. The configuration for the server and API key can
be made at config/ folder. Alternatively, the configuration can be made by 
passing arguments such as -k (for API key), -s (for server IP) and -p (for
port number).

Other than that, the Virustotal APi module need to be installed with:
pip install vtapi3



# Running the application.
Run the dir_scan.py at main_application/ directory to launch the application.

