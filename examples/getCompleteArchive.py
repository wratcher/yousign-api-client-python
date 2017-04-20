import suds
import ysApi
import os
import base64

if __name__ == "__main__":

    # Config File
    c = ysApi.ApiClient('../config/config.ini')

    # c = ysApi.ApiClient(None, "username",
    #                     "password",
    #                     "apikey",
    #                     "environment")

    uia = ''
    
    try :
        res = c.getCompleteArchive(uia)
        zipContent = res['file']


        pathZip= 'documents/'+os.path.basename(res['fileName'])
        archFile = open(pathZip, 'w')
        archFile.write(base64.b64decode(zipContent))

        print('Archive saved in : '+os.getcwd()+'/'+pathZip)
        print('Response from Yousign API ...')
        print(res)
    except suds.WebFault as detail:
        print(detail)
