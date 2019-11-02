class player:
    '''
    Class that handles the player'stats computation
    '''
    def __init__(self, firstName, lastName, team):
        self.firstName = firstName
        self.lastName = lastName
        self.team=team

    def __str__(self):
        return self.firstName + ' ' + self.lastName + ', plays for ' + self.team
