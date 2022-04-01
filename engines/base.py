from __future__ import annotations

from abc import abstractmethod, ABC

from chess import Board, Move


class BaseEngine(ABC):
    """Базовый класс для движков."""

    def __init__(
            self,
            name: str,
    ):
        self.name = name
        self.board = None

    def set_board(
            self,
            board: Board,
    ) -> BaseEngine:
        """Ставим доску"""
        self.board = board
        return self

    @abstractmethod
    def get_move(self):
        """Получаем ход игрока."""
        pass
