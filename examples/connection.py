#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import suds
import ysApi

if __name__ == "__main__":
    
        #If you use a config file to set your parameters.
    c = ysApi.ApiClient('../config/config.ini')

    """If you do not use a config file : you will give 5 parameters :
        * None : To specify that you are not using a config file.
        * Your login
        * Your password
        * Your apikey
        * The environment ("demo" or "prod").
    """
   # c = ysApi.ApiClient(None, "username",
   #                     "password",
   #                     "apikey",
   #                     "environment")
    try :
        print "Successful authentication"  if c.connect() else "Authentication failed"
    except suds.WebFault as detail:
        print detail
