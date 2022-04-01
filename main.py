import random



def play_game(
        p1_name: str,
        p2_name: str,
        p1_type: str = "human",
        p2_type: str = "engine",
        randomize_colors: bool = False,
):
    """Играем игру."""
    if randomize_colors and random.random() < 0.5:
        p1_name, p1_type, p2_name, p2_type = p2_name, p2_type, p1_name, p1_type

    if p1_type == "engine":
        p1 = Eng


def main():
    ...


if __name__ == '__main__':
    main()
