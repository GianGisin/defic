from typing import Union


class UnevenRowError(Exception):
    pass


def parse(lines: list[str]) -> list[list[Union[str, int]]]:
    # RFC4180 ch2, paragraph 4, every line should have the same width
    result = []
    width = None
    for line in lines:
        line = line.strip("\n")
        line = line.split(",")
        if width and len(line) != width:
            raise UnevenRowError("All rows need to have the same amount of elements")
        width = len(line)
        result.append(line)
    return result
