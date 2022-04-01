from chess import Board, Move

from engines.base import BaseEngine


class HumanPlayer(BaseEngine):
    """Человечий игрок."""

    def __init__(
            self,
            name: str,
    ):
        super().__init__(name)

    def get_move(self) -> Move:
        """Получаем ход."""
        return Move.from_uci(input('>'))
