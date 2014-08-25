#SMTP Alerter- E-mails 
import smtplib
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "averyswords.settings")
'averyswords.settings'
from flashcards.models import Flashcard

f = open(addresses.txt, 'r')
addrs = []
for line in f:
	addrs.append(line.rstrip())

# Credentials (if needed)
username = 'username'
password = 'password'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()