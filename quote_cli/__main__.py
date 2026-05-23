import argparse
import random
import sys

_QUOTES = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Life is what happens when you’re busy making other plans. – John Lennon",
    "The purpose of our lives is to be happy. – Dalai Lama",
    "Stay hungry, stay foolish. – Steve Jobs",
    "You miss 100% of the shots you don’t take. – Wayne Gretzky",
]


def get_random_quote() -> str:
    """Return a randomly selected quote."""
    return random.choice(_QUOTES)


def list_quotes() -> list[str]:
    """Return the full list of quotes."""
    return list(_QUOTES)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="quote-cli", description="Print a random inspirational quote.")
    parser.add_argument("--list", action="store_true", help="Show all available quotes instead of a random one")
    return parser.parse_args(argv)


def main() -> None:
    args = parse_args()
    if args.list:
        for i, q in enumerate(list_quotes(), 1):
            print(f"{i}. {q}")
    else:
        print(get_random_quote())


if __name__ == "__main__":
    main()
