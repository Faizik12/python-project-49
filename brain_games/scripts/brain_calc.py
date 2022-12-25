#!/usr/bin/env python3
from brain_games.play import launch_the_game
from brain_games.games import calc


def main():
    launch_the_game(calc)


if __name__ == '__main__':
    main()
