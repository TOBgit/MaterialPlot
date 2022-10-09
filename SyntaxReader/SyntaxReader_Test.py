from SyntaxReader.lexer import LexerForData
from SyntaxReader.parser_ import Parser
from SyntaxReader.Interpreter import Interpreter

#adapted from https://github.com/davidcallanan/py-simple-math-interpreter

while True:
    try:
        test_data = {"Density_mean": 1., "Density_sd": .1, "Modulus_mean": 2., "Modulus_sd": .2}
        text = input("calc > ")
        lexer = LexerForData(text, test_data)
        tokens = lexer.generate_token()
        parser = Parser(tokens)
        tree = parser.parse()
        print(tree)
        if not tree: continue
        meanInt = Interpreter()
        value = meanInt.visit(tree)
        print(meanInt.visit(tree).value, meanInt.visit(tree).sd)
        print(value)
    except Exception as e:
        print(e)