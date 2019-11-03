from __future__ import absolute_import
from __future__ import annotations
import sys
sys.path.append('C:/Users/stefa/Desktop/BotFantasyESPN/src')

import unittest

from team import *

class TestTeam(unittest.TestCase):
    
    def test_wrong_addPlayer(self):
        try:
            print('Testing...')
            team = team()
            team.addPlayer('WrongFirstName','WrongLastName', 'WrongTeam')
            self.fail('There should have been raised an Exception')
        except Exception:
            self.assertTrue(True)

if __name__== '__main__':
    unittest.main()