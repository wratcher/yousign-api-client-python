# Python Client for Yousign API

## Description

This client allows to use the Yousign Soap API through Python.

## Install
You need to have a version of Python (2.6 or 2.7) running on your device, in order to execute the following programs.

+ Clone this repository:  
    * git clone https://github.com/rapha777/yousign-api-client-python
+ Cd into **yousign-api-client-python** and execute:  
    * python setup.py install

## Configuration
You can edit the file **'~/config/config.ini'** in order to enter your settings.  
Then set your configuration with these parameters:

    * login : Your login (email address)
    * password : Your password
    * apikey : Your API Key 
    * environment : demo or prod
    * isEncryptedPassword : true if you use an encrypted password, false if not.    
You need to hash your password. 
Here is the hash calculation : sha1(sha1(clearPassword)+sha1(clearPassword)).  
This calcul is done to secure your password.   
If clearPassword = "test123", password ="6bc498d4dc47ec2177ff42151139da01c1660ddf".

## Examples
You can find some examples about the way the client works in **~/examples**.
First, run the file **connection.py** to verify your access.  
Here, you can also set your user parameters in each Python file.  
First, comment the line **c = ysApi.ApiClient('../config/config.ini')**.  
Then, uncomment these one and put your user information.  

     * c = ysApi.ApiClient(None, username,  
                       password, => (encrypted),  
                       apikey, 
                       environment 
For other examples, Modify information in each of these Python, then you can run these following programs.
  
     * signature_init : Initialize a signature process.
     * signature_downloadFile : Get signed files associated with a signature process from an idDemand or a token.
     * signature_details : Get information (status, name, file info) about a signature process from an idDemand or a token.
     * signature_list : Get information of all your signature processes.
     * signature_alert : Alert signers who have not signed document(s) yet.
     * signature_cancel : Cancel a signature process which is not finished yet.
     * archive : Archive document for 10 years with metadatas. Metadatas are used to find easily one (or several) archive.
     * getArchive : Get archive file identified by its iua
     * getCompleteArchive : Get complete archive file identified by its iua.
