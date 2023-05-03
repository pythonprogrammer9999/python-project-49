#!/usr/bin/env python3
from structure_games import structute
from brain_games.games.progression import description, progression_game


def main():
    structute(progression_game, description)


if __name__ == '__main__':
    main()
