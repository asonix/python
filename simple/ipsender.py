#!/usr/bin/env python3

import urllib.request
import re
import smtplib
from email.mime.text import MIMEText
import time
import getpass
from subprocess import Popen, PIPE

url = "http://checkip.dyndns.org"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = input("Enter your gmail username: ")
SMTP_PASSWORD = getpass.getpass("Enter your password: ")
oldExtIP = ''
oldIntIP = ''

while(True):
    grep1 = Popen(['grep', '-i', 'inet'], stdin=PIPE, stdout=PIPE)
    grep2 = Popen(['grep', '-i', 'eth0'], stdin=PIPE, stdout=PIPE)
    com = Popen(['ip', 'addr'], stdout=PIPE)
    out = grep1.communicate(grep2.communicate(com.stdout.read())[0])[0].decode()
    theIntIP = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", out)[0]

    request = urllib.request.urlopen(url).read().decode("utf-8")
    theExtIP = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", request)[0]
    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    print("current ip is "+theExtIP+" and "+theIntIP)
    if (theExtIP != oldExtIP or theIntIP != oldIntIP):
        print("preparing to send")
        oldIntIP = theIntIP
        oldExtIP = theExtIP
        msg = MIMEText("the current external ip is {} and the internal ip is {}".format(theExtIP,theIntIP))
        msg['subject'] = "[SSH] " + theExtIP + " " + theIntIP
        msg['To'] = "asonix.dev@gmail.com"
        msg['From'] = "asonix.dev@gmail.com"
        mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        mail.starttls()
        mail.login(SMTP_USERNAME, SMTP_PASSWORD)
        mail.sendmail("asonix.dev@gmail.com", ["asonix.dev@gmail.com"], msg.as_string())
        mail.quit()
        print("sent")
    time.sleep(60*1)
