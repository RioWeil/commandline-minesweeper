"""
Date: 06/06/2021
Name: Rio Weil
Title: gamestate_unittest.py
Description: Testing module for gamestate.py
"""

import unittest
import gamestate
import errors

class TestTileConstructor(unittest.TestCase):
    def test_constructor_bomb(self):
        test_tile = gamestate.Tile(True)
        self.assertTrue(test_tile.is_bomb)
        self.assertFalse(test_tile.flagged)
        self.assertFalse(test_tile.revealed)

    def test_constructor_notbomb(self):
        test_tile = gamestate.Tile(False)
        self.assertFalse(test_tile.is_bomb)
        self.assertFalse(test_tile.flagged)
        self.assertFalse(test_tile.revealed)

class TestGameStateConstructor(unittest.TestCase):
    def test_constructor_normal(self):
        try:
            test_gamestate = gamestate.GameState(5, 10, 2)
            self.assertEqual(5, test_gamestate.width)
            self.assertEqual(10, test_gamestate.height)
            self.assertEqual(2, test_gamestate.numbombs)
            self.assertFalse(test_gamestate.victory)
            self.assertFalse(test_gamestate.gameover)
        except(errors.ZeroException):
            self.fail("ZeroException shouldn't be thrown")
        except(errors.TooManyBombsException):
            self.fail("TooManyBombsException shouldn't be thrown")

    def test_constructor_zerodimensions(self):
        try:
            test_gamestate = gamestate.GameState(0, 0, 10)
            self.fail("ZeroException should have been thrown, but no exception was thrown")
        except(errors.ZeroException):
            pass
        except(errors.TooManyBombsException):
            self.fail("TooManyBombsException was thrown instead of ZeroException")

    def test_constructor_zerobombs(self):
        try:
            test_gamestate = gamestate.GameState(10, 10, 0)
            self.fail("ZeroException should have been thrown, but no exception was thrown")
        except(errors.ZeroException):
            pass
        except(errors.TooManyBombsException):
            self.fail("TooManyBombsException was thrown instead of ZeroException")

    def test_constructor_toomanybombs(self):
        try:
            test_gamestate = gamestate.GameState(10, 10, 0)
            self.fail("TooManyBombsException should have been thrown, but no exception was thrown")
        except(errors.ZeroException):
            self.fail("ZeroException was thrown instead of TooManyBombsException")   
        except(errors.TooManyBombsException):
            pass

if __name__ == '__main__':
    unittest.main()
