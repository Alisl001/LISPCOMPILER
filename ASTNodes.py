# ASTNodes.py
class ASTNode:
    """Base class for all AST nodes."""
    def __init__(self, node_type):
        self.node_type = node_type
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"{self.node_type}({', '.join(map(str, self.children))})"

class ProgramNode(ASTNode):
    def __init__(self):
        super().__init__("Program")

class FunctionDefNode(ASTNode):
    def __init__(self, name):
        super().__init__("FunctionDef")
        self.name = name

    def __repr__(self):
        return f"FunctionDef(name={self.name}, params={self.children[0]}, body={self.children[1:]})"

class ParameterListNode(ASTNode):
    def __init__(self):
        super().__init__("Parameters")

class OperationNode(ASTNode):
    def __init__(self, operator):
        super().__init__(f"Operation({operator})")

class FunctionCallNode(ASTNode):
    def __init__(self, name):
        super().__init__(f"FunctionCall({name})")

class LiteralNode(ASTNode):
    def __init__(self, value):
        super().__init__(f"Literal({value})")

class IdentifierNode(ASTNode):
    def __init__(self, name):
        super().__init__("Identifier")
        self.name = name

    def __repr__(self):
        return f"Identifier({self.name})"

class LambdaNode(ASTNode):
    def __init__(self):
        super().__init__("Lambda")

class ConditionalNode(ASTNode):
    def __init__(self, condition_type):
        super().__init__(f"Conditional({condition_type})")

class CondClauseNode(ASTNode):
    def __init__(self):
        super().__init__("CondClause")

class FormatCallNode(ASTNode):
    def __init__(self):
        super().__init__("FormatCall")
