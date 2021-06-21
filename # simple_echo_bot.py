# simple_echo_bot
import telebot
from telebot.types import Message

bot = telebot.TeleBot("1741018950:AAHNc5Tz3qbCbPpHMtb3jke1ZYw_NRy3768", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Greetings! \nUse this messages for more /help /gowild \nOr just lets play in ECHO!")

@bot.message_handler(commands=['help'])
def send_wild(message):
	bot.reply_to(message, "No help for you here, punk.")

@bot.message_handler(commands=['gowild'])
def send_wild(message):
	bot.reply_to(message, "MONKE!!! UHUHUHAHAHAH AHUHUHUHAHH")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
