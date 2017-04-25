# -*- coding: utf-8 -*-
import hashlib
import os
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import RawConfigParser as ConfigParser
import logging
from suds.client import Client
from suds.sax.element import Element

logging.basicConfig(level=logging.FATAL)

"Here is a full Python Client for Yousign Api"

class ApiClient():

    @property
    def env_dict(self):
        return {"demo":'apidemo.yousign.fr:8181/',"prod":'api.yousign.fr:8181/'}
    @property
    def url_dict(self):
        return {"demo":'https://demo.yousign.fr/',"prod":'https://yousign.fr/'}

    @property
    def WSDL_AUTH_URL(self):
        return "https://%s/AuthenticationWS/AuthenticationWS?wsdl" % self.environment
    @property
    def WSDL_SIGN_URL(self):
        return "https://%s/CosignWS/CosignWS?wsdl" % self.environment
    @property
    def WSDL_ARCH_URL(self):
        return "https://%s//ArchiveWS/ArchiveWS?wsdl" % self.environment


    "Method used to hash(encrypt) the password"
    @staticmethod
    def hashPassword(password):
        password = hashlib.sha1(password.encode('utf-8')).hexdigest().encode('ascii')
        return hashlib.sha1(password + password).hexdigest()

    """
    Method used to load user configuration (in order to establish a connection)from a file.
    Specified parameters are username, password and the API key.
    User can choose to put (or no) an encrypted password.
    """
    def parseConf(self, pathParameters):
        config = ConfigParser()
        config.read(pathParameters)
        self.username = config.get('client', 'username')

        isEncryptedPassword = config.get('client','isEncryptedPassword')
        if isEncryptedPassword == 'false':
            self.password = ApiClient.hashPassword(config.get('client', 'password'))
        elif isEncryptedPassword == 'true':
            self.password = config.get('client', 'password')
        self.apikey = config.get('client','apikey')

        envKey = config.get('client', 'environment')
        self.environment = self.env_dict.get(envKey)
        self.url_iFrame = self.url_dict.get(envKey)


    """
    Creation of the client by using the config file.
    Creation of WSDL headers and setting of the URL depending on the WSDL addresses(Authentication, Signature, Archive)
    """
    def createHeaders(self):
        ssn = [Element('apikey').setText(self.apikey),
        Element('username').setText(self.username),
        Element('password').setText(self.password)]

        self._authClient = Client(self.WSDL_AUTH_URL, soapheaders=ssn)
        self._signClient = Client(self.WSDL_SIGN_URL, soapheaders=ssn)
        self._archClient = Client(self.WSDL_ARCH_URL, soapheaders=ssn)

    def __init__(self,pathParameters = None,username="",password="",apikey="",environment="demo"):
        if pathParameters!= None and os.path.isfile(pathParameters):
            self.parseConf(pathParameters)
        else :
            self.username = username
            self.password = password
            self.apikey = apikey
            self.environment = self.env_dict.get(environment)
            self.url_iFrame = self.url_dict.get(environment)
        self.createHeaders()

    """
    Method used to check the connection to the API. All WS are using soap header for the authentication. There are 3 tags :
        username : your mail address (used in subscription)
        password : your password (used in subscription). You need to hash your password. Here is the hash calculation : sha1(sha1(clearPassword)+sha1(clearPassword)). Be carreful, this is a concatenation. In some languages (like PHP), the symbol to concatenate strings is '.', not '+'. This calcul is done to secure your password. If clearPassword = "test123", password = "6bc498d4dc47ec2177ff42151139da01c1660ddf"
        apikey : your apikey
    The connect method should be used just for testing. You do not have to call it each time you want to call the API
    """""
    def connect(self):
        return getattr(self._authClient.service, 'connect')(None)

    """
    This method is used to initialize a signature process. File(s) and information about signer(s) are sent. Only one signer could be used."
    For each parameter you can see its details in the online documentation
    """
    def initSign(self,
                  lstCosignedFile,
                  lstCosignerInfos,
                  message='',
                  title='',
                  initMailSubject=False,
                  initMail=False,
                  endMailSubject=False,
                  endMail=False,
                  language='FR',
                  mode='IFRAME',
                  archive=False):

        return getattr(self._signClient.service, 'initCosign')(lstCosignedFile=lstCosignedFile,
                                                    lstCosignerInfos=lstCosignerInfos,
                                                    title=title,
                                                    message=message,
                                                    initMailSubject=initMailSubject,
                                                    initMail=initMail,
                                                    endMailSubject=endMailSubject,
                                                    endMail=endMail,
                                                    language=language,
                                                    mode=mode,
                                                    archive=archive)
    """
    Get signed files associated with a signature process from an idDemand or a token. If the user is subscribed, you could use the idDemand parameter.
    If idFile is specified, we only get the file associated with this id (this id must be part of the signature process).
    """
    def getSignedFilesFromDemand(self, idDemand, token='',idFile = ''):
        return getattr(self._signClient.service,'getCosignedFilesFromDemand')(idDemand = idDemand, token=token,idFile=idFile)

    "Get informations (status, name, file infos) about a signature process from an idDemand or a token. "
    def getInfosFromSignatureDemand(self, idDemand, token=''):
        return getattr(self._signClient.service,'getInfosFromCosignatureDemand')(idDemand = idDemand, token=token)

    """
    Get informations of all your signature processes.
    It includes all signature processes launched by the user and all signature processes where the user is a signer (the signature process has been launched by another user).
    Maximum results returned by this WS is 1000.
    """
    def getListSign(self, search='', firstResult=0, count=1000, status='COSIGNATURE_EVENT_REQUEST_PENDING', dateBegin='', dateEnd=''):
        return getattr(self._signClient.service,'getListCosign')(search = search, firstResult=firstResult,count=count,status=status,dateBegin=dateBegin,dateEnd=dateEnd)

    """
    Cancel a signature process which is not finished yet. Only the initiator could cancel it.
    Signers will not be able to sign documents. They will not be notified.
    """
    def cancelSignatureDemand(self, idDemand):
        return getattr(self._signClient.service,'cancelCosignatureDemand')(idDemand = idDemand)

    "Alert signers who have not signed document(s) yet."
    def alertSigners(self, idDemand, mailSubject='', mail='', language='FR'):
        return getattr(self._signClient.service,'alertCosigners')(idDemand = idDemand, mailSubject=mailSubject,mail=mail,language=language)

    "Archive document for 10 years with metadatas. Metadatas are used to find easily one (or several) archive."
    def archive(self, file):
        return getattr(self._archClient.service,'archive')( file = file)

    "Get archive file identified by its iua"
    def getArchive(self, iua):
        return getattr(self._archClient.service,'getArchive')(iua = iua)

    "Get complete archive file identified by its iua. "
    "It includes all proof informations about archive : descriptive metadatas, applicative metadatas, sealing datas and the initial archive file"
    def getCompleteArchive(self,iua):
        return getattr(self._archClient.service,'getCompleteArchive')( iua = iua)
