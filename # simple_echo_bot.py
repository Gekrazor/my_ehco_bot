# simple_echo_bot
import telebot


# token
bot = telebot.TeleBot("", parse_mode=None)

# message commands
@bot.message_handler(commands=['start'])
def send_welcome(message):
	sti_greetings = open('pictures/greetings.webp', 'rb')
	bot.send_sticker(message.chat.id, sti_greetings)
	bot.send_message(message.chat.id, "Greetings! \nUse this commands for more /help /gowild \nOr just lets play in ECHO!")

@bot.message_handler(commands=['help'])
def send_wild(message):
	sti_no_help = open('pictures/no_help.webp', 'rb')
	bot.send_sticker(message.chat.id, sti_no_help)
	bot.send_message(message.chat.id, "No help for you here, punk.")

@bot.message_handler(commands=['gowild'])
def send_wild(message):
	pic_monke = open('pictures/monke.jpg', 'rb')
	bot.send_sticker(message.chat.id, pic_monke)
	bot.send_message(message.chat.id, "MONKE!!! UHUHUHAHAHAH AHUHUHUHAHH")


# echo messages
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
