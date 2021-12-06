#!/usr/bin/env python3
import argparse
from typing import List
from typing import Optional


def print_board(board: List[str]) -> None:
    i = 0
    while i < len(board):
        print('\t'.join(board[i:i+5]))
        i += 5
    print()


def mark_matches(num: str, board: List[str]) -> None:
    for i in range(len(board)):
        if board[i] == num:
            board[i] = 'm'


def calc_board(board: List[str]) -> int:
    return sum(int(b) for b in board if b != 'm')


def find_match(board: List[str]) -> Optional[int]:
    i = 0
    while i < 5:
        # ith row
        row = board[i*5:i*5+5]
        print(row)
        if len(list(filter(lambda y: y != 'm', row))) == 0:
            return calc_board(board)

        # try the ith column
        col = board[i::5]
        print(col)
        if len(list(filter(lambda y: y != 'm', col))) == 0:
            return calc_board(board)

        i += 1

    return None


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input', nargs='?', default='input.txt',
        help='input file to read',
    )
    args = parser.parse_args()

    inputs = []
    with open(args.input) as f:
        inputs = [line.rstrip() for line in f]

    numbers = inputs[0].split(',')
    print(numbers)

    board_size = 5

    boards: List[List[str]] = []

    i = 2
    while i < len(inputs[2:]):
        board = []
        for row in inputs[i:i+board_size]:
            board += row.split()

        boards.append(board)
        i += 6

    for board in boards:
        print_board(board)

    # mark boards
    for num in numbers:
        print(f'marking {num}')
        for i in range(len(boards)):
            board = boards[i]
            if board == []:
                continue
            mark_matches(num, board)
            print_board(board)
            match = find_match(board)
            if match is not None:
                print(
                    f'board {i} complete: {match} * {num} = {match*int(num)}',
                )
                if len(boards) == 1:
                    return 0
                else:
                    boards[i] = []

    return 0


if __name__ == '__main__':
    exit(main())
