import os
import base64


class FileToSign(dict):
    def __init__(self, name, visibleOptions, password, **kwargs):
        super(FileToSign, self).__init__(**kwargs)
        dirName = "../examples/documents/"
        f = dirName+os.path.basename(name)
        self["name"] = os.path.basename(f)
        with open(f, "rb") as test_file:
            content = base64.b64encode(test_file.read()).decode('ascii')
        self["content"] = content
        self["visibleOptions"] = visibleOptions
        self["pdfPassword"] = password


class Signer(dict):
    def __init__(self, firstName, lastName, phone, mail, authenticationMode="sms", **kwargs):
        super(Signer, self).__init__(**kwargs)
        self["firstName"] = firstName
        self["lastName"] = lastName
        self["phone"] = phone
        self["mail"] = mail
        self["authenticationMode"] = authenticationMode


class VisibleOptions(dict):
    def __init__(self, visibleSignaturePage=1, isVisibleSignature=True, visibleRectangleSignature="0,39,99,0", mail="", **kwargs):
        super(VisibleOptions, self).__init__(**kwargs)
        self["visibleSignaturePage"] = visibleSignaturePage
        self["isVisibleSignature"] = isVisibleSignature
        self["visibleRectangleSignature"] = visibleRectangleSignature
        self["mail"] = mail
