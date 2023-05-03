#!/usr/bin/env python3
from structure_games import structute
from brain_games.games.calc import description, calc_game


def main():
    structute(calc_game, description)


if __name__ == '__main__':
    main()
