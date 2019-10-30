import requests
from datetime import datetime
import os

apiKey = os.environ.get("NBAKEY")
print(apiKey)

#SportsDataIO

def todayGames():
    '''
    Return a list of games scheduled for tonight contaiting interested keys
    'GameID', 'AwayTeam', 'HomeTeam', 'AwayTeamScore', 'HomeTeamScore', 'IsClosed'
    '''
    now = "2019-OCT-29"

    #Send http request to get info about games
    #https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/{date}
    response = requests.get(
        url="https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/" + now,
        headers={'Ocp-Apim-Subscription-Key':apiKey}
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
        #IsClosed = false -> Game not ended
        #IsClosed = true -> game ended -> Print the final score
        if(not game['IsClosed']):
            print(f'{game["AwayTeam"]} @ {game["HomeTeam"]}')
        else:
            print(f'{game["AwayTeam"]} @ {game["HomeTeam"]}\n\t{game["AwayTeamScore"]} - {game["HomeTeamScore"]}')
        print(f'\tGameID: {gameId}')


def newPlayer(firstName, lastName, team):
    playerID=0
    '''
        Return a dict representing a player
        {name: , team: , playerID:}

        parameters:
            -name: Player's name
            -team: Team abbreviation
    '''
    #https://api.sportsdata.io/v3/nba/stats/json/Players/TEAM?key=KEY
    response = requests.get(
        url= 'https://api.sportsdata.io/v3/nba/stats/json/Players/' + team.upper(),
        headers={'Ocp-Apim-Subscription-Key':apiKey}
    )

    jsonPlayers = response.json()
    for player in jsonPlayers:
        if(lastName == player['LastName']):
            playerID = player['PlayerID']
            

    if(playerID==0):
        print("Errore nel cercare il giocatore\nAssicurarsi di aver inserito un cognome valido")
    return {'name': firstName + ' ' + lastName, 'team':team, 'playerID':playerID}

def printPlayer(player):
    '''
        Print a player dict in a readable form
        
        parameters
            -player dict containing ['name', 'team'] keys
    '''
    print(f"{player['name']} with ID {player['playerID']}, plays for {player['team']} ")

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
    myPlayers.append(newPlayer('John', 'Collins', 'ATL'))
    myPlayers.append(newPlayer('Dwight', 'Howard', 'LAL'))
    myPlayers.append(newPlayer('Anthony', 'Davis', 'LAL'))

    printTeam(myPlayers)

    #Set of teams that roster some of my players
    teamSet = set(player['team'] for player in myPlayers)

    '''
    I'm interested in my Player Stats by date and playerID
    https://api.sportsdata.io/v3/nba/stats/json/PlayerGameStatsByPlayer/DATE/PLAYEID?key=keyapiKey

    Stats I'm interested in:
        ESPN names: FG%, FT%, 3PM, REB, AST, STL, BLK, TO, DD, TD, PTS
        SportsDataIO names: ['FieldGoalsPercentage', 'FreeThrowsPercentage', 'ThreePointersMade', 'Rebounds', 'Assists', 'Steals', 'BlockedShots',
            'Turnovers', 'DoubleDoubles', 'TripleDoubles', 'Points']

        DD and TD = 0.0 OR 1.0
    '''

    #Return empty string if playerID does not play in that DATE
    #https://api.sportsdata.io/v3/nba/stats/json/PlayerGameStatsByPlayer/DATE/PLAYEID?key=keyapiKey
    response = requests.get(
        url = 'https://api.sportsdata.io/v3/nba/stats/json/PlayerGameStatsByPlayer/{}/{}'.format('2019-OCT-29', 20001835), #Collins
        headers={'Ocp-Apim-Subscription-Key':apiKey}   
    )


    print(response.json())
    


main()

