from abc import ABC, abstractmethod
from EasyDesignProblems.TicTacToe.entities.board import Board
from EasyDesignProblems.TicTacToe.entities.player import Player


class WinningStrategy(ABC):
    @abstractmethod
    def check_winner(self, board: Board, player: Player) -> bool:
        pass