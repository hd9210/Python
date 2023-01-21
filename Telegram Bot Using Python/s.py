import requests
import json
import time
l=0
c=0
ch=True
while(ch):  
    f = open("count.txt", "r+") 
    r = requests.get("https://api.telegram.org/"ur_token"/getUpdates?timeout=100")
    p= json.loads(r.content)
    p=p['result']
    d = {}
    for j in range(0,len(p)): 
        d[j]=p[j]
    for k in range(l,len(p)):
        if 'message' in d[k].keys() and d[k]['message']["chat"]["id"]>0:
            c=c+1
            print(d[k]['message']["chat"]["id"])
            t= "Welcome to ExtraHours " + d[k]['message']['from']['first_name'] +" "+ d[k]['message']['from']['last_name']
            reply = "https://api.telegram.org/"ur_token"/sendMessage?chat_id={}&text={}".format(d[k]['message']["chat"]["id"],t)
            requests.get(reply)
    time.sleep(5)
    l=c
ch=True




