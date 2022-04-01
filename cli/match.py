from game.game import ChessGame


class ChessMatch:
    """Один матч в шахматы."""

    def __init__(
            self,
            black
    ):
        self.game = ChessGame("stockfish")


    def start(self) -> None:
        """Начинаем шахматный матч."""
        # while not self.game.is_finished():



    def read_command(self) -> None:
        """Читаем команду из консоли."""
        command = input("Enter command: ")

    def process_move(
            self,
            sen: str,
    ) -> None:
        """Обрабатываем ход."""
        if sen not in self.game.board.legal_moves:
            raise ValueError(f"{sen} is not a legal move.")

        self.game.play(sen)

    def process_command(self) -> None:
        """Обрабатываем команду."""
