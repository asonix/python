#!/usr/bin/env python3

import urllib.request
import re
import smtplib
from email.mime.text import MIMEText
import time
import getpass

url = "http://checkip.dyndns.org"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = input("Enter your gmail username: ")
SMTP_PASSWORD = getpass.getpass("Enter your password: ")
oldIP = []

while(True):
    request = urllib.request.urlopen(url).read().decode("utf-8")
    theIP = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", request)
# Send the message via our own SMTP server, but don't include the
# envelope header.
    print("current ip is "+"".join(theIP))
    if (theIP != oldIP):
        print("preparing to send")
        oldIP = theIP
        msg = MIMEText("the current ip is %s" % "".join(theIP))
        msg['subject'] = "[SSH] " + "".join(theIP)
        msg['To'] = "asonix.dev@gmail.com"
        msg['From'] = "asonix.dev@gmail.com"
        mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        mail.starttls()
        mail.login(SMTP_USERNAME, SMTP_PASSWORD)
        mail.sendmail("asonix.dev@gmail.com", ["asonix.dev@gmail.com"], msg.as_string())
        mail.quit()
        print("sent")
    time.sleep(60*1)
