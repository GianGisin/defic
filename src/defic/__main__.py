import sys
from .lib import csv


def read_stdin() -> list[str]:
    return [line for line in sys.stdin]


def write_stdout(lines: list[str]) -> None:
    for line in lines:
        # This leaves the file with a linebreak at the end, which is allowed according to spec
        print(line, file=sys.stdout)


def main() -> None:
    c = csv.parse(read_stdin())
    write_stdout(csv.dump(c))


# i don't think this is necessary in this one specific case (see file name) but let's honor the convention
if __name__ == "__main__":
    main()
