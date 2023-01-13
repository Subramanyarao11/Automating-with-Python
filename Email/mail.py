import smtplib

conn = smtplib.SMTP('smtp.gmail.com' , 587)
conn.ehlo()
# print(conn.ehlo())
conn.starttls()
conn.login('subramanya11rao@gmail.com' , 'password')
conn.sendmail('subramanya11rao@gmail.com' , 'imsmr17@gmail.com' , 'Subject: So long...\n\nDear Subramanya, so long and thanks for all the Tips!.')
conn.quit()
