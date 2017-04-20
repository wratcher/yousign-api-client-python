import suds

import ysApi
from ysApi import FileToSign,Signer,VisibleOptions

if __name__ == "__main__":

    # Config File
    c = ysApi.ApiClient('../config/config.ini')

    # c = ysApi.ApiClient(None, "username",
    #                     "password",
    #                     "apikey",
    #                     "environment")

    # Create the signer(s) list.
    # Create your "Signer" objects with five parameters :
    #   * FirstName
    #   * LastName
    #   * Phone
    #   * Mail Address
    #   * AuthenticationMode (sms/mail, default:sms)
    listSignersInfos = [Signer(firstName="Martin",lastName="Voisin",phone="+33601020304",mail="martin.voisin@hostname.com",authenticationMode="sms"),
                        Signer(firstName="Sandra",lastName="Duchemin",phone="+33601020305",mail="sandra.duchemin@hostname.com",authenticationMode="sms"),
                        Signer(firstName="Pierre",lastName="Dupuis",phone="+33601020306",mail="pierre.dupuis@hostname.com",authenticationMode="sms")]

    # Files to sign
    # You can sign one file or more
    lstFile = ["/documents/doc1.pdf","/documents/doc2.pdf"]

    # Pdf passwords if they have one.
    pdfPassword = ['','']
    # Signature Options. For each file specify four parameters :
    #   * visibleSignaturePage
    # , * isVisibleSignature,
    #   * visibleRectangleSignature
    #   * mail

    # In this example, you choose your options for the first file, then for the second one (for each signer).
    options = [[VisibleOptions(1,True,"0,39,80,0","martin.voisin@hostname.com"),
                VisibleOptions(1,True,"0,39,80,0","sandra.duchemin@hostname.com"),
                VisibleOptions(1,True,"0,39,80,0","pierre.dupuis@hostname.com")],

               [VisibleOptions(1,True,"0,39,99,0","martin.voisin@hostname.com"),
                VisibleOptions(1,True,"0,39,99,0","sandra.duchemin@hostname.com"),
                VisibleOptions(1,True,"0,39,99,0","pierre.dupuis@hostname.com")]]


    listSignedFile = []

    # Verify that each file is associated with its options.
    if len(lstFile)!=len(options):
        print("Files and options numbers must be identical")

    # Verify that each signer is associated with his signature options.
    for op in options:
        if len(op)!=len(listSignersInfos):
            print("Make sure that all signers are associated with signature options  [Not fatal]")

    # Associate each file to its options and its password if it exists.
    for i in range (len(lstFile)) :
        listSignedFile.append(FileToSign(lstFile[i],options[i], pdfPassword[i]))


    #Other options
    message='',
    title='',
    initMailSubject=False
    initMail=False
    endMailSubject=False
    endMail=False
    language='FR'
    mode='IFRAME'
    archive=False

    try :
        res = c.initSign(listSignedFile, listSignersInfos, message, title, initMailSubject, initMail, endMailSubject, endMail, language, mode, archive)

        tokens = res['tokens']
        token=[]
        mail=[]
        for el in tokens:
            token.append(el['token'])
        for el in tokens:
            mail.append(el['mail'])

        # To display url associated with each email address (signers)
        print("Access Links to documents to sign :")
        for el in mail:
            ind = mail.index(el)
            print("Link for the signer  "+el+" : "+c.url_iFrame+'public/ext/cosignature/'+token[ind])

        # To display all information about the signatures
        print("Response from Yousign API :")
        print(res)
    except suds.WebFault as detail:
        print(detail)
