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

    depth = 0
    h_pos = 0

    for i in inputs:
        direction, amount = i.split(' ')
        if direction == 'forward':
            h_pos += int(amount)
        elif direction == 'down':
            depth += int(amount)
        elif direction == 'up':
            depth -= int(amount)

    print(f'{depth} * {h_pos} = {depth*h_pos}')

    return 0


if __name__ == '__main__':
    exit(main())
