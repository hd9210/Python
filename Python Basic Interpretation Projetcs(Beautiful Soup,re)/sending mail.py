import smtplib,getpass

obj = smtplib.SMTP('smtp.gmail.com',587)

obj.ehlo()

obj.starttls()

email =''
password = ''
obj.login(email,password)
fromm = email
sub = input("input subject ")
msg = input("enter message ")
m="Subject :"+sub+'\n'+msg
to = email

obj.sendmail(fromm,to,m)
