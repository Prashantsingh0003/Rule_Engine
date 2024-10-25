from app.rule_parser import Node

def combine_rules(rules):
    if not rules:
        return None
    
    root = rules[0]
    for rule in rules[1:]:
        root = Node("operator", left=root, right=rule, value="AND")
    
    return root
