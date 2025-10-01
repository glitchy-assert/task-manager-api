#!/usr/bin/env python3
import sys

from _ruff import RuffFormatter


def main():
    args = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "."
    RuffFormatter.format(args)


if __name__ == "__main__":
    main()
