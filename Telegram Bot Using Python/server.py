from bot import telegrambot
import requests
import json

bot = telegrambot("config.cfg")

r = requests.get("https://api.telegram.org/"ur_token"/getUpdates")
p= json.loads(r.content)

def make_reply(msg):
    reply = None
    if msg is not None:
        reply = "Welcome to ExtraHours " + p['result'][0]['message']['from']['first_name'] +" "+ p['result'][0]['message']['from']['last_name']
    return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)
