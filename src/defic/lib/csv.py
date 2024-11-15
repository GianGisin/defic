class UnevenRowError(Exception):
    pass


def parse(lines: list[str]) -> list[list[str]]:
    result = []
    width = None
    for line in lines:
        line = line.strip("\n")
        line = line.split(",")
        if width and len(line) != width:
            # RFC4180 ch2, paragraph 4, every line should have the same width
            raise UnevenRowError("All rows need to have the same amount of elements")
        width = len(line)
        result.append(line)
    return result


def dump(cells: list[any]) -> list[str]:
    result = []
    for rows in cells:
        line = ""
        # int, float are casted automatically to str
        for cell in rows:
            line += f"{cell},"
        result.append(line[:-1])
    return result
