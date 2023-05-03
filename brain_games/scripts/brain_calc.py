#!/usr/bin/env python3
from structure_games import structute
from brain_games.games.calc import description, calc


def main():
    structute(calc, description)


if __name__ == '__main__':
    main()
