#email_shed_prog_2
import smtplib
server=smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("abey.17ec@cmr.edu.in", "password")
a="hello"
l=["abeykakkuzhi@gmail.com","dopemathew4@gmail.com","antonyax@gmail.com"]
for i in l:
    server.sendmail("abey.17ec@cmr.edu.in",i,a)
    server.quit()

