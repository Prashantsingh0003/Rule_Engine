from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Rule model to store the rule string and AST
class Rule(db.Model):
    __tablename__ = 'rules'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rule_string = db.Column(db.Text, nullable=False)
    ast_json = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
