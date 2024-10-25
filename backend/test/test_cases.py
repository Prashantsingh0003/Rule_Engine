from app.rule_parser import create_rule
from app.rule_combiner import combine_rules
from app.rule_evaluator import evaluate_rule

def test_create_rule():
    rule1 = create_rule("age > 30 AND department = 'Sales'")
    assert rule1 is not None

def test_combine_rules():
    rule1 = create_rule("age > 30 AND department = 'Sales'")
    rule2 = create_rule("salary > 50000 OR experience > 5")
    combined_ast = combine_rules([rule1, rule2])
    assert combined_ast is not None

def test_evaluate_rule():
    rule1 = create_rule("age > 30 AND department = 'Sales'")
    rule2 = create_rule("salary > 50000 OR experience > 5")
    combined_ast = combine_rules([rule1, rule2])
    
    user_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
    result = evaluate_rule(combined_ast, user_data)
    assert result == True
