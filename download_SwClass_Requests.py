#!/usr/bin/env python
# coding: utf-8

#Download SwClass based on Requests

# GET /downloadfiles.aspx?swindexcode=SwClass&type=530&columnid=8892 HTTP/1.1
# Host: www.swsindex.com
# Connection: keep-alive
# Cache-Control: max-age=0
# DNT: 1
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
# Referer: http://www.swsindex.com/idx0530.aspx
# Accept-Encoding: gzip, deflate
# Accept-Language: en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,zh-CN;q=0.6,zh;q=0.5
# Cookie: ASP.NET_SessionId=e3sd1uaqpfconu45b5xwsb31

import requests
import pandas as pd

Url = 'http://www.swsindex.com/downloadfiles.aspx?swindexcode=SwClass&type=530&columnid=8892'
Referer = 'http://www.swsindex.com/idx0530.aspx'
Headers = {'referer':Referer}

def download_SwClass():
    r =requests.get(Url,headers = Headers)
    with open('SwClass.xls', 'wb') as f:
        f.write(r.content)
    df = pd.DataFrame(pd.read_html('SwClass.xls')[0])
    return df

download_SwClass()

