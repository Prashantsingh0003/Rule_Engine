def evaluate_rule(node, data):
    if node.type == "operator":
        left_eval = evaluate_rule(node.left, data)
        right_eval = evaluate_rule(node.right, data)
        if node.value == "AND":
            return left_eval and right_eval
        elif node.value == "OR":
            return left_eval or right_eval
    elif node.type == "operand":
        attr, operator, value = node.value
        user_value = data.get(attr)

        if user_value is None:
            raise ValueError(f"Missing attribute in data: {attr}")
        
        try:
            if operator == '>':
                return user_value > int(value)
            elif operator == '<':
                return user_value < int(value)
            elif operator == '=':
                return user_value == value
        except ValueError as e:
            raise ValueError(f"Error evaluating operand: {e}")
    
    return False
