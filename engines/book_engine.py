from operator import attrgetter
from os import PathLike
from pathlib import Path

import chess
import chess.polyglot
from chess import Move

from engines.base import BaseEngine

DEFAULT_BOOK: Path = (Path(__file__).parent.parent / "data" / "openings" / "Perfect2021.bin").absolute()


class NoMovesException(Exception):
    """Выбрасывается, если нет больше ходов в книге."""
    pass


class BookEngine(BaseEngine):
    """Движок, который играет по дебютной книге."""

    def __init__(
            self,
            name: str,
            path: PathLike = DEFAULT_BOOK,
    ):
        super().__init__(name)

        self.path = path
        self.reader = chess.polyglot.open_reader(self.path)

    def get_move(self) -> Move:
        """Получаем книжный ход."""
        entries = list(self.reader.find_all(self.board))
        if not entries:
            raise NoMovesException

        return max(entries, key=attrgetter('weight')).move
