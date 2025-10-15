from EasyDesignProblems.TicTacToe.entities.player import Player
from EasyDesignProblems.TicTacToe.enums.game_status import GameStatus
from EasyDesignProblems.TicTacToe.enums.symbol import Symbol
from EasyDesignProblems.TicTacToe.exceptions.invalid_move_exception import InvalidMoveException
from EasyDesignProblems.TicTacToe.states.draw_state import DrawState
from EasyDesignProblems.TicTacToe.states.game_state import GameState
from EasyDesignProblems.TicTacToe.states.winner_state import WinnerState


class InProgressState(GameState):
    def handle_move(self, game, player: Player, row: int, col: int):
        if game.get_current_player() != player:
            raise InvalidMoveException("Not your turn!")
        
        # Place the piece on the board
        game.get_board().place_symbol(row, col, player.get_symbol())
        
        # Check for a winner or a draw
        if game.check_winner(player):
            game.set_winner(player)
            game.set_status(GameStatus.WINNER_X if player.get_symbol() == Symbol.X else GameStatus.WINNER_O)
            game.set_state(WinnerState())
        elif game.get_board().is_full():
            game.set_status(GameStatus.DRAW)
            game.set_state(DrawState())
        else:
            # If the game is still in progress, switch players
            game.switch_player()