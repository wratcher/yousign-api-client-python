import base64
import suds
import os
import ysApi
import string
import random

if __name__ == "__main__":

    # Config File
    c = ysApi.ApiClient('../config/config.ini')

    # c = ysApi.ApiClient(None, "username",
    #                     "password",
    #                     "apikey",
    #                     "environment")

    def id_generator(size=5, chars=  string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    print "Getting Signed file(s) ..."

    try :
        # For the last signature
        last = c.getListSign(count=1)
        idDemand = last[0]['cosignatureEvent']

        res = c.getSignedFilesFromDemand(idDemand)
        file = []
        fileName =[]

        # Get files contents
        for el in res:
             file.append(el['file'])

        # Get files names
        for el in res:
             fileName.append(os.path.basename(el['fileName']))

        # Write contents associated to each file
        for el in fileName :
            pathFile= 'documents/'+id_generator()+'_'+fileName[fileName.index(el)]
            print pathFile
            signedFile = open(pathFile, 'w')
            signedFile.write(base64.b64decode(file[fileName.index(el)]))

            print 'Signed file saved in : '+os.getcwd()+'/'+pathFile
    except suds.WebFault as detail:
        print detail
