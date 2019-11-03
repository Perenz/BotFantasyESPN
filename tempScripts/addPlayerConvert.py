'''
Simple script that converts 
myPlayers.append(newPlayer('Dwight', 'Howard', 'LAL'))
INTO
myTeam.addPlayer('Collin', 'Sexton', 'CLE')
'''

def newPlayer(firstName, lastName, team):
    print ("myTeam.addPlayer('{}', '{}', '{}')".format(firstName,lastName,team))
    return 1

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
myPlayers.append(newPlayer('Mohamed', 'Bamba', 'ORL'))
myPlayers.append(newPlayer('Dillon', 'Brooks', 'MEM'))