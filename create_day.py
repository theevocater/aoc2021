#!/usr/bin/env python3
import argparse
import os
import shutil
from typing import List
from typing import Optional
from urllib import request


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        'create a new day in python. '
        'attempts pull token from a file named TOKEN if --token isn\'t passed',
    )
    parser.add_argument('day', help='day for AoC')
    parser.add_argument('--token', help='session token for AoC')
    parser.add_argument('--language', help='session token for AoC')
    args = parser.parse_args()
    day = args.day
    session = args.token

    py_day = f'py_day_{day}'
    if not os.path.exists(py_day):
        os.mkdir(py_day)
        shutil.copy('main.py', os.path.join(py_day, 'part1.py'))
        shutil.copy('main.py', os.path.join(py_day, 'part2.py'))

    if session is None:
        with open('TOKEN') as f:
            session = f.read().strip()

    req = request.Request(
        f'https://adventofcode.com/2020/day/{day}/input',
        headers={'Cookie': f'session={session}'},
    )
    input_file = 'input.txt'
    py_input = os.path.join(py_day, input_file)
    with request.urlopen(req) as r, open(py_input, 'w') as f:
        f.write(r.read().decode('utf-8'))

    return 0


if __name__ == '__main__':
    exit(main())
