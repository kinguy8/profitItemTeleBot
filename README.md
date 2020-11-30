# ProfitItemBot 

A bot designed to search for a Dota 2 item at a price lower than on the Steam marketplace. Also returns the cost of the item and the difference.

### Notes

In a directory `bot/files` create a file "token.txt" and insert token by key "TOKEN" to initialize your bot 
Sample: "TOKEN=your_token".
Also you can check info about message sender in file log

### Requirements
This API is tested with Python Python 3.6-3.9 and Pypy 3. There are two ways to install the library:

Installation using pip (a Python package manager)*:
$ pip install pyTelegramBotAPI

### Installation from source (requires git):
$ git clone https://github.com/kinguy8/profitItemTeleBot.git
$ cd profitItemTeleBot
$ python main.py

### Available commands for interacting with the bot:
> ##### Send `/start` to start a dialogue
> ##### Send `/info` for detailed information about the bot
> ##### Send `your some text` for find you item 

