from EasyDesignProblems.TicTacToe.entities.board import Board
from EasyDesignProblems.TicTacToe.entities.player import Player
from EasyDesignProblems.TicTacToe.strategy.winning_strategy import WinningStrategy


class ColumnWinningStrategy(WinningStrategy):
    def check_winner(self, board: Board, player: Player) -> bool:
        for col in range(board.get_size()):
            col_win = True
            for row in range(board.get_size()):
                if board.get_cell(row, col).get_symbol() != player.get_symbol():
                    col_win = False
                    break
            if col_win:
                return True
        return False