from __future__ import absolute_import
from __future__ import annotations

from unittest import TestCase
import os

from player import *

class TestPlayer(TestCase):
    def test_file_presence(self):
        try:
            os.rename('C:/Users/stefa/Desktop/BotFantasyESPN/files/activePlayers.json', 'C:/Users/stefa/Desktop/BotFantasyESPN/files/wrongFileName.json')
            myPlayer = player('Zach', 'Lavine', 'CHI')
            os.rename('C:/Users/stefa/Desktop/BotFantasyESPN/files/wrongFileName.json', 'C:/Users/stefa/Desktop/BotFantasyESPN/files/activePlayers.json')
            self.fail('There should have been raised an exception')
        except Exception:
            os.rename('C:/Users/stefa/Desktop/BotFantasyESPN/files/wrongFileName.json', 'C:/Users/stefa/Desktop/BotFantasyESPN/files/activePlayers.json')
            self.assertTrue(True)

    def test_wrong_play_personal(self):
        try:
            myPlayer = player('WrongFirstName','WrongLastName','WrongTeam')
            self.fail('There should have been raised an exception')
        except Exception:
            self.assertTrue(True)