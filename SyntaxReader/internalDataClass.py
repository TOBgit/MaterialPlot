from dataclasses import dataclass
from enum import Enum

#
# Tokens: the first type of items after processed through latex syntax.
# It includes the enum information about the syntax.
#
class TokenType(Enum):
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    LPAREN = 5
    RPAREN = 6
    POWER = 7
    PROP = 8

@dataclass
class Token:
    type: TokenType
    value: any = None
    sd: any = None
    def __repr__(self):
        return (self.type.name + (f":{self.value}" if self.value != None else "")
                + (f"({self.sd})" if self.sd != None else ""))


#
# Nodes: used for describing the semantic relationship among the individual items.
# It describes the item contents (for content nodes) or the relationship between items (for operator nodes).
#
@dataclass
class NumberNode:
    value: any
    sd: any = 0
    def __repr__(self):
        return f"{self.value}"

@dataclass
class AddNode:
    node_a: any
    node_b: any
    def __repr__(self):
        return f"({self.node_a}+{self.node_b})"

@dataclass
class SubtractNode:
    node_a: any
    node_b: any
    def __repr__(self):
        return f"({self.node_a}-{self.node_b})"

@dataclass
class MultiplyNode:
    node_a: any
    node_b: any
    def __repr__(self):
        return f"({self.node_a}*{self.node_b})"

@dataclass
class DivideNode:
    node_a: any
    node_b: any
    def __repr__(self):
        return f"({self.node_a}/{self.node_b})"

@dataclass
class PlusNode:
    node: any
    def __repr__(self):
        return f"(+{self.node})"
    
@dataclass
class MinusNode:
    node: any
    def __repr__(self):
        return f"(-{self.node})"
        
@dataclass
class PropNode:
    value: any
    sd: any
    def __repr__(self):
        return f":{self.value}({self.sd})"

@dataclass
class PowerNode:
    node_a: any
    node_b: any
    def __repr__(self):
        return f"{self.node_a}**{self.node_b}"


#
# Number: internal data transferring structure inside the interpreter.
#
@dataclass
class Number:
    value: any = None
    sd: any = None
    def __repr__(self):
        return ((f":{self.value}" if self.value != None else "")
                + (f"({self.sd})" if self.sd != None else ""))
