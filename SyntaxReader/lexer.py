from tokens import Token, TokenType

WHITESPACE = " \n\t"
DIGITS = "0123456789"
LETTERS = "abcdefghijlkmnopqrstuvwxyz"

class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None
    
    def generate_token(self):
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()

            elif self.current_char == "." or self.current_char in DIGITS:
                yield self.generate_number()

            elif self.current_char in LETTERS:
                yield self.generate_property()

            elif self.current_char == "+":
                self.advance()
                yield Token(TokenType.PLUS)

            elif self.current_char == "-":
                self.advance()
                yield Token(TokenType.MINUS)

            elif self.current_char == "*":
                self.advance()
                yield self.star()

            elif self.current_char == "^":
                self.advance()
                yield Token(TokenType.POWER)
                
            elif self.current_char == "/":
                self.advance()
                yield Token(TokenType.DIVIDE)

            elif self.current_char == "(":
                self.advance()
                yield Token(TokenType.LPAREN)

            elif self.current_char == ")":
                self.advance()
                yield Token(TokenType.RPAREN)
                
            else:
                raise Exception(f"Illegal Character '{self.current_char}'")
    
    def generate_number(self):
        number_str = self.current_char
        decimal_point_count = 0
        self.advance()

        while self.current_char != None and (self.current_char == "." or self.current_char in DIGITS):
            if self.current_char == ".":
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break

            number_str += self.current_char
            self.advance()

        if number_str.startswith("."):
            number_str = "0" + number_str

        if number_str.endswith("."):
            number_str + "0"

        return Token(TokenType.NUMBER, float(number_str))
    
    def generate_property(self):
        prop_str = self.current_char
        self.advance()
        while self.current_char in LETTERS:
            prop_str += self.current_char
            self.advance()
    #TODO (sheshe): here need to compare if this prop_str is in the input list. if not return error.
        return Token(TokenType.PROP, str(prop_str))

    def star(self):
        if self.current_char == "*":
            self.advance()
            print("read **")
            result = Token(TokenType.POWER)
            return result
        elif self.current_char != "*":
            print("read *")
            result = Token(TokenType.MULTIPLY)
            return result