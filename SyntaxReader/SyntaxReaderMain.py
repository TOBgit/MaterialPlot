from lexer import Lexer
from parser_ import Parser
from Interpreter import meanInterpreter

#adapted from https://github.com/davidcallanan/py-simple-math-interpreter

while True:
    try:
        text = input("calc > ")
        lexer = Lexer(text)
        tokens = lexer.generate_token()
        parser = Parser(tokens)
        tree = parser.parse()
        print(tree)
        if not tree: continue
        meanInt = meanInterpreter()
        value = meanInt.visit(tree)
        print(value)
    except Exception as e:
        print(e)