class playerDailyStats:

    myKeys = {'FieldGoalsPercentage':'FG%', 'FreeThrowsPercentage':'FT%', 'ThreePointersMade':'3PM', 'Rebounds':'REB', 'Assists':'AST', 'Steals':'STL', 'BlockedShots':'BLK',
            'Turnovers':'TO ', 'DoubleDoubles':'DD ', 'TripleDoubles':'TD ', 'Points':'PTS'}

    def __init__(self, statsDict):
        self.playerStats = {}
        self.playerStats['Name'] = statsDict['Name']
        for key in playerDailyStats.myKeys.keys():
            self.playerStats[playerDailyStats.myKeys[key]] = statsDict[key]

    def __str__(self):
        toRtn = self.playerStats['Name'] + ':'
        for key in self.playerStats.keys():
            if key != 'Name':
                toRtn += "\t{:<15} {:<15}\n".format(key, self.playerStats[key])
        return toRtn


class myTeamDailyStats:
    def __init__(self):
        self.teamStats = []

    def addPlayerStats(self, playerStats):
        self.teamStats.append(playerStats)

    def __str__(self):
        toRtn = ''
        for p in self.teamStats:
            toRtn += str(p) + '\n'

        return toRtn
