import telebot
from player import player
from team import team
import gameDay
import os
from datetime import timedelta

teleBotToken = os.environ['TELETOKEN']

bot = telebot.TeleBot(teleBotToken)

#This can be sostituted with a WebScraping operation from https://fantasy.espn.com/basketball/team?leagueId=28348224&teamId=7&seasonId=2020

#Add a module that calls the API only once and keep lastName, team and PlayerID
'''
myPlayers = []
myPlayers.append(newPlayer('Dwight', 'Howard', 'LAL'))
myPlayers.append(newPlayer('Anthony', 'Davis', 'LAL'))
myPlayers.append(newPlayer('Shai', 'Gilgeous-Alexander', 'OKC'))
myPlayers.append(newPlayer('Zach', 'LaVine', 'CHI'))
myPlayers.append(newPlayer('Khris', 'Middleton', 'MIL'))
myPlayers.append(newPlayer('Dario', 'Saric', 'PHO'))
myPlayers.append(newPlayer('Collin', 'Sexton', 'CLE'))
myPlayers.append(newPlayer('Tobias', 'Harris', 'PHI'))
myPlayers.append(newPlayer("De'Aaron", 'Fox', 'SAC'))
myPlayers.append(newPlayer('Joe', 'Harris', 'BKN'))
myPlayers.append(newPlayer('Kent', 'Bazemore', 'POR'))
myPlayers.append(newPlayer('Mo', 'Bamba', 'ORL'))
myPlayers.append(newPlayer('Dillon', 'Brooks', 'MEM'))

'''


#Add to the team all the players from ESPN Fantasy
#TODO Automated inseriment through ESPN Fantasy website with Selenium Webscraping:
# https://fantasy.espn.com/basketball/team?leagueId=28348224&teamId=7&seasonId=2020

myTeam = team()
myTeam.addPlayer('Dwight', 'Howard', 'LAL')
myTeam.addPlayer('Shai', 'Gilgeous-Alexander', 'OKC')
myTeam.addPlayer('Zach', 'LaVine', 'CHI')
myTeam.addPlayer('Rudy', 'Gobert', 'UTA')
myTeam.addPlayer('Khris', 'Middleton', 'MIL')
myTeam.addPlayer('Dario', 'Saric', 'PHO')
myTeam.addPlayer('Collin', 'Sexton', 'CLE')
myTeam.addPlayer('Tobias', 'Harris', 'PHI')
myTeam.addPlayer("De'Aaron", 'Fox', 'SAC')
myTeam.addPlayer('Joe', 'Harris', 'BKN')
myTeam.addPlayer('Kent', 'Bazemore', 'POR')
myTeam.addPlayer('Mohamed', 'Bamba', 'ORL')
myTeam.addPlayer('Dillon', 'Brooks', 'MEM')
# print(myTeam)


gD = gameDay.gameDay('2019-OCT-29')

#print(gD)
#print(gD.getPlayingTeams())

teamStats = gD.getTeamStatsByGameDay(myTeam)
print(teamStats)

#For every player that plays in a team belongig to PlayingTeam -> compute daily Stats 

@bot.message_handler(commands=['today', 'night'])
def send_stats(message):
    '''
    date = datetime.now() - timedelta(days=1)
    date = date.strftime('%Y-%b-%d').upper()
    response = toStringTeamStats(date,myPlayers)
    #print(response)
    bot.reply_to(message, response)
    '''

@bot.message_handler(commands=['players'])
def send_players(message):
    '''
    response = toStringTeam(myPlayers)
    bot.reply_to(message, response)
    '''


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    '''
        response = '/today'
        bot.reply_to(message, response)
    '''


#bot.polling()