from typing import Dict

from SyntaxReader.internalDataClass import *
from SyntaxReader.lexer import LexerForData
from SyntaxReader.parser import Parser

class Interpreter:
    '''
    This interpreter class handle the calculation of the mean and std from a node tree.
    For std, we calculate any with error propagation:
    Var(a) = std(a) ^ 2
    Var(f(x)) ~= (f'(x)^2) * Var(x)
    and thus
    Var(a + b) = Var(a) + Var(b)
    Var(a * b) ~= Var(a) * b^2 +  Var(b) * a^2
    Var(a / b) ~= Var(a) / b^2 +  Var(b) * a^2 / b^4
    Var(a ^ n) ~= (n * a^(n-1))^2 * Var(a)
    '''
    def visit(self, node):
        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name)
        return method(node)

    def visit_NumberNode(self, node):
        return Number(node.value, 0)

    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value,
                      (self.visit(node.node_a).sd ** 2 + self.visit(node.node_b).sd ** 2) ** .5)
    
    def visit_SubtractNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value,
                      (self.visit(node.node_a).sd ** 2 + self.visit(node.node_b).sd ** 2) ** .5)

    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value,
                      (self.visit(node.node_a).sd ** 2 * self.visit(node.node_b).value ** 2
                       + self.visit(node.node_b).sd ** 2 * self.visit(node.node_a).value ** 2) ** .5)

    def visit_DivideNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value,
                          ((self.visit(node.node_a).sd ** 2 / self.visit(node.node_b).value ** 2)
                           +  (self.visit(node.node_b).sd ** 2
                              * self.visit(node.node_a).value ** 2
                              / self.visit(node.node_b).value ** 4)) ** .5)
        except:
            raise Exception("Runtime math error")

    def visit_PowerNode(self, node):
        # Note: only support the case that the order node is a number node.
        # Does not support the order node is a prop node. Result is wrong in such case.
        return Number(self.visit(node.node_a).value ** self.visit(node.node_b).value,
                      self.visit(node.node_a).sd * self.visit(node.node_b).value
                      * self.visit(node.node_a).value ** (self.visit(node.node_b).value - 1))

    def visit_PlusNode(self, node):
        return self.visit(node.node)

    def visit_MinusNode(self, node):
        return Number(-self.visit(node.node).value, self.visit(node.node).sd)

    def visit_PropNode(self, node):
        return Number(node.value, node.sd)

def evaluateWithData(syntax: str, original_data_features: Dict):
    '''
    :param syntax: the new feature name, without suffix.
    :param original_data_features: the source for referring the mean and sd of the original value.
    :return: the mean and sd of the new feature.
    '''
    lexer = LexerForData(syntax, original_data_features)
    tokens = lexer.generate_token()
    parser = Parser(tokens)
    tree = parser.parse()
    if not tree:
        return False
    meanInt = Interpreter()
    res = meanInt.visit(tree)
    return res.value, res.sd