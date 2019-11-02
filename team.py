from APIInterface import getJson
from player import player

class team:
    def __init__(self):
        self.players = []

    def __str__(self):
        '''
        Print the team in a readable form
        '''
        toRtn = ''
        for p in self.players:
            toRtn += p.__str__() + '\n'

        return toRtn

    def addPlayer(self, *args, **kwds):
        '''
        Function that add a player to the team instance
        2 ways to call it:
        team.addPlayer(Player)

        team.addPlayer(firstName, lastName, team)
        '''

        if(len(args)==1 and isinstance(args[0], player)):
            self.players.append(args[0])
        elif(len(args)==3):
            self.players.append(player(args[0],args[1],args[2]))
        else:
            raise TypeError('2 ways to call addPlayer:\nteam.addPlayer(Player)\nteam.addPlayer(firstName, lastName, team)')
