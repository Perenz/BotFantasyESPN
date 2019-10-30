import requests
from datetime import datetime

#SportsDataIO

#Games by date
#Date format: 2015-SEP-01
#https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/{date}


#now = datetime.now().strftime("%Y-%b-%d").upper()
now = "2019-OCT-29"

key = "a0e931bbd74a4897813722d32fec448f"


player ="John Collins"

#IsClosed = false -> Game not ended
#IsClosed = true -> game ended

def todayGames():
    '''
    Return a list of games scheduled for tonight contaiting interested keys
    'GameID', 'AwayTeam', 'HomeTeam', 'AwayTeamScore', 'HomeTeamScore', 'IsClosed'
    '''
    now = "2019-OCT-29"

    #Send http request to get info about games
    response = requests.get(
        url="https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/" + now,
        headers={'Ocp-Apim-Subscription-Key':'a0e931bbd74a4897813722d32fec448f'}
    )

    toRtnGames = []  
    # Is returned a list of games, each game is represented by a dict
    jsonGames = response.json()
    for game in jsonGames:
        keys = ['GameID', 'AwayTeam', 'HomeTeam', 'AwayTeamScore', 'HomeTeamScore', 'IsClosed']
        toRtnGames.append({key: game[key] for key in keys})

    #Return a list of dict containing interested keys    
    return toRtnGames

def printTodayGames(games):
    '''
    print a list of games in a readable form

    Parameters:
        games: list of dict with keys:['GameID', 'AwayTeam', 'HomeTeam', 'AwayTeamScore', 'HomeTeamScore', 'IsClosed']
    '''
    for game in games:
        gameId = game["GameID"]
        if(not game['IsClosed']):
            print(f'{game["AwayTeam"]} @ {game["HomeTeam"]}')
        else:
            print(f'{game["AwayTeam"]} @ {game["HomeTeam"]}\n\t{game["AwayTeamScore"]} - {game["HomeTeamScore"]}')
        print(f'\tGameID: {gameId}')


def newPlayer(name, team):
    '''
        Return a dict representing a player
        {name: , team: }

        parameters:
            -name: Player's name
            -team: Team abbreviation
    '''
    return {'name': name, 'team':team}

def printPlayer(player):
    '''
        Print a player dict in a readable form
        
        parameters
            -player dict containing ['name', 'team'] keys
    '''
    print(f"{player['name']}, plays for {player['team']}")

def printTeam(players):
    '''
        Print a players list in a readable form

        parameters
            -players list containing players dict
    '''
    for player in players:
        printPlayer(player)

def main():
    games = todayGames()
    printTodayGames(games)

    #I want to keep those games that involve players in my Fantasy Team
    '''
    Create a list of my Fantasy Player:
        - Name
        - Team
        - ...
    '''
    myPlayers = []
    myPlayers.append(newPlayer('John Collins', 'ATL'))
    myPlayers.append(newPlayer('Dwight Howard', 'LAL'))
    printTeam(myPlayers)


main()

