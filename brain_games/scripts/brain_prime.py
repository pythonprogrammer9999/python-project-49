#!/usr/bin/env python3
from structure_games import structute
from brain_games.games.prime import description, prime_game


def main():
    structute(prime_game, description)


if __name__ == '__main__':
    main()
