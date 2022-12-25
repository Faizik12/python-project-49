#!/usr/bin/env python3
from brain_games.play import launch_the_game
from brain_games.games import gcd


def main():
    launch_the_game(gcd)


if __name__ == '__main__':
    main()
