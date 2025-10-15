from EasyDesignProblems.TicTacToe.entities.board import Board
from EasyDesignProblems.TicTacToe.entities.player import Player
from EasyDesignProblems.TicTacToe.strategy.winning_strategy import WinningStrategy


class DiagonalWinningStrategy(WinningStrategy):
    def check_winner(self, board: Board, player: Player) -> bool:
        # Main diagonal
        main_diag_win = True
        for i in range(board.get_size()):
            if board.get_cell(i, i).get_symbol() != player.get_symbol():
                main_diag_win = False
                break
        if main_diag_win:
            return True
        
        # Anti-diagonal
        anti_diag_win = True
        for i in range(board.get_size()):
            if board.get_cell(i, board.get_size() - 1 - i).get_symbol() != player.get_symbol():
                anti_diag_win = False
                break
        return anti_diag_win