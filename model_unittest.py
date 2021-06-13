"""
Date: 06/06/2021
Name: Rio Weil
Title: model_unittest.py
Description: Testing module for model.py
"""

import unittest
import model
import errors

zero_except_wrong = "ZeroException shouldn't be thrown"
bomb_except_wrong = "TooManyBombsException shouldn't be thrown"
index_except_wrong = "IndexError shouldn't be thrown"

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
            self.fail(zero_except_wrong)
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
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)
        
    
    def test_1x1_withbomb(self):
        try:
            test_gamestate = model.GameState(1, 1, 1)
            self.assertEqual(1, len(test_gamestate.board))
            self.assertEqual(1, len(test_gamestate.board[0]))
            self.assertTrue(test_gamestate.board[0][0].is_bomb)
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
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
            self.fail(zero_except_wrong)  
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
            self.fail(zero_except_wrong)  
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
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)


class TestSetNeighbours(unittest.TestCase):
    def test_1x1_setneighbours(self):
        try:
            test_gamestate = model.GameState(1, 1, 1)
            self.assertEquals(0, test_gamestate.board[0][0].bomb_neighbours)
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

    def test_2x1_setneighbours(self):
        try:
            test_gamestate = model.GameState(2, 1, 1)
            test_gamestate.board = [[model.Tile(True), model.Tile(False)]]
            test_gamestate.set_neighbours()
            self.assertEquals(0, test_gamestate.board[0][0])
            self.assertEquals(1, test_gamestate.board[0][1])
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

    def test_3x3_nobombs_setneighbours(self):
        try:
            test_gamestate = model.GameState(3, 3, 3)
            self.assertFalse(test_gamestate.is_win())
            test_gamestate.board = [[model.Tile(False), model.Tile(False), model.Tile(False)], [model.Tile(False), model.Tile(False), model.Tile(False)], [model.Tile(False), model.Tile(False), model.Tile(False)]]
            self.assertEquals(0, test_gamestate.board[0][0])
            self.assertEquals(0, test_gamestate.board[0][1])
            self.assertEquals(0, test_gamestate.board[0][2])
            self.assertEquals(0, test_gamestate.board[1][0])
            self.assertEquals(0, test_gamestate.board[1][1])
            self.assertEquals(0, test_gamestate.board[1][2])
            self.assertEquals(0, test_gamestate.board[2][0])
            self.assertEquals(0, test_gamestate.board[2][1])
            self.assertEquals(0, test_gamestate.board[2][2])     
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

    def test_3x3_fewbombs_setneighbours(self):
        try:
            test_gamestate = model.GameState(3, 3, 3)
            self.assertFalse(test_gamestate.is_win())
            test_gamestate.board = [[model.Tile(True), model.Tile(False), model.Tile(True)], [model.Tile(False), model.Tile(False), model.Tile(False)], [model.Tile(False), model.Tile(True), model.Tile(False)]]
            self.assertEquals(0, test_gamestate.board[0][0])
            self.assertEquals(2, test_gamestate.board[0][1])
            self.assertEquals(0, test_gamestate.board[0][2])
            self.assertEquals(2, test_gamestate.board[1][0])
            self.assertEquals(3, test_gamestate.board[1][1])
            self.assertEquals(2, test_gamestate.board[1][2])
            self.assertEquals(1, test_gamestate.board[2][0])
            self.assertEquals(0, test_gamestate.board[2][1])
            self.assertEquals(1, test_gamestate.board[2][2])     
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

    def test_3x3_allbombs_setneighbours(self):
        try:
            test_gamestate = model.GameState(3, 3, 3)
            self.assertFalse(test_gamestate.is_win())
            test_gamestate.board = [[model.Tile(True), model.Tile(True), model.Tile(True)], [model.Tile(True), model.Tile(True), model.Tile(True)], [model.Tile(True), model.Tile(True), model.Tile(True)]]
            self.assertEquals(3, test_gamestate.board[0][0])
            self.assertEquals(5, test_gamestate.board[0][1])
            self.assertEquals(3, test_gamestate.board[0][2])
            self.assertEquals(5, test_gamestate.board[1][0])
            self.assertEquals(8, test_gamestate.board[1][1])
            self.assertEquals(5, test_gamestate.board[1][2])
            self.assertEquals(3, test_gamestate.board[2][0])
            self.assertEquals(5, test_gamestate.board[2][1])
            self.assertEquals(3, test_gamestate.board[2][2])     
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)                        


class TestRender(unittest.TestCase):
    def test_1x1_render_noreveal(self):
        try:
            test_gamestate = model.GameState(1, 1, 1)
            self.assertEquals("   1 \n  +-+\n1 | |\n  +-+", test_gamestate.render())
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

    def test_1x1_render_reveal_nobomb(self):
        try:
            test_gamestate = model.GameState(1, 1, 0)
            test_gamestate.check_space(0, 0)
            self.assertEquals("   1 \n  +-+\n1 |0|\n  +-+", test_gamestate.render())
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)  

    def test_1x1_render_reveal_bomb(self):
        try:
            test_gamestate = model.GameState(1, 1, 1)
            test_gamestate.check_space(0, 0)
            self.assertEquals("   1 \n  +-+\n1 |B|\n  +-+", test_gamestate.render())
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong) 

    def test_1x1_render_reveal_flagged(self):
        try:
            test_gamestate = model.GameState(1, 1, 0)
            test_gamestate.set_flag(0, 0)
            self.assertEquals("   1 \n  +-+\n1 |F|\n  +-+", test_gamestate.render())
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

    def test_3x3_render_noreveal(self):
        try:
            test_gamestate = model.GameState(3, 3, 0)
            self.assertEquals("   1 2 3 \n  +-+-+-+\n1 | | | |\n  +-+-+-+\n2 | | | |\n  +-+-+-+\n3 | | | |\n  +-+-+-+", test_gamestate.render())
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

    def test_3x3_render_complex(self):
        try:
            test_gamestate = model.GameState(3, 3, 8)
            test_gamestate.board = [[model.Tile(True), model.Tile(True), model.Tile(True)], [model.Tile(False), model.Tile(False), model.Tile(False)], [model.Tile(True), model.Tile(True), model.Tile(True)]]
            test_gamestate.check_space(1, 0)
            test_gamestate.check_space(1, 1)
            test_gamestate.check_space(1, 2)
            test_gamestate.check_space(2, 0)
            test_gamestate.set_flag(0, 0)
            test_gamestate.set_flag(0, 2)
            test_gamestate.set_flag(2, 1)
            self.assertEquals("   1 2 3 \n  +-+-+-+\n1 |F| |F|\n  +-+-+-+\n2 |4|6|4|\n  +-+-+-+\n3 |B|F| |\n  +-+-+-+", test_gamestate.render())
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

class TestRenderLabelRow(unittest.TestCase):
    def test_1col_label_render(self):
        try:
            test_gamestate = model.GameState(1, 1, 1)
            self.assertEquals("   1 ", test_gamestate.render_label_row())
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

    def test_multicol_label_render(self):
        try:
            test_gamestate = model.GameState(5, 1, 1)
            self.assertEquals("   1 2 3 4 5 ", test_gamestate.render_label_row())
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

    def test_overtencol_label_render(self):
        try:
            test_gamestate = model.GameState(15, 1, 1)
            self.assertEquals("   1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ", test_gamestate.render_label_row())
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)
    
class TestRenderBorderRow(self):
    def test_1col_border_render(self):
        try:
            test_gamestate = model.GameState(1, 1, 1)
            self.assertEquals("  +-+", test_gamestate.render_border_row())
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

    def test_multicol_border_render(self):
        try:
            test_gamestate = model.GameState(5, 1, 1)
            self.assertEquals("  +-+-+-+-+-+", test_gamestate.render_border_row())
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

#TODO
class TestRenderMinefieldRow(self):
    def test_1col_minefield_render_noreveal(self):
        try:
            test_gamestate = model.GameState(1, 1, 1)
            self.assertEquals("1 | |", test_gamestate.render_minefield_row(0))
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

    def test_1col_minefield_render_flag(self):      
        try:
            test_gamestate = model.GameState(1, 1, 1)
            test_game.state.set_flag(0, 0)
            self.assertEquals("1 |F|", test_gamestate.render_minefield_row(0))
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

    def test_1col_minefield_render_bomb(self):  
        try:
            test_gamestate = model.GameState(1, 1, 1)
            test_game.state.check_space(0, 0)
            self.assertEquals("1 |B|", test_gamestate.render_minefield_row(0))
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

    def test_multicol_minefield_render(self):
        try:
            test_gamestate = model.GameState(5, 1, 1)
            test_game.board = [[model.Tile(False), model.Tile(True), model.Tile(False), model.Tile(True), model.Tile(False)]]
            test_game.check_space(0, 0)
            test_game.check_space(0, 2)
            test_game.check_space(0, 4)
            self.assertEquals("1 |1| |2| |1|", test_gamestate.render_minefield_row(0))
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

    def test_10throw_minefield_render(self):
        try:
            test_gamestate = model.Gamestate(1, 10, 0)
            self.assertEquals("10| |", test_gamestate.render_minefield_row(9))      
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

class TestCheckSpace(unittest.TestCase):
    def test_check_space_notin_board(self):
        try:
            test_gamestate = model.GameState(1, 1, 0)
            test_gamestate.check_space(10, 10)
            self.fail("IndexError should have been thrown.")
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)
        except(IndexError):
            pass
        
    def test_1x1_checkspace_nobomb(self):
        try:
            test_gamestate = model.GameState(1, 1, 0)
            test_gamestate.check_space(0, 0)
            self.assertTrue(test_gamestate.board[0][0].revealed)
            self.assertFalse(test_gamestate.gameover)
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)
        except(IndexError):
            self.fail(index_except_wrong)

    def test_1x1_checkspace_withbomb(self):
        try:
            test_gamestate = model.GameState(1, 1, 1)
            test_gamestate.check_space(0, 0)
            self.assertTrue(test_gamestate.board[0][0].revealed)
            self.assertTrue(test_gamestate.gameover)
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)
        except(IndexError):
            self.fail(index_except_wrong)

    def test_3x1_checkspace_revealall(self):
        try:
            test_gamestate = model.GameState(3, 1, 0)
            test_gamestate.check_space(0, 0)
            self.assertTrue(test_gamestate.board[0][0].revealed)
            self.assertTrue(test_gamestate.board[0][1].revealed)
            self.assertTrue(test_gamestate.board[0][2].revealed)
            self.assertFalse(test_gamestate.gameover)
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)
        except(IndexError):
            self.fail(index_except_wrong)

    def test_3x1_checkspace_dont_reveal_bombs(self):
        try:
            test_gamestate = model.GameState(3, 1, 1)
            test_gamestate.board = [[model.Tile(False), model.Tile(False), model.Tile(True)]]
            test_gamestate.check_space(0, 0)
            self.assertTrue(test_gamestate.board[0][0].revealed)
            self.assertTrue(test_gamestate.board[0][1].revealed)
            self.assertFalse(test_gamestate.board[0][2].revealed)
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)
        except(IndexError):
            self.fail(index_except_wrong)
    
    def test_3x3_checkspace_complex(self):
        try:
            test_gamestate = model.GameState(3, 3, 3)
            self.assertFalse(test_gamestate.is_win())
            test_gamestate.board = [[model.Tile(True), model.Tile(False), model.Tile(True)], [model.Tile(False), model.Tile(False), model.Tile(False)], [model.Tile(False), model.Tile(True), model.Tile(False)]]
            test_gamestate.check_space(0, 1)
            test_gamestate.check_space(1, 1)
            self.assertFalse(test_gamestate.board[0][0].revealed)
            self.assertTrue(test_gamestate.board[0][1].revealed)
            self.assertTrue(test_gamestate.board[0][2].revealed)
            self.assertFalse(test_gamestate.board[1][0].revealed)
            self.assertTrue(test_gamestate.board[1][1].revealed)
            self.assertFalse(test_gamestate.board[1][2].revealed)
            self.assertFalse(test_gamestate.board[2][0].revealed)
            self.assertFalse(test_gamestate.board[2][1].revealed)
            self.assertFalse(test_gamestate.board[2][2].revealed)
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)
        except(IndexError):
            self.fail(index_except_wrong)            



