from SyntaxReader.nodes import *
from SyntaxReader.values import Number

class meanInterpreter:

    def visit(self, node):
        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name)
        return method(node)

    def visit_NumberNode(self, node):
        return Number(node.value)

    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)
    
    def visit_SubtractNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_DivideNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise Exception("Runtime math error")

    def visit_PowerNode(self, node):
        return Number(self.visit(node.node_a).value ** self.visit(node.node_b).value)

    def visit_PlusNode(self, node):
        return self.visit(node.node)

    def visit_MinusNode(self, node):
        return Number(-self.visit(node.node).value)

##here input is mean (node.value) and sd (node.std)
class errorPropagationInterpreter:
    def visit(self, node):
        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name)
        return method(node)

    def visit_NumberNode(self, node):
        return Number(node.value)

#need to bring in the mean...
    def visit_AddNode(self, node):
        return Number((self.visit(node.node_a).value **2 + self.visit(node.node_b).value ** 2)**0.5)
#here too...
    def visit_SubtractNode(self, node):
        return Number((self.visit(node.node_a).value **2 + self.visit(node.node_b).value ** 2)**0.5)

    def visit_MultiplyNode(self, node):
        return Number((self.visit(node.node_a).value **2 + self.visit(node.node_b).value ** 2)**0.5)

    def visit_DivideNode(self, node):
        try:
            return Number((self.visit(node.node_a).value **2 + self.visit(node.node_b).value ** 2)**0.5)
        except:
            raise Exception("Runtime math error")

    def visit_PowerNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_PlusNode(self, node):
        return self.visit(node.node)

    def visit_MinusNode(self, node):
        return Number(-self.visit(node.node).value)