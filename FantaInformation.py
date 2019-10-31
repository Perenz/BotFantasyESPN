import requests
from datetime import datetime
import os

apiKey = os.environ.get("NBAKEY")

#SportsDataIO

def todayGames():
    '''
    Return a list of games scheduled for tonight contaiting interested keys
    'GameID', 'AwayTeam', 'HomeTeam', 'AwayTeamScore', 'HomeTeamScore', 'IsClosed'
    '''
    date = datetime.now().strftime('%Y-%b-%d').upper()

    #Send http request to get info about games
    #https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/{date}
    response = requests.get(
        url="https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/" + date,
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

def toStringTodayGames(games):
    '''
    print a list of games in a readable form

    Parameters:
        games: list of dict with keys:['GameID', 'AwayTeam', 'HomeTeam', 'AwayTeamScore', 'HomeTeamScore', 'IsClosed']
    '''

    toRtn = ''
    for game in games:
        gameId = game["GameID"]
        #IsClosed = false -> Game not ended
        #IsClosed = true -> game ended -> Print the final score
        if(not game['IsClosed']):
            toRtn += f'{game["AwayTeam"]} @ {game["HomeTeam"]}\n'
        else:
            toRtn += f'{game["AwayTeam"]} @ {game["HomeTeam"]}\n\t{game["AwayTeamScore"]} - {game["HomeTeamScore"]}\n'
        toRtn += f'\tGameID: {gameId}\n'
    return toRtn


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
        print(f"Errore nel cercare il giocatore {firstName} {lastName}\nAssicurarsi di aver inserito un cognome valido")
    return {'name': firstName + ' ' + lastName, 'team':team, 'playerID':playerID}

def toStringPlayer(player):
    '''
        Print a player dict in a readable form
        
        parameters
            -player dict containing ['name', 'team'] keys
    '''
    return f"{player['name']} with ID {player['playerID']}, plays for {player['team']}\n"

def toStringTeam(players):
    '''
        Print a players list in a readable form

        parameters
            -players list containing players dict
    '''
    toRtn = ''
    for player in players:
        toRtn += toStringPlayer(player)

    return toRtn

def getStatsByDatePlayer(date, playerID):   
    '''
    Returns Player Stats by date and playerID
    https://api.sportsdata.io/v3/nba/stats/json/PlayerGameStatsByPlayer/DATE/PLAYEID?key=keyapiKey

    Stats I'm interested in:
        ESPN names: FG%, FT%, 3PM, REB, AST, STL, BLK, TO, DD, TD, PTS
        SportsDataIO names: ['FieldGoalsPercentage', 'FreeThrowsPercentage', 'ThreePointersMade', 'Rebounds', 'Assists', 'Steals', 'BlockedShots',
            'Turnovers', 'DoubleDoubles', 'TripleDoubles', 'Points']

        DD and TD = 0.0 OR 1.0

    parameters
        - date: format sample: 2019-OCT-29
        - playerID
    '''

    myKeys = {'FieldGoalsPercentage':'FG%', 'FreeThrowsPercentage':'FT%', 'ThreePointersMade':'3PM', 'Rebounds':'REB', 'Assists':'AST', 'Steals':'STL', 'BlockedShots':'BLK',
            'Turnovers':'TO ', 'DoubleDoubles':'DD ', 'TripleDoubles':'TD ', 'Points':'PTS'}

    #Return empty string if playerID does not play in that DATE
    #https://api.sportsdata.io/v3/nba/stats/json/PlayerGameStatsByPlayer/DATE/PLAYEID?key=keyapiKey
    response = requests.get(
        url = 'https://api.sportsdata.io/v3/nba/stats/json/PlayerGameStatsByPlayer/{}/{}'.format(date, playerID), #Collins
        headers={'Ocp-Apim-Subscription-Key':apiKey}   
    )

    #print(response.json().keys())

    #Check if the playerID played on that date
    playerStats = ''
    if response.text != '':
        jsonResp = response.json()
        playerStats = {}
        playerStats['Name'], playerStats['playerID'] = jsonResp['Name'], playerID
        for key in myKeys.keys():
            playerStats[myKeys[key]] = jsonResp[key]
    
    return playerStats
    
def toStringPlayerStats(playerStats):
    toRtn = ''
    if(playerStats!=''):
        for key in playerStats.keys():
            if key != 'playerID':
                toRtn += "{:<15} {:<15}\n".format(key, playerStats[key])
    return toRtn

def toStringTeamStats(date, players):
    toRtn = ' '
    for player in players:
        toRtn += toStringPlayerStats(getStatsByDatePlayer(date, player['playerID']))

    return toRtn





def main():
    date = datetime.now().strftime('%Y-%b-%d').upper()
    #print(date)

    games = todayGames()
    print(toStringTodayGames(games))

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
    myPlayers.append(newPlayer('Rudy', 'Gobert', 'UTA'))

    print(toStringTeam(myPlayers))

    #Set of teams that roster some of my players
    teamSet = set(player['team'] for player in myPlayers)
    
    print(toStringTeamStats('2019-OCT-30', myPlayers))


#main()
