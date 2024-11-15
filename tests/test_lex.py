import unittest
from defic.lib import lex
from defic.lib.lex import TokenType, Token


class TestStorer(unittest.TestCase):
    def test_init(self):
        Storer = lex.Storer("=A1 + A3")
        self.assertEqual(Storer.letters, ["3", "A", " ", "+", " ", "1", "A", "="])

    def test_hasnext(self):
        s = lex.Storer("a")
        self.assertEqual(s.has_next(), True)

        s.consume()
        self.assertEqual(s.has_next(), False)


class TestScanning(unittest.TestCase):
    def test_cellname(self):
        self.assertEqual(lex.scan_cell("A1"), [Token(TokenType.identifier, "A1")])
        self.assertEqual(lex.scan_cell("A1 "), [Token(TokenType.identifier, "A1")])
        self.assertEqual(
            lex.scan_cell("A1 A2"),
            [Token(TokenType.identifier, "A1"), Token(TokenType.identifier, "A2")],
        )

    def test_whitespace(self):
        self.assertEqual(lex.scan_cell("    "), [])

    def test_range(self):
        self.assertEqual(
            lex.scan_cell("A1:A2"),
            [
                Token(TokenType.identifier, "A1"),
                Token(TokenType.rangeColon, None),
                Token(TokenType.identifier, "A2"),
            ],
        )

    def test_lit(self):
        self.assertEqual(
            lex.scan_cell("3.14159"), [Token(TokenType.litFloat, "3.14159")]
        )
        self.assertEqual(lex.scan_cell("42"), [Token(TokenType.litInt, "42")])
        self.assertEqual(lex.scan_cell("42 "), [Token(TokenType.litInt, "42")])
        self.assertEqual(
            lex.scan_cell("42 3"),
            [Token(TokenType.litInt, "42"), Token(TokenType.litInt, "3")],
        )
