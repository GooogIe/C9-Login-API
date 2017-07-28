#!/usr/bin/env python

import requests

LOGIN_URL = "https://c9.io/auth/login"

# Returns the dict with the data
def buildPayload(username,password):
	return {
  		'username': username,
  		'password': password,
	}

# Performs the login and checks for account subscription
def login(username,password):

	payload = buildPayload(username,password)

	headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, sdch, br",
        "Accept-Language":"it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Host":"c9.io",
        "Referer":"https://c9.io/",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
        "X-Requested-With":"XMLHttpRequest",
    	}
	login = requests.post(LOGIN_URL, headers=headers, data=payload)	# Perform the login
	
	if "Incorrect" in login.text:
		return [False,"Dead"]
	else:
		return [True,"Working"]
