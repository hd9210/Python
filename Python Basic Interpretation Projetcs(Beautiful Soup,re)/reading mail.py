import imaplib,email,re

obj = imaplib.IMAP4_SSL('imap.gmail.com')

mail =''
password = ''
obj.login(mail,password)
obj.select('inbox')
typ,data=obj.search(None,'SUBJECT "hello world"')

idd=data[0]

res,dataa=obj.fetch(idd,'(RFC822)')
st=''
raw=email.message_from_string(dataa[0][1].decode('utf-8'))
for i in raw.walk():
    if i.get_content_type()=='text/plain':
        st= st + str(i.get_payload(decode=True))

lst=re.findall(r'[^\\n+]',st)
print(''.join(lst))