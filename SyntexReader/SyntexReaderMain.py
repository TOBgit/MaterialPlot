from lexer import Lexer
from parser import Parser
from Interpreter import meanInterpreter, errorPropagationInterpreter

#adapted from https://github.com/davidcallanan/py-simple-math-interpreter

while True:
    try:
        text = input("calc > ")
        lexer = Lexer(text)
        tokens = lexer.generate_token()
        parser = Parser(tokens)
        tree = parser.parse()
        if not tree: continue
        meanInt = meanInterpreter()
        value = meanInt.visit(tree)
        print(value)
    except Exception as e:
        print(e)