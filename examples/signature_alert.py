import suds
import ysApi

if __name__ == "__main__":

    # Config File
    c = ysApi.ApiClient('../config/config.ini')

    # c = ysApi.ApiClient(None, "username",
    #                     "password",
    #                     "apikey",
    #                     "environment")


    try:
        print("Alerting the Signers ...")

        # For the last signature
        last = c.getListSign(count=1)
        idDemand = last[0]['cosignatureEvent']

        res = c.alertSigners(idDemand)
        print(res)

    except suds.WebFault as detail:
        print(detail)
