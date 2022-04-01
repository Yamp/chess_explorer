import os

from chess import Move, Board
from stockfish import Stockfish

from engines.base import BaseEngine
from engines.book_engine import BookEngine, NoMovesException


class StockfishEngine(BaseEngine):
    """Движок стокфиш."""

    def __init__(
            self,
            use_book: bool = True,
            move_time: int = 1000,
    ):
        super().__init__('stockfish')
        self.use_book = use_book
        self.move_time = move_time
        self.book_engine = BookEngine("book")
        self.stockfish = Stockfish(
            path='/usr/local/bin/stockfish',
            depth=25,
            parameters={
                "Write Debug Log": "false",
                'MultiPV': 1,  # показывать только 1 лучший ход

                # Ресурсы
                'Threads': os.cpu_count(),  # ядра
                'Hash': 1 * 1024,  # память в мб
                'Ponder': True,  # думаем, даже когда сделали ход.

                # Управление временем
                "Move Overhead": 30,  # milliseconds
                "Minimum Thinking Time": 20,
                "Slow Mover": 80,

                # параметры поиска
                'Contempt': 0,
                "Min Split Depth": 0,
                'Skill Level': 20,
                'Use NNUE': True,  # используем нейросетки
                # "SyzygyPath": "C:\\tablebases\\wdl345;C:\\tablebases\\wdl6;D:\\tablebases\\dtz345;D:\\tablebases\\dtz6",

                # ненужные параметры
                # "UCI_AnalyseMode": "false",
                # "UCI_Elo": 1350,
                "UCI_Chess960": "false",
                "UCI_ShowWDL": "false",
                "UCI_LimitStrength": "false",
            },
        )

    def set_board(self, board: Board) -> BaseEngine:
        """Устанавливаем доску."""
        super().set_board(board)
        self.book_engine.set_board(board)
        return self

    def make_move(self, move: Move):
        """Делаем ход"""
        self.stockfish.make_moves_from_current_position([str(move)])
        # self.board.push(move)

    def make_book_move_if_possible(self):
        """Делаем ход из книги, если возможно."""
        if self.use_book:
            try:
                return self.book_engine.get_move()
            except NoMovesException:
                self.use_book = False
                print(f'Дебютные ходы {[str(m) for m in self.board.move_stack]}')
                self.stockfish.make_moves_from_current_position([str(m) for m in self.board.move_stack[:-1]])

        return False

    def get_move(self, time: int = 1000):
        """Получаем лучший ход."""
        move = self.make_book_move_if_possible()
        if move:
            return move

        player_move = self.board.move_stack[-1]

        print(f'Adding player move {player_move}')
        self.stockfish.make_moves_from_current_position([str(player_move)])

        print("Getting stockfish move")
        move = self.stockfish.get_best_move_time(time)

        print(f"Adding stockfish move {move}")
        self.stockfish.make_moves_from_current_position([str(move)])

        print("added")

        return Move.from_uci(move)
