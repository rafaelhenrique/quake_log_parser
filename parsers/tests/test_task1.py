# from mock import patch
import os

import pytest

from parsers.task1 import parse_game_kills, parse_kill_line


class TestTask1:
    """
    Run tests on task1 parser
    """

    @pytest.fixture
    def task1_logfile(self):
        logfile = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'fixtures',
            'task1.log')
        return logfile

    def setup(self):
        pass

    def test_parse_game_kills(self, task1_logfile):
        parsed_dict = dict(parse_game_kills(task1_logfile))
        assert parsed_dict == {
            'game1': {
                'total_kills': 11,
                'kills': {
                    'Mocinha': 1,
                    'Isgalamido': 2
                },
                'players': ['Isgalamido', 'Mocinha']
            },
            'game2': {
                'total_kills': 4,
                'kills': {'Mocinha': 1},
                'players': ['Isgalamido', 'Mocinha', 'Zeh', 'Dono da Bola']
            }
        }

    def test_parse_kill_line(self):
        game_match = {
            "total_kills": 0,
            "players": [],
            "kills": {}
        }
        line = ("20:54 Kill: 1022 2 22: <world> killed Isgalamido "
                "by MOD_TRIGGER_HURT")
        parse_kill_line(line, game_match)
        assert game_match == {'kills': {}, 'players': ['Isgalamido'],
                              'total_kills': 1}

        line = ("22:06 Kill: 2 3 7: Isgalamido killed Mocinha by "
                "MOD_ROCKET_SPLASH")
        parse_kill_line(line, game_match)
        assert game_match == {'kills': {'Mocinha': 1}, 'total_kills': 2,
                              'players': ['Isgalamido', 'Mocinha']}
