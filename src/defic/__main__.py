import sys
from .lib import csv


def read_stdin() -> list[str]:
    return [line for line in sys.stdin]


def main() -> None:
    pass


# i don't think this is necessary in this one specific case (see file name) but let's honor the convention
if __name__ == "__main__":
    main()
