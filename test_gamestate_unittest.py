import unittest
import gamestate

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
    def test_constructor(self):
        test_gamestate = gamestate.GameState(5, 10, 2)
        self.assertEqual(5, test_gamestate.width)
        self.assertEqual(10, test_gamestate.height)
        self.assertEqual(2, test_gamestate.numbombs)
        self.assertFalse(test_gamestate.victory)
        self.assertFalse(test_gamestate.gameover)

if __name__ == '__main__':
    unittest.main()
