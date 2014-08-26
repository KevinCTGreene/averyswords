#SMTP.PY
#Alerts family members of words for the upcoming week

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "averyswords.settings")
'averyswords.settings'
import smtplib
from flashcards.views import getActiveWords
from flashcards.models import Flashcard

f = open("addresses.txt", 'r')
toaddrs = []
for line in f:
	toaddrs.append(line.rstrip())
f.close()

p = open("authinfo.txt", 'r')
#username = p.readline().rstrip()
username = 'kctg.1985@gmail.com'
password = 'L0ckedout'
p.close()

active = getActiveWords()
msg = "Subject: Avery's words for the week\n\nAvery's words for the week are:\n\n"
for word in active:
        msg = msg +  "%s\n" % word.content
else:
        msg = msg + "\nGo to http://www.averyswords.com and teach them to her!"
# Credentials (if needed)


# The actual mail send
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail('kctg.1985@gmail.com', toaddrs, msg)
server.quit()

print username
print password
print msg
