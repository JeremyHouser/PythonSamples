#!/usr/bin/python

import OpenSSL
import ssl, socket
import requests
import array
import re

socket.setdefaulttimeout(10)

f = open("/home/srvraccnt/internal_ssl_hosts.txt", "r")
content = f.readlines()
f.close()
z = open("/home/srvraccnt/outside_ssl_hosts.txt", "r")
contentTwo = z.readlines()
z.close()

rawiplist = []

for z in content:
    ip = re.search(r'[0-9]+(?:\.[0-9]+){3}', z)
    if ip is not None:
        rawiplist.append(ip.group(0))
for z in contentTwo:
    ip = re.search(r'[0-9]+(?:\.[0-9]+){3}', z)
    if ip is not None:
        rawiplist.append(ip.group(0))

issTrim1 = "CN="
issTrim2 = "'>"
issTrim2Alt = "/"             # sometimes there is content after the CN, so this helps handle that issue
dateTrim1 = "b'"
dateTrim2 = "Z'"
iplist = []
for x in rawiplist:
    hostname = x.strip()
    try:
        # gets cert
        cert=ssl.get_server_certificate((hostname, 443))

        # serializes cert as an object
        certData = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)

        # find issuer
        issuer = str(certData.get_issuer())
        pos1 = issuer.index(issTrim1)
        pos1 = pos1 + 3
        pos2 = 0
        if (issuer.find(issTrim2Alt, pos1) > -1):
            pos2 = issuer.index(issTrim2Alt, pos1)
        else:
            pos2 = issuer.rfind(issTrim2, pos1)
        issuer = issuer[pos1:pos2]

        # find expiration date of certificate
        expiryDate = str(certData.get_notAfter())
        datePos1 = expiryDate.find(dateTrim1) + 1
        datePos2 = expiryDate.rfind(dateTrim2)
        expiryDate = expiryDate[datePos1:datePos2]
        
        # attempt to resolve hostname, making the owner easier to track down
        try:
            dnsRes = str(socket.gethostbyaddr(hostname)[0])
        except Exception:
            dnsRes = "Domain Name unresolvable"
            
        # create exhaustive list of all SSL certs
        iplist.append(hostname + "\t" + issuer + "\t" + expiryDate + "\t" + dnsRes + "\n")
    
    except Exception as e:
        pass
        """this is a dangerous statement, but in this case
          our internal network is so messy that adjusting for what were
          only various types of connection issues or timeouts thrown from
          http requests to private internal test sites made individual
          exception handling unnecessary with time constraints in consideration"""
        
        
v = open("/home/srvraccnt/issuerAndExpiry.txt", "w")
for ip in iplist:
    v.write(ip)
v.close()
