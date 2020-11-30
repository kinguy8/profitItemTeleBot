import random

from bot import botAPI
from bot.utils.utils import return_price, save_data_to_file, read_data_file, get_steam_price
from bot.settings import WELCOME_MSG, IM_BOT, ITEM_FOUND, ITEM_NOT_FOUND, list, HELLO_LIST, RANDOM_HELLO, WARNING_MESSAGE


@botAPI.message_handler(commands=['start'])
def send_message(message):
    """WELCOME MESSAGE FOR USER"""
    botAPI.send_message(message.chat.id, WELCOME_MSG.format(message.from_user) +"\n"+ IM_BOT,
    parse_mode='html')


@botAPI.message_handler(commands=['info'])
def send_info(message):
    """SHOW INFO ABOUT BOT"""
    botAPI.send_message(message.chat.id, IM_BOT,
    parse_mode='html')


@botAPI.message_handler(content_types=['text'])
def echo_all(message):
    """BUILD MESSAGE FOR USER ABOUT ITEM"""
    if (str(message.text)).lower() in HELLO_LIST:
        botAPI.send_message(message.chat.id, random.choice(RANDOM_HELLO).format(message.from_user.first_name),
                            parse_mode='html')
    elif (str(message.text)).lower() in list:
        botAPI.send_message(message.chat.id, WARNING_MESSAGE.format(message.from_user.first_name),
                            parse_mode='html')
    else:
        msg = return_price(message.text)
        if msg is not None:
            rus_price = msg + ' Rub'
            steam_price = get_steam_price(str(message.text).strip()) if msg else ""
            save_data_to_file(message)
            d1 = read_data_file()
            botAPI.send_message(message.chat.id, ITEM_NOT_FOUND if not msg and steam_price else ITEM_FOUND.format(message.text, rus_price, int(steam_price)-int(msg)), parse_mode='html')
        else:
            botAPI.send_message(message.chat.id, ITEM_NOT_FOUND, parse_mode='html')

botAPI.polling()