import re
from app.models import db, Rule

class Node:
    def __init__(self, type, left=None, right=None, value=None):
        if type not in ("operator", "operand"):
            raise ValueError(f"Invalid node type: {type}")
        self.type = type    # "operator" or "operand"
        self.left = left    # Left child node
        self.right = right  # Right child node
        self.value = value  # Operand value (for conditions)
    
    def __repr__(self):
        return f"Node({self.type}, {self.value}, {self.left}, {self.right})"

def parse_condition(condition):
    match = re.match(r"(\w+)\s*(>=|<=|>|<|=)\s*([\w']+)", condition)
    if match:
        left, operator, right = match.groups()
        return Node("operand", value=(left, operator, right))
    else:
        raise ValueError(f"Invalid condition: {condition}")
    
def create_rule(rule_string):
    tokens = re.split(r'(\sAND\s|\sOR\s)', rule_string)
    if len(tokens) != 3:
        raise ValueError(f"Invalid rule format: {rule_string}")
    
    left_condition = parse_condition(tokens[0].strip())
    operator = tokens[1].strip()
    right_condition = parse_condition(tokens[2].strip())

    if operator not in ["AND", "OR"]:
        raise ValueError(f"Invalid operator: {operator}")

    root = Node("operator", left=left_condition, right=right_condition, value=operator)
    return root
