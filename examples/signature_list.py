import suds
import ysApi

if __name__ == "__main__":

    # Config File
    c = ysApi.ApiClient('../config/config.ini')

    # c = ysApi.ApiClient(None, "username",
    #                     "password",
    #                     "apikey",
    #                     "environment")


    print "Getting List ... "

    # The last ten signatures for this example
    try:
        res = c.getListSign('', 0, count = 10)
        print res
    except suds.WebFault as detail:
        print detail