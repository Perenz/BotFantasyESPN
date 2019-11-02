import typing
from APIInterface import getJson

class gameDay:
    def __init__(self, date):
        self.date = date
        self.games = []
        '''
        Return an instance of gameDay with all the games scheduled for that DATE

        Date in format %Y-%b-%d: 2019-OCT-30
        '''

        #Send http request to get info about games
        #https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/{date}

        jsonGames = getJson("https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/" + date)

        # Is returned a list of games, each game is represented by a dict
        for g in jsonGames:
            # Keys: ['GameID', 'AwayTeam', 'HomeTeam', 'AwayTeamScore', 'HomeTeamScore', 'IsClosed']
            newGame = game(g['AwayTeam'], g['HomeTeam'], g['GameID'])
            #IsClosed = false -> Game not ended
            #IsClosed = true -> game ended -> Print the final score
            if(g['IsClosed']):
                newGame.endGame(g['AwayTeamScore'], g['HomeTeamScore'])
            
            self.games.append(newGame)


    def __str__(self):
        toRtn = ''
        for g in self.games:
            toRtn += str(g) + '\n'
        return toRtn

    def addGame(self, *args, **kwds):
        '''
        Function that add a game to tha gameDay instance
        2 ways to call it:
        gameDay.addGame(game) SUGGESTED

        gameDay.addGame(awayTeam, homeTeam, gameID)
        '''

        if(len(args)==1 and isinstance(args[0], game)):
            self.players.append(args[0])  
        elif(len(args)==3):
            self.players.append(game(args[0],args[1],args[2]))
        else:
            raise TypeError('2 ways to call addGame:\ngameDay.addGame(game)\ngameDay.addGame(awayTeam, homeTeam, gameID)')

    def getPlayingTeams(self):
        '''
        Return a list containing the abbrevations of the Team involved in that gameDay
        '''
        teamsList = []
        for g in self.games:
            teamsList.append(g.homeTeam)
            teamsList.append(g.awayTeam)
        return teamsList



class game:
    def __init__(self, awayTeam, homeTeam, gameID):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.gameID = gameID
        self.ended = False

    def __str__(self):
        if(self.ended):
            return f'{self.awayTeam} @ {self.homeTeam}\n\t{self.awayScore} - {self.homeScore}\t\t(ID:{self.gameID})'
        else:
            return f'{self.awayTeam} @ {self.homeTeam}\n'

    def endGame(self, awayScore, homeScore):
        self.ended = True
        self.awayScore = awayScore
        self.homeScore = homeScore


#TODO: I should use this function as gameDay init    
def getGameDay(date) -> gameDay:
    '''
    Return an instance of gameDay with all the games scheduled for that DATE

    Date in format %Y-%b-%d: 2019-OCT-30
    '''

    #Send http request to get info about games
    #https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/{date}

    jsonGames = getJson("https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/" + date)

    toRtnGameDay = gameDay(date)
    # Is returned a list of games, each game is represented by a dict
    for g in jsonGames:
        # Keys: ['GameID', 'AwayTeam', 'HomeTeam', 'AwayTeamScore', 'HomeTeamScore', 'IsClosed']
        newGame = game(g['AwayTeam'], g['HomeTeam'], g['GameID'])
        #IsClosed = false -> Game not ended
        #IsClosed = true -> game ended -> Print the final score
        print(g['IsClosed'], type(g['IsClosed']))
        if(g['IsClosed'] == 'true'):
            newGame.endGame(g['AwayTeamScore', 'HomeTeamScore'])


    #Return a list of dict containing interested keys    
    return toRtnGameDay