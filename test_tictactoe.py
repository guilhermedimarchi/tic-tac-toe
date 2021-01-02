from unittest import TestCase
from tictactoe import *

class Test(TestCase):

    BOARD_EMPTY = [[EMPTY, EMPTY, EMPTY],
                   [EMPTY, EMPTY, EMPTY],
                   [EMPTY, EMPTY, EMPTY]]

    BOARD_WITH_ONE_MOVE = [[EMPTY, EMPTY,  EMPTY],
                           [EMPTY, X,      EMPTY],
                           [EMPTY, EMPTY,  EMPTY]]

    BOARD_WITH_TWO_MOVES = [[EMPTY, EMPTY,  O],
                            [EMPTY, X,      EMPTY],
                            [EMPTY, EMPTY,  EMPTY]]

    BOARD_DRAW = [[O, X, O],
                 [O, X, X],
                 [X, O, X]]

    BOARD_O_WON = [[O, EMPTY, X],
                   [O, X, EMPTY],
                   [O, EMPTY, X]]

    BOARD_X_WON = [[X, EMPTY, EMPTY],
                   [O, X, EMPTY],
                   [O, EMPTY, X]]

    def test_player_empty_board(self):
        self.assertEqual(X, player(self.BOARD_EMPTY))

    def test_player_O_turn(self):
        self.assertEqual(O, player(self.BOARD_WITH_ONE_MOVE))

    def test_player_X_turn(self):
        self.assertEqual(X, player(self.BOARD_WITH_TWO_MOVES))

    def test_actions_empty_board(self):
        expected = [(0, 0), (0, 1), (0, 2),
                    (1, 0), (1, 1), (1, 2),
                    (2, 0), (2, 1), (2, 2)]
        self.assertEqual(expected, actions(self.BOARD_EMPTY))

    def test_actions_after_with_move(self):
        expected = [(0, 0), (0, 1), (0, 2),
                    (1, 0),         (1, 2),
                    (2, 0), (2, 1), (2, 2)]
        self.assertEqual(expected, actions(self.BOARD_WITH_ONE_MOVE))

    def test_actions_after_with_two_moves(self):
        expected = [(0, 0), (0, 1),
                    (1, 0),         (1, 2),
                    (2, 0), (2, 1), (2, 2)]
        self.assertEqual(expected, actions(self.BOARD_WITH_TWO_MOVES))

    def test_result_empty_board(self):
        actual = [[EMPTY, EMPTY,  EMPTY],
                  [EMPTY, X,      EMPTY],
                  [EMPTY, EMPTY,  EMPTY]]
        self.assertEqual(actual, result(self.BOARD_EMPTY, (1, 1)))

    def test_result_O_turn(self):
        actual = [[EMPTY, EMPTY,  O],
                  [EMPTY, X,      EMPTY],
                  [EMPTY, EMPTY,  EMPTY]]
        self.assertEqual(actual, result(self.BOARD_WITH_ONE_MOVE, (0, 2)))

    def test_result_invalid_action(self):
        with self.assertRaises(Exception):
            result(self.BOARD_EMPTY, (3, 0))
            result(self.BOARD_EMPTY, (-1, 0))
            result(self.BOARD_EMPTY, (0, 3))
            result(self.BOARD_EMPTY, (0, -1))

    def test_winner_no_winner(self):
        self.assertEqual(None, winner(self.BOARD_EMPTY))

    def test_winner_row_winner(self):
        board = [[X, X, X],
                 [EMPTY, O, EMPTY],
                 [O, O, X]]
        self.assertEqual(X, winner(board))

    def test_winner_col_winner(self):
        board = [[O, EMPTY, X],
                 [O, X, EMPTY],
                 [O, EMPTY, X]]
        self.assertEqual(O, winner(board))

    def test_winner_diagonal_winner(self):
        board = [[X, EMPTY, EMPTY],
                 [O, X, EMPTY],
                 [O, EMPTY, X]]
        self.assertEqual(X, winner(board))

    def test_winner_anti_diagonal_winner(self):
        board = [[EMPTY, EMPTY, X],
                 [EMPTY, X, O],
                 [X, EMPTY, O]]
        self.assertEqual(X, winner(board))

    def test_winner_draw(self):
        self.assertEqual(None, winner(self.BOARD_DRAW))

    def test_terminal(self):
        self.assertFalse(terminal(self.BOARD_EMPTY))
        self.assertTrue(terminal(self.BOARD_X_WON))
        self.assertTrue(terminal(self.BOARD_DRAW))

    def test_utility(self):
        self.assertEqual(1, utility(self.BOARD_X_WON))
        self.assertEqual(-1, utility(self.BOARD_O_WON))
        self.assertEqual(0, utility(self.BOARD_DRAW))






