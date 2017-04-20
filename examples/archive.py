import suds
import ysApi
import base64

if __name__ == "__main__":

    # Config File
    c = ysApi.ApiClient('../config/config.ini')

    # c = ysApi.ApiClient(None, "username",
    #                     "password",
    #                     "apikey",
    #                     "environment")
    fileName = "documents/doc1.pdf"

    with open(fileName, "rb") as test_file:
        content = base64.b64encode(test_file.read())

    # subject = "a"
    # date1 = "01-01-15"
    # date2 = "12-12-15"
    # type = "contract"
    author = "Martin Voisin"
    comment = "My Comment"
    # ref = "ref"
    # amount = "amount"
    # tag =  ['a']
    # generic1 = ['b']
    # generic2 = ['c']

    file = {'content' : content, 'fileName' : fileName, 'author':author, 'comment':comment}

    try :
        res = c.archive(file)
        print(res)
    except suds.WebFault as detail:
        print(detail)
