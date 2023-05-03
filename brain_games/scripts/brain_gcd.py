#!/usr/bin/env python3
from structure_games import structute
from brain_games.games.gcd import description, gcd_game


def main():
    structute(gcd_game, description)


if __name__ == '__main__':
    main()
