"""
Date: 06/06/2021
Name: Rio Weil
Title: model_unittest.py
Description: Testing module for model.py
"""

import unittest
import model
import errors

zero_expcept_wrong = "ZeroException shouldn't be thrown"
bomb_except_wrong = "TooManyBombsException shouldn't be thrown"

class TestTileConstructor(unittest.TestCase):
    def test_constructor_bomb(self):
        test_tile = model.Tile(True)
        self.assertTrue(test_tile.is_bomb)
        self.assertFalse(test_tile.flagged)
        self.assertFalse(test_tile.revealed)

    def test_constructor_notbomb(self):
        test_tile = model.Tile(False)
        self.assertFalse(test_tile.is_bomb)
        self.assertFalse(test_tile.flagged)
        self.assertFalse(test_tile.revealed)

class TestGameStateConstructor(unittest.TestCase):
    def test_constructor_normal(self):
        try:
            test_gamestate = model.GameState(5, 10, 2)
            self.assertEqual(5, test_gamestate.width)
            self.assertEqual(10, test_gamestate.height)
            self.assertEqual(2, test_gamestate.numbombs)
            self.assertFalse(test_gamestate.victory)
            self.assertFalse(test_gamestate.gameover)
        except(errors.ZeroException):
            self.fail(zero_expcept_wrong)
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

    def test_constructor_zerodimensions(self):
        try:
            test_gamestate = model.GameState(0, 0, 10)
            self.fail("ZeroException should have been thrown, but no exception was thrown")
        except(errors.ZeroException):
            pass
        except(errors.TooManyBombsException):
            self.fail("TooManyBombsException was thrown instead of ZeroException")

    def test_constructor_toomanybombs(self):
        try:
            test_gamestate = model.GameState(10, 10, 1000)
            self.fail("TooManyBombsException should have been thrown, but no exception was thrown")
        except(errors.ZeroException):
            self.fail("ZeroException was thrown instead of TooManyBombsException")   
        except(errors.TooManyBombsException):
            pass

class TestCreateBoard(unittest.TestCase):
    def test_1x1_nobomb(self):
        try:
            test_gamestate = model.GameState(1, 1, 0)
            self.assertEqual(1, len(test_gamestate.board))
            self.assertEqual(1, len(test_gamestate.board[0]))
            self.assertFalse(test_gamestate.board[0][0].is_bomb)
        except(errors.ZeroException):
            self.fail(zero_expcept_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)
        
    
    def test_1x1_withbomb(self):
        try:
            test_gamestate = model.GameState(1, 1, 1)
            self.assertEqual(1, len(test_gamestate.board))
            self.assertEqual(1, len(test_gamestate.board[0]))
            self.assertTrue(test_gamestate.board[0][0].is_bomb)
        except(errors.ZeroException):
            self.fail(zero_expcept_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

    def test_large_nobombs(self):
        try:
            test_gamestate = model.GameState(5, 10, 0)
            self.assertEqual(10, len(test_gamestate.board))
            self.assertEqual(5, len(test_gamestate.board[0]))
            for i in range(10):
                for j in range(5):
                    self.assertFalse(test_gamestate.board[i][j].is_bomb)
        except(errors.ZeroException):
            self.fail(zero_expcept_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

    def test_large_allbombs(self):
        try:
            test_gamestate = model.GameState(10, 10, 100)
            self.assertEqual(10, len(test_gamestate.board))
            self.assertEqual(10, len(test_gamestate.board[0]))
            for i in range(10):
                for j in range(10):
                    self.assertTrue(test_gamestate.board[i][j].is_bomb)
        except(errors.ZeroException):
            self.fail(zero_expcept_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

    def test_large_somebombs(self):
        try:
            test_gamestate = model.GameState(10, 5, 25)
            self.assertEqual(5, len(test_gamestate.board))
            self.assertEqual(10, len(test_gamestate.board[0]))
            count = 0
            for i in range(5):
                for j in range(10):
                    if(test_gamestate.board[i][j].is_bomb):
                        count += 1
            self.assertEqual(25, count)
        except(errors.ZeroException):
            self.fail(zero_expcept_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)
            


if __name__ == '__main__':
    unittest.main()
