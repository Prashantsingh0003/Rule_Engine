# Rule Engine with Abstract Syntax Tree (AST)

## Overview
This project is a 3-tier rule engine application built with a simple UI, API, and Backend that enables dynamic rule creation and evaluation based on user attributes like age, department, income, and experience. The system utilizes an Abstract Syntax Tree (AST) to efficiently represent and manage conditional rules, allowing for dynamic rule generation, combination, and modification.

## Table of Contents
- [Objective](#objective)
- [Data Structure](#data-structure)
- [Data Storage](#data-storage)
- [API Design](#api-design)
- [Sample Rules](#sample-rules)
- [Testing](#testing)
- [Error Handling](#error-handling)
- [Future Enhancements](#future-enhancements)

## Objective
The primary goal of this project is to evaluate user eligibility based on predefined rules, using an AST to structure complex conditional rules dynamically. The system should be capable of:
- Parsing rule strings to create an AST representation.
- Combining multiple ASTs to create more complex rules.
- Evaluating user data against these rules.

![image](https://github.com/user-attachments/assets/3609d374-a062-4cde-b478-5fdabf40cd6b)

![image](https://github.com/user-attachments/assets/2832583e-b870-48e0-965e-549b65f1b3a4)

![image](https://github.com/user-attachments/assets/1150f7ab-6514-4845-951d-968fcf4ab320)

![image](https://github.com/user-attachments/assets/66abc981-6b6e-4f43-b842-987cba561410)


## Data Structure
To support dynamic rule handling, the following data structure is implemented to represent the AST:

```python
class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type  # "operator" (AND/OR) or "operand" (condition)
        self.left = left  # Reference to another Node (left child)
        self.right = right  # Reference to another Node (right child for operators)
        self.value = value  # Optional, used for operand nodes (e.g., numbers for comparisons)
This structure allows for flexible modification and combination of rules.

Data Storage
Database Choice
We chose MySQL as our database, which supports storing rules and metadata dynamically, aligning well with our project’s needs.

Schema
Each rule is stored as a document with the following fields:

{
  "_id": "<unique_id>",
  "rule": "<rule_string>",
  "AST": "<AST_representation>",
  "metadata": {
    "created_at": "<timestamp>",
    "modified_at": "<timestamp>"
  }
}
API Design
The following API endpoints allow rule creation, modification, and evaluation:

create_rule(rule_string): Parses a rule string into an AST.
combine_rules(rules): Takes a list of rule strings and combines them into a single AST.
evaluate_rule(JSON_data): Evaluates user data against the combined rule’s AST and returns True if the data meets the rule conditions, otherwise False.

Sample Usage
# Sample rule strings
rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"

# Creating AST nodes
node1 = create_rule(rule1)
node2 = create_rule(rule2)

# Combining rules
combined_node = combine_rules([rule1, rule2])



# Evaluating rules
data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
result = evaluate_rule(combined_node, data)  # Returns True or False


Sample Rules
Rule 1: "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
Rule 2: "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
These sample rules are parsed into ASTs using the create_rule function and evaluated by evaluate_rule.


Testing
Test Cases
Rule Creation: Verify the AST structure for each rule using create_rule.
Rule Combination: Ensure the combined AST accurately represents combined rules using combine_rules.
Evaluation: Test various data inputs against evaluate_rule to validate rule functionality.
Additional Rule Testing: Add further sample rules to explore AST efficiency and ensure accuracy.
Error Handling
The system includes validation to handle:

Invalid rule syntax or missing operators.
Invalid attribute types or unsupported comparisons.
Ensuring attribute values in the rules are part of an allowed catalog.
Future Enhancements
Consider expanding the rule language to support:

User-defined functions for advanced custom conditions.
Rule modification utilities to allow dynamic changes to existing rules (e.g., change conditions, add/remove expressions).
Optimized AST Parsing to minimize redundant checks and improve performance.
Acknowledgments
Inspired by real-world eligibility checking systems, this rule engine leverages AST for optimal rule handling and evaluation.


This `README.md` is structured to give an overview, code samples, and clarity on the project's goals and design. It should be helpful for others exploring or contributing to your project!
