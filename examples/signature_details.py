import suds
import ysApi

if __name__ == "__main__":

    # Config File
    c = ysApi.ApiClient('../config/config.ini')

    # c = ysApi.ApiClient(None, "username",
    #                     "password",
    #                     "apikey",
    #                     "environment")

    # To get information about the last signature
    try:
        res = c.getListSign(count=1)
        if res == []:
            print "Signature not yet created "
        idDemand = res[0]['cosignatureEvent']
        res = c.getInfosFromSignatureDemand(idDemand)
        print " Details from the signature with the id : %d" %(idDemand)
        print res
    except suds.WebFault as detail:
        print detail

