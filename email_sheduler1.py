
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("abey.17ec@cmr.edu.in", "abey@cmr")
msg = "hello"
server.sendmail("abey.17ec@cmr.edu.in", "abeykakkuzhi@gmail.com", msg)
server.quit()