class TestSetFlag(unittest.TestCase):
    def test_flag_space_notin_board(self):
        try:
            test_gamestate = model.GameState(1, 1, 0)
            test_gamestate.set_flag(10, 10)
            self.fail("IndexError should have been thrown.")
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)
        except(IndexError):
            pass

    def test_1x1_setflag(self):
        try:
            test_gamestate = model.GameState(1, 1, 1)
            test_gamestate.set_flag(0, 0)
            self.assertTrue(test_gamestate.board[0][0].flagged)
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)  
        except(IndexError):
            self.fail(index_except_wrong)  

    def test_larger_setmultflags(self):
        try:
            test_gamestate = model.GameState(3, 3, 1)
            test_gamestate.set_flag(0, 2)
            test_gamestate.set_flag(1, 0)
            test_gamestate.set_flag(2, 1)
            for i in range(3):
                for j in range(3):
                    if (i == 0 and j == 2) or (i == 1 and j == 0) or (i == 2 and j == 1):
                        self.assertTrue(test_gamestate.board[i][j].flagged)
                    else:
                        self.assertFalse(test_gamestate.board[i][j].flagged)
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)                    
        except(IndexError):
            self.fail(index_except_wrong)  

class TestIsWin(unittest.TestCase):
    def test_1x1_iswin(self):
        try:
            test_gamestate = model.GameState(1, 1, 0)
            self.assertFalse(test_gamestate.is_win())
            test_gamestate.check_space(0, 0)
            self.assertTrue(test_gamestate.is_win())
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

    def test_larger_iswin(self):
        try:
            test_gamestate = model.GameState(3, 3, 3)
            self.assertFalse(test_gamestate.is_win())
            test_gamestate.board = [[model.Tile(True), model.Tile(False), model.Tile(True)], [model.Tile(False), model.Tile(False), model.Tile(False)], [model.Tile(False), model.Tile(True), model.Tile(False)]]
            test_gamestate.check_space(0, 1)
            self.assertFalse(test_gamestate.is_win())
            test_gamestate.check_space(1, 0)
            self.assertFalse(test_gamestate.is_win())
            test_gamestate.check_space(1, 1)
            self.assertFalse(test_gamestate.is_win())   
            test_gamestate.check_space(1, 2)      
            self.assertFalse(test_gamestate.is_win())     
            test_gamestate.check_space(2, 0)    
            self.assertFalse(test_gamestate.is_win())   
            test_gamestate.check_space(2, 2)      
            self.assertTrue(test_gamestate.is_win())           
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

class TestRevealAll(unittest.TestCase):
    def test_1x1_reveal(self):
        try:
            test_gamestate = model.GameState(1, 1, 1)
            test_gamestate.reveal_all()
            self.assertTrue(test_gamestate.board[0][0].revealed)
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

    def test_larger_reveal(self):
        try:
            test_gamestate = model.GameState(5, 5, 10)
            test_gamestate.reveal_all()
            for i in range(5):
                for j in range(5):
                    self.assertTrue(test_gamestate.board[i][j].revealed)
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

    def test_larger_reveal_after_checks(self):
        try:
            test_gamestate = model.GameState(5, 5, 10)
            test_gamestate.check_space(0, 0)
            test_gamestate.check_space(1, 3)
            test_gamestate.reveal_all()
            for i in range(5):
                for j in range(5):
                    self.assertTrue(test_gamestate.board[i][j].revealed)
        except(errors.ZeroException):
            self.fail(zero_except_wrong)  
        except(errors.TooManyBombsException):
            self.fail(bomb_except_wrong)

if __name__ == '__main__':
    unittest.main()
