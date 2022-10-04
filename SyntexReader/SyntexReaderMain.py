from lexer import Lexer
from parser import Parser

#https://github.com/davidcallanan/py-simple-math-interpreter

while True:
    text = input("calc > ")
    lexer = Lexer(text)
    tokens = lexer.generate_token()
    parser = Parser(tokens)
    tree = parser.parse()
    print(tree)