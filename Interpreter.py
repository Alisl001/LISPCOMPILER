# Interpreter.py
from ASTNodes import *

class Interpreter:
    def evaluate(self, node):
        if isinstance(node, LiteralNode):
            return int(node.node_type.split('(')[1][:-1])
        elif isinstance(node, OperationNode):
            operator = node.node_type.split('(')[1][:-1]
            operands = [self.evaluate(child) for child in node.children]
            if operator == '+':
                return sum(operands)
            elif operator == '-':
                return operands[0] - sum(operands[1:])
            # Add more operators as needed
        elif isinstance(node, FunctionCallNode):
            if node.node_type == "FunctionCall(add)":
                return sum(self.evaluate(child) for child in node.children)
        return None
