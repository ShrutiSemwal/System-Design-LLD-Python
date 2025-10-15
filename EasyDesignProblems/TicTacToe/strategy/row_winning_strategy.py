from EasyDesignProblems.TicTacToe.entities.board import Board
from EasyDesignProblems.TicTacToe.entities.player import Player
from EasyDesignProblems.TicTacToe.strategy.winning_strategy import WinningStrategy


class RowWinningStrategy(WinningStrategy):
    def check_winner(self, board: Board, player: Player) -> bool:
        for row in range(board.get_size()):
            row_win = True
            for col in range(board.get_size()):
                if board.get_cell(row, col).get_symbol() != player.get_symbol():
                    row_win = False
                    break
            if row_win:
                return True
        return False