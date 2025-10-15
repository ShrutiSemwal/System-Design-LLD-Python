from EasyDesignProblems.TicTacToe.entities.player import Player
from EasyDesignProblems.TicTacToe.exceptions.invalid_move_exception import InvalidMoveException
from EasyDesignProblems.TicTacToe.states.game_state import GameState


class WinnerState(GameState):
    def handle_move(self, game, player: Player, row: int, col: int):
        raise InvalidMoveException(f"Game is already over. {game.get_winner().get_name()} has won.")