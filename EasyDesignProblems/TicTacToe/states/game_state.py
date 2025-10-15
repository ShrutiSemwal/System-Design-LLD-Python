from abc import ABC, abstractmethod
from EasyDesignProblems.TicTacToe.entities.player import Player


class GameState(ABC):
    @abstractmethod
    def handle_move(self, game, player: Player, row: int, col: int):
        pass