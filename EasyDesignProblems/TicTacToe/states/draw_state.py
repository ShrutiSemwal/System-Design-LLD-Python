from EasyDesignProblems.TicTacToe.entities.player import Player
from EasyDesignProblems.TicTacToe.exceptions.invalid_move_exception import InvalidMoveException
from EasyDesignProblems.TicTacToe.states.game_state import GameState


class DrawState(GameState):
    def handle_move(self, game, player: Player, row: int, col: int):
        raise InvalidMoveException("Game is already over. It was a draw.")