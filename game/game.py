from chess import Board, Move

from engines.base import BaseEngine
from engines.book_engine import BookEngine
from engines.human_player import HumanPlayer

from engines.stockfish_engine import StockfishEngine


class IllegalMove(Exception):
    """Неверный ход."""
    pass


class ChessGame:
    """Интерфейс для игры в шахматы."""

    def __init__(
            self,
            p1: BaseEngine,
            p2: BaseEngine,
            board: Board = Board(),
    ):
        self.board = board

        self.p1 = p1.set_board(board)
        self.p2 = p2.set_board(board)

    def play(
            self,
    ) -> None:
        """Играем партию."""
        p_cur, p_next = self.p1, self.p2

        while not self.board.is_game_over():
            try:
                print(p_cur.name, "is thinking...")
                self.make_move(p_cur.get_move())
                p_cur, p_next = p_next, p_cur
            except IllegalMove as e:
                print(e)

    def make_move(self, move: Move) -> None:
        """Делаем ход."""
        if move not in self.board.legal_moves:
            raise IllegalMove(f"{move} is not legal.")

        self.board.push(move)
        self.print_unicode()

    def pop(self) -> None:
        """Удаляет последний ход."""
        self.board.pop()

    def print_board(self) -> None:
        """Выводит доску."""
        print(self.board)

    def print_unicode(self) -> None:
        """Печатаем доску unicode символами."""
        print(self.board.unicode(
            invert_color=False,
            borders=True,
            empty_square=' ',
        ))


def main():
    """Тестируем ChessGame."""
    b = Board()

    e1 = StockfishEngine(
        use_book=True,
        move_time=60 * 1000,
    )
    e2 = HumanPlayer('player')

    game = ChessGame(e1, e2, board=b)
    game.play()


if __name__ == '__main__':
    main()
