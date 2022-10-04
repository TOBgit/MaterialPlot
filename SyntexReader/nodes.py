from dataclasses import dataclass

@dataclass
class NumberNode:
    value: any
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
    def __repr__(self):
# TODO (sheshe) here we need to read the mean of the property
        return f"{self.value}"
# TODO and need to get the SD and calculate it through error propagation

@dataclass
class PowerNode:
    node_a: any
    node_b: any
    def __repr__(self):
       return f"{self.node_a}^{self.node_b}"

