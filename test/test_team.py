from __future__ import absolute_import
from __future__ import annotations

import unittest

from team import *

class TestTeam(unittest.TestCase):
    
    def test_wrong_addPlayer(self):
        try:
            team = team()
            team.addPlayer('WrongFirstParam', 'WrongSecondParam')
            self.fail('There should have been raised an Exception')
        except Exception:
            self.assertTrue(True)

    def test_wrong_instance(self):
        try:
            team = team()
            team.addPlayer([])
            self.fail('There should have been raised an Exception')
        except Exception:
            self.assertTrue(True)
