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

    previous: Optional[int] = None
    larger = 0
    for i in inputs:
        print(i)
        depth = int(i)
        if previous and depth > previous:
            larger += 1
        previous = depth

    print(larger)

    return 0


if __name__ == '__main__':
    exit(main())
