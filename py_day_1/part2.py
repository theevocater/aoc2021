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

    sums = [0]*(len(inputs)-1)
    for i, inp in enumerate(inputs):
        print(f'{i} {inp}')
        depth = int(inp)
        if i - 2 >= 0:
            sums[i-2] += depth
        if i - 1 >= 0:
            sums[i-1] += depth
        if i < len(inputs) - 1:
            sums[i] += depth

    print(sums)
    previous: Optional[int] = None
    larger = 0
    for depth in sums:
        if previous and depth > previous:
            larger += 1
        previous = depth

    print(larger)

    return 0


if __name__ == '__main__':
    exit(main())
