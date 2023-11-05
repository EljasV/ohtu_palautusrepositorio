import unittest
from statistics_service import StatisticsService
from player import Player


class StatisticsServiceTest(unittest.TestCase):
    def setUp(self):
        self.service = StatisticsService(StubReader())

    def test_search_finds_player(self):
        player = self.service.search("Aaa Aaa")
        self.assertEqual(player.name, "Aaa Aaa")
        self.assertEqual(player.team, "AAA")
        self.assertEqual(player.goals, 1)
        self.assertEqual(player.assists, 1)

    def test_search_finds_nothing(self):
        self.assertIsNone(self.service.search("asdfghjkl"))

    def test_team(self):
        self.assertEqual(len(self.service.team("AAA")), 2)

    def test_top(self):
        top = self.service.top(2)
        self.assertEqual(top[0].name, "Bbb Bbb")
        self.assertEqual(top[1].team, "AAA")


class StubReader:
    def get_players(self):
        return [Player("Aaa Aaa", "AAA", 1, 1), Player("Bbb Bbb", "BB", 2, 1), Player("Eaa Aee", "AAA", 0, 1)]
