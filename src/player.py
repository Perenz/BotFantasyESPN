from APIInterface import getJson
import json




class player:
    '''
    Class that handles the player'stats computation
    '''
    def __init__(self, firstName, lastName, team) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.team=team

        #jsonPlayers = getJson('https://api.sportsdata.io/v3/nba/stats/json/Players/' + self.team.upper())

        with open('files/activePlayers.json') as jSonFile:
            jsonPlayers = json.load(jSonFile)

        findFlag = False
        for player in jsonPlayers:
            if(lastName == player['LastName'] and firstName == player['FirstName']):
                self.playerID = player['PlayerID']
                findFlag = True
                

        if(not findFlag):
            raise ValueError("Error in retrieving Player's lastName," + " be sure lastName and team are correct")

    def __str__(self) -> None:
        return self.firstName + ' ' + self.lastName + ', plays for ' + self.team

class dailyStats:
    pass 
