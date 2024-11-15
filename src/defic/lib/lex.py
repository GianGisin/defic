import dataclasses
from enum import auto, Enum


class TokenType(Enum):
    identifier = auto()
    opPlus = auto()
    opMinus = auto()
    opDiv = auto()
    opMult = auto()
    opExp = auto()
    # only int of float for now (no strings)
    litInt = auto()
    litFloat = auto()
    openBracket = auto()
    closeBracket = auto()
    rangeColon = auto()


@dataclasses.dataclass
class Token:
    token_type: TokenType
    value: any


class Storer:
    def __init__(self, text: str):
        text = list(text)
        text.reverse()
        self.letters = text

    def consume(self) -> str:
        return self.letters.pop()

    def peek(self) -> str:
        return self.letters[-1]

    def has_next(self) -> bool:
        return bool(self.letters)


def scan_cell(text: str) -> list[Token]:
    s = Storer(text.strip())
    tokens = []
    while s.has_next():
        current = ""
        l = s.consume()
        current += l
        match l:
            case l if 90 >= ord(l) >= 65:
                # uppercase letter, either function or cell
                while s.has_next():
                    if s.peek().isalnum():
                        current += s.consume()
                    else:
                        tokens.append(Token(TokenType.identifier, current))
                        break
                else:
                    tokens.append(Token(TokenType.identifier, current))

            case ":":
                tokens.append(Token(TokenType.rangeColon, None))

            case "(":
                tokens.append(Token(TokenType.openBracket, None))

            case ")":
                tokens.append(Token(TokenType.closeBracket, None))

            case "+":
                tokens.append(Token(TokenType.opPlus, None))

            case "-":
                tokens.append(Token(TokenType.opMinus, None))

            case "*":
                tokens.append(Token(TokenType.opMult, None))

            case "/":
                tokens.append(Token(TokenType.opDiv, None))

            case "^":
                tokens.append(Token(TokenType.opExp, None))

            case l if l.isnumeric():
                # int or float literal
                lit_type = TokenType.litInt
                while s.has_next():
                    if s.peek().isnumeric():
                        current += s.consume()
                    elif s.peek() == ".":
                        # TODO: throw error if literal ends with a period
                        current += s.consume()
                        lit_type = TokenType.litFloat
                    else:
                        tokens.append(Token(lit_type, current))
                        break
                else:
                    tokens.append(Token(lit_type, current))

    return tokens


def main() -> None:
    print(scan_cell("A1:A2"))


if __name__ == "__main__":
    main()
