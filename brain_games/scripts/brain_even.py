#!/usr/bin/env python3
from structure_games import structute
from brain_games.games.even import description, even_game


def main():
    structute(even_game, description)


if __name__ == '__main__':
    main()
