#!/usr/bin/env python3
"""
Rock–Paper–Scissors CLI bot.

Usage
-----
$ python rps_bot.py          # play until you press Q
$ python -m pytest           # run unit tests (see tests/ folder)

Features
--------
* Robust input parsing (R/P/S or full words, case-insensitive)
* Graceful quit with “Q” / “quit”
* Running score tallied across rounds
* Dramatic 0.3-second pause before the bot reveals its move
"""

from __future__ import annotations

import random
import sys
import time
from enum import Enum, auto


class Move(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

    @staticmethod
    def from_user_input(label: str) -> "Move":
        mapping = {
            "r": Move.ROCK,
            "rock": Move.ROCK,
            "p": Move.PAPER,
            "paper": Move.PAPER,
            "s": Move.SCISSORS,
            "scissors": Move.SCISSORS,
        }
        key = label.strip().lower()

        if key in {"q", "quit"}:
            raise KeyboardInterrupt  # bubble up for clean exit

        if key not in mapping:
            raise ValueError("❌  Invalid choice — enter R, P, S or Q to quit.")
        return mapping[key]

    def beats(self, other: "Move") -> bool:
        return (
            (self == Move.ROCK and other == Move.SCISSORS)
            or (self == Move.PAPER and other == Move.ROCK)
            or (self == Move.SCISSORS and other == Move.PAPER)
        )

    def __str__(self) -> str:  # pretty print
        return self.name.title()


def play() -> None:
    wins = losses = ties = 0
    choices = tuple(Move)

    try:
        while True:
            try:
                user_move = Move.from_user_input(
                    input("Your move [R/P/S or Q to quit]: ")
                )
            except ValueError as err:
                print(err)
                continue

            ai_move = random.choice(choices)
            time.sleep(0.3)
            print(f"🤖  I choose {ai_move}!")

            if user_move == ai_move:
                result = "It's a tie."
                ties += 1
            elif user_move.beats(ai_move):
                result = "You win! 🎉"
                wins += 1
            else:
                result = "I win! 😈"
                losses += 1

            print(f"— {result}\n")

    except KeyboardInterrupt:
        # User pressed Q or Ctrl-C
        print("\nGood game! Final score:")
        print(f"  You   : {wins}")
        print(f"  Me    : {losses}")
        print(f"  Ties  : {ties}")
        print("Bye 👋")
        sys.exit(0)


if __name__ == "__main__":
    play()
