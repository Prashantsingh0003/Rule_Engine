from flask import Blueprint, request, jsonify
from app.models import db, Rule
from app.rule_parser import create_rule
from app.rule_evaluator import evaluate_rule
from app.rule_combiner import combine_rules
import json

api_bp = Blueprint('api', __name__)

@api_bp.route('/create_rule', methods=['POST'])
def create_rule_route():
    try:
        rule_string = request.json.get('rule')
        if not rule_string:
            return jsonify({"error": "Missing rule string"}), 400
        
        # Create the rule AST
        rule_ast = create_rule(rule_string)
        ast_json = json.dumps(rule_ast, default=lambda x: x.__dict__)
        
        # Save rule in the database
        new_rule = Rule(rule_string=rule_string, ast_json=ast_json)
        db.session.add(new_rule)
        db.session.commit()

        return jsonify({"message": "Rule created", "ast": ast_json}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@api_bp.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_route():
    try:
        rule_id = request.json.get('rule_id')
        user_data = request.json.get('data')
        
        rule = Rule.query.get(rule_id)
        if not rule:
            return jsonify({"error": "Rule not found"}), 404

        ast = json.loads(rule.ast_json)
        result = evaluate_rule(ast, user_data)

        return jsonify({"message": "Evaluation complete", "result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
