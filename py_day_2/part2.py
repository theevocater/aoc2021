#!/usr/bin/env python3
import argparse
from typing import List
from typing import Optional


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

    aim = 0
    h_pos = 0
    depth = 0

    for i in inputs:
        direction, amount = i.split(' ')
        if direction == 'down':
            aim += int(amount)
        elif direction == 'up':
            aim -= int(amount)
        elif direction == 'forward':
            h_pos += int(amount)
            depth += aim * int(amount)

    print(f'{depth} * {h_pos} = {depth*h_pos}')

    return 0


if __name__ == '__main__':
    exit(main())
