import suds
import ysApi
import os
import base64
import random
import string

if __name__ == "__main__":

    # Config File
    c = ysApi.ApiClient('../config/config.ini')

    # c = ysApi.ApiClient(None, "username",
    #                     "password",
    #                     "apikey",
    #                     "environment")

    # Generate a random string to avoid conflicts when different files have the same name
    def id_generator(size=5, chars=  string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    uia = ''

    try :
        res = c.getArchive(uia)

        # Get the file content and write it on the disk
        content = res['file']
        pathFile= 'documents/'+'arch_'+id_generator()+'_'+os.path.basename(res['fileName'])
        archFile = open(pathFile, 'w')
        archFile.write(base64.b64decode(content))

        print('Archive saved in : '+os.getcwd()+'/'+pathFile)
        print('Response from Yousign API ...')
        print(res)
    except suds.WebFault as detail:
        print(detail)
