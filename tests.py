import argparse
import json
import unittest

from board import Board


# *********************************************************************************************
# ******************** Test  different input output  scenario *********************************
# *********************************************************************************************
from state import State


class ValidateKnightPickedScore(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = Board()

    # validate the item is picked by knight updated knight score scenario
    def test_validate_knight_picked_items_and_score(self):
        game = Board()
        input_ = [
            "R:S",
            "R:S",
            "R:E",
            "R:E",
        ]
        for _in in input_:
            name, direction = _in.split(":")
            game.read_input(knight=name, direction=direction)
        actual = {
            "red": [
                [
                    2,
                    2
                ],
                "LIVE",
                "A",
                3,
                1
            ],
            "blue": [
                [
                    7,
                    0
                ],
                "LIVE",
                None,
                1,
                1
            ],
            "green": [
                [
                    7,
                    7
                ],
                "LIVE",
                None,
                1,
                1
            ],
            "yellow": [
                [
                    0,
                    7
                ],
                "LIVE",
                None,
                1,
                1
            ],
            "magic_staff": [
                [
                    5,
                    2
                ],
                False
            ],
            "helmet": [
                [
                    5,
                    5
                ],
                False
            ],
            "dagger": [
                [
                    2,
                    5
                ],
                False
            ],
            "axe": [
                [
                    2,
                    2
                ],
                True
            ]
        }
        self.assertDictEqual(game.output(), actual)

    # validate that knights move rightly in mentioned directions scenario
    def test_validate_knight(self):
        game = Board()
        input_ = [
            'R:E',
            'Y:W',
            'B:E',
            'G:W',
        ]
        for _in in input_:
            name, direction = _in.split(":")
            game.read_input(name, direction)
        actual = {
            "red": [
                [
                    0,
                    1
                ],
                "LIVE",
                None,
                1,
                1
            ],
            "blue": [
                [
                    7,
                    1
                ],
                "LIVE",
                None,
                1,
                1
            ],
            "green": [
                [
                    7,
                    6
                ],
                "LIVE",
                None,
                1,
                1
            ],
            "yellow": [
                [
                    0,
                    6
                ],
                "LIVE",
                None,
                1,
                1
            ],
            "magic_staff": [
                [
                    5,
                    2
                ],
                False
            ],
            "helmet": [
                [
                    5,
                    5
                ],
                False
            ],
            "dagger": [
                [
                    2,
                    5
                ],
                False
            ],
            "axe": [
                [
                    2,
                    2
                ],
                False
            ]
        }

        self.assertDictEqual(game.output(), actual)

    # validate state after died and check weather item dropped or not scenario
    def test_validate_knight_fight_item_drop(self):
        game = Board()
        input_ = [
            'R:S',
            'R:S',
            'R:E',
            'R:E',
            'R:S',
            'B:N',
            'B:N',
            'B:E',
            'B:E',
            'B:N',
            'R:S',
            'R:W',
        ]

        for _in in input_:
            name, direction = _in.split(":")
            game.read_input(name, direction)
        actual = {
            "red": [
                [
                    4,
                    1
                ],
                "LIVE",
                "A",
                3,
                1
            ],
            "blue": [
                [
                    4,
                    2
                ],
                "DEAD",
                None,
                0,
                0
            ],
            "green": [
                [
                    7,
                    7
                ],
                "LIVE",
                None,
                1,
                1
            ],
            "yellow": [
                [
                    0,
                    7
                ],
                "LIVE",
                None,
                1,
                1
            ],
            "magic_staff": [
                [
                    4,
                    2
                ],
                False
            ],
            "helmet": [
                [
                    5,
                    5
                ],
                False
            ],
            "dagger": [
                [
                    2,
                    5
                ],
                False
            ],
            "axe": [
                [
                    4,
                    1
                ],
                True
            ]
        }
        self.assertDictEqual(game.output(), actual)

    # *********************************************************************************************
    # ************************** Test each function as Unit ***************************************
    # *********************************************************************************************

    def test_validate_is_alive_function(self):
        self.assertEqual(self.game.knights["R"].is_live(), True)
        self.game.knights["R"].state = State.Dead
        self.assertEqual(self.game.knights["R"].is_live(), False)

    def test_validate_is_defended(self):
        self.game.knights["R"].score.attack = 3
        self.game.knights["B"].score.defence = 2
        self.assertEqual(self.game.knights["R"].is_winner(self.game.knights["B"]), True)
        self.game.knights["G"].score.attack = 3
        self.game.knights["Y"].score.defence = 5
        self.assertEqual(self.game.knights["G"].is_winner(self.game.knights["Y"]), False)

    def test_acquire_item(self):
        self.game.knights["R"].position.x, self.game.knights["R"].position.y = [3, 3]
        self.game.items["M"].position.x, self.game.items["M"].position.y = [3, 3]
        self.game.validate_fight_and_item("R")
        self.assertEqual(self.game.items["M"].acquired_by, self.game.knights["R"])

    def test_has_fight_attacker(self):
        self.game.knights["R"].position.x, self.game.knights["R"].position.y = [5, 5]
        self.game.knights["G"].position.x, self.game.knights["G"].position.y = [5, 5]
        self.game.knights["R"].score.attack = 3
        self.game.knights["G"].score.defence = 2
        self.game.validate_fight_and_item("R")
        self.assertEqual(self.game.knights["G"].state, State.Dead)
        self.assertEqual(self.game.knights["G"].score.attack, 0)
        self.assertEqual(self.game.knights["G"].score.defence, 0)

    def test_drop_item_has_item(self):
        # set mock values
        self.game.items["H"].acquired_by = self.game.knights["Y"]
        self.game.knights["Y"].item = self.game.items["H"]
        # Test function
        self.game.knights["Y"].drop_item(State.Dead)
        self.assertEqual(self.game.knights["Y"].item, None)
        self.assertEqual(self.game.knights["Y"].does_not_has_item(), True)

    def test_move_function(self):
        self.game.read_input(knight="R", direction="E")
        self.game.read_input(knight="B", direction="E")
        self.game.read_input(knight="G", direction="N")
        self.game.read_input(knight="Y", direction="W")
        self.assertListEqual([self.game.knights["R"].position.x, self.game.knights["R"].position.y], [0, 1])
        self.assertListEqual([self.game.knights["B"].position.x, self.game.knights["B"].position.y], [7, 1])
        self.assertListEqual([self.game.knights["G"].position.x, self.game.knights["G"].position.y], [6, 7])
        self.assertListEqual([self.game.knights["Y"].position.x, self.game.knights["Y"].position.y], [0, 6])
