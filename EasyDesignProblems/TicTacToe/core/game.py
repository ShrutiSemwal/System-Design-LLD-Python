"""
Summary of Core Entities:

-->Board: Represents the 3x3 game grid. Manages a 2D matrix of cells and provides methods to update cell values, validate positions, and check for win or draw conditions.
-->Cell: Represents an individual square on the board. Each cell can either be empty or contain a symbol (X or O).
-->Player: Represent a player with a symbol and optionally a name or ID.
-->Symbol: Represents the value a cell can hold—X, O, or EMPTY.
-->Game: Controls the overall game flow. Alternates turns, validates moves, updates the board, and checks for winning or draw conditions.
-->GameStatus: Represents the current state of the game. Possible values include IN_PROGRESS, DRAW, WINNER_X, and WINNER_O.
-->Scoreboard: Tracks cumulative scores and outcomes across multiple game sessions.
-->TicTacToeSystem: Orchestrates the creation of games and ties together core components like the scoreboard and game engine.

Implementation / Inheritance ("is-a"):
-->Game --|> GameSubject: Game is a subject that can be observed.
-->Scoreboard --|> GameObserver: Scoreboard is an observer that listens to Game events.
-->RowWinningStrategy, ColumnWinningStrategy, DiagonalWinningStrategy --|> WinningStrategy: These are concrete implementations of the winning strategy contract.
-->InProgressState, WinnerState, DrawState --|> GameState: These are concrete implementations of the game state contract.

Key Design Patterns:
-->Strategy Pattern
-->State Pattern
-->Observer Pattern- The Game (Subject) and Scoreboard (Observer)
-->Facade Pattern- TicTacToeSystem acts as a facade
-->Singleton Pattern- TicTacToeSystem class is implemented as a singleton to ensure a single, globally accessible entry point to the system
"""

from EasyDesignProblems.TicTacToe.entities.board import Board
from EasyDesignProblems.TicTacToe.entities.player import Player
from EasyDesignProblems.TicTacToe.enums.game_status import GameStatus
from EasyDesignProblems.TicTacToe.observer.game_subject import GameSubject
from EasyDesignProblems.TicTacToe.states.game_state import GameState
from EasyDesignProblems.TicTacToe.states.in_progress_state import InProgressState
from EasyDesignProblems.TicTacToe.strategy.column_winning_strategy import ColumnWinningStrategy
from EasyDesignProblems.TicTacToe.strategy.diagonal_winning_strategy import DiagonalWinningStrategy
from EasyDesignProblems.TicTacToe.strategy.row_winning_strategy import RowWinningStrategy


class Game(GameSubject):
    def __init__(self, player1: Player, player2: Player):
        super().__init__()
        self.board = Board(3)
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1  # Player 1 starts
        self.winner = None
        self.status = GameStatus.IN_PROGRESS
        self.state = InProgressState()
        self.winning_strategies = [
            RowWinningStrategy(),
            ColumnWinningStrategy(),
            DiagonalWinningStrategy()
        ]
    
    def make_move(self, player: Player, row: int, col: int):
        self.state.handle_move(self, player, row, col)
    
    def check_winner(self, player: Player) -> bool:
        for strategy in self.winning_strategies:
            if strategy.check_winner(self.board, player):
                return True
        return False
    
    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
    
    def get_board(self):
        return self.board
    
    def get_current_player(self):
        return self.current_player
    
    def get_winner(self):
        return self.winner
    
    def set_winner(self, winner: Player):
        self.winner = winner
    
    def get_status(self):
        return self.status
    
    def set_state(self, state: GameState):
        self.state = state
    
    def set_status(self, status: GameStatus):
        self.status = status
        # Notify observers when the status changes to a finished state
        if status != GameStatus.IN_PROGRESS:
            self.notify_observers()