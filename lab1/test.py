import unittest
import scanner


class Test_Scanner(unittest.TestCase):

    def test_small_example(self):
        with open('small_example.txt', 'r') as f:
            text = f.read()
        lexer = scanner.lexer
        lexer.input(text)  # Give the lexer some input

        out = ""
        # Tokenize
        while True:
            tok = lexer.token()
            if not tok:
                break  # No more input
            out += ("(%d): %s(%s)\n" % (tok.lineno, tok.type, tok.value))

        correct = \
            """(1): ID(A)
(1): =(=)
(1): ZEROS(zeros)
(1): ((()
(1): INTNUM(5)
(1): )())
(1): ;(;)
(2): ID(B)
(2): =(=)
(2): ONES(ones)
(2): ((()
(2): INTNUM(7)
(2): )())
(2): ;(;)
(3): ID(I)
(3): =(=)
(3): EYE(eye)
(3): ((()
(3): INTNUM(10)
(3): )())
(3): ;(;)
(4): ID(D1)
(4): =(=)
(4): ID(A)
(4): DOTADD(.+)
(4): ID(B)
(4): '(')
(4): ;(;)
(5): ID(D2)
(5): SUBASSIGN(-=)
(5): ID(A)
(5): DOTSUB(.-)
(5): ID(B)
(5): '(')
(5): ;(;)
(6): ID(D3)
(6): MULASSIGN(*=)
(6): ID(A)
(6): DOTMUL(.*)
(6): ID(B)
(6): '(')
(6): ;(;)
(7): ID(D4)
(7): DIVASSIGN(/=)
(7): ID(A)
(7): DOTDIV(./)
(7): ID(B)
(7): '(')
(7): ;(;)
"""
        self.assertEqual(correct, out)

    def test_example_full_no_exception(self):
        with open('example_full.txt', 'r') as f:
            text = f.read()
        try:
            lexer = scanner.lexer
            lexer.input(text)  # Give the lexer some input
        except Exception:
            self.fail("Exception occurred while parsing example_full")


if __name__ == "__main__":
    unittest.main()