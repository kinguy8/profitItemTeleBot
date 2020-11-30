import telebot


with open('bot/files/token.txt', 'r') as r:
    for i in r.readlines():
        key, val = i.strip().split('=')
        TOKEN = val

botAPI = telebot.TeleBot(TOKEN)