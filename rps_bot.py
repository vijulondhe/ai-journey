import random
from enum import Enum, auto


class Move(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

    @staticmethod
    def from_str(label: str):
        label = label.strip().lower()
        mapping = {"r": Move.ROCK, "rock": Move.ROCK,
                   "p": Move.PAPER, "paper": Move.PAPER,
                   "s": Move.SCISSORS, "scissors": Move.SCISSORS}
        if label not in mapping:
            raise ValueError("Choose R, P, or S")
        return mapping[label]

    def beats(self, other: "Move") -> bool:
        return (
            (self == Move.ROCK and other == Move.SCISSORS) or
            (self == Move.PAPER and other == Move.ROCK) or
            (self == Move.SCISSORS and other == Move.PAPER)
        )


def main() -> None:
    choices = list(Move)
    while True:
        try:
            user_move = Move.from_str(input("Your move [R/P/S or Q to quit]: "))
        except ValueError as e:
            if str(e).startswith("Choose"):
                print(e)
                continue
            break  # Q pressed
        ai_move = random.choice(choices)
        print(f"I choose {ai_move.name.title()}.")

        if user_move == ai_move:
            print("— It's a tie!\n")
        elif user_move.beats(ai_move):
            print("— You win! 🎉\n")
        else:
            print("— I win! 😈\n")


if __name__ == "__main__":
    main()
