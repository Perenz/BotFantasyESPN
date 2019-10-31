import telebot
from datetime import timedelta
from FantaInformation import *

teleBotToken = os.environ['TELETOKEN']

bot = telebot.TeleBot(teleBotToken)

myPlayers = []
myPlayers.append(newPlayer('John', 'Collins', 'ATL'))
myPlayers.append(newPlayer('Dwight', 'Howard', 'LAL'))
myPlayers.append(newPlayer('Anthony', 'Davis', 'LAL'))
myPlayers.append(newPlayer('Rudy', 'Gobert', 'UTA'))

@bot.message_handler(commands=['today', 'night'])
def send_welcome(message):
    date = datetime.now() - timedelta(days=1)
    date = date.strftime('%Y-%b-%d').upper()
    response = toStringTeamStats(date,myPlayers)
    #print(response)
    bot.reply_to(message, response)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
        response = 'Prova'
        bot.reply_to(message, response)


bot.polling()