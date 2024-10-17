from flask import Flask, request, jsonify, render_template
import ast
import operator

app = Flask(__name__)

# Sample user data for testing
users = [
    {"id": 1, "age": 35, "department": "Sales", "salary": 60000, "experience": 3},
    {"id": 2, "age": 22, "department": "Marketing", "salary": 45000, "experience": 1},
    {"id": 3, "age": 40, "department": "Tech", "salary": 90000, "experience": 15},
]

# Rule Engine class using Abstract Syntax Tree (AST)
class RuleEngine:
    def __init__(self, user):
        self.user = user

    def evaluate(self, rule):
        # Parse the rule into an AST (expression)
        tree = ast.parse(rule, mode='eval')
        return self._eval(tree.body)

    def _eval(self, node):
        # Operators mapping for AST evaluation
        operators_map = {
            ast.And: operator.and_,
            ast.Or: operator.or_,
            ast.Eq: operator.eq,
            ast.Gt: operator.gt,
            ast.GtE: operator.ge,
            ast.Lt: operator.lt,
            ast.LtE: operator.le,
            ast.NotEq: operator.ne,
        }

        # Evaluate binary operation (e.g., age > 30)
        if isinstance(node, ast.BinOp):
            left = self._eval(node.left)
            right = self._eval(node.right)
            return operators_map[type(node.op)](left, right)

        # Evaluate comparisons (e.g., age > 30 and department == 'Sales')
        elif isinstance(node, ast.Compare):
            left = self._eval(node.left)
            right = self._eval(node.comparators[0])
            return operators_map[type(node.ops[0])](left, right)

        # Return the value of user attribute (e.g., user['age'])
        elif isinstance(node, ast.Name):
            return self.user.get(node.id)

        # Return constant value in the rule (e.g., 30, 'Sales')
        elif isinstance(node, ast.Constant):
            return node.value

        return False

@app.route('/')
def home():
    return render_template('index.html')

# Route to evaluate a rule for a specific user
@app.route('/check_eligibility', methods=['POST'])
def check_eligibility():
    data = request.json
    user_id = data.get('user_id')
    rule = data.get('rule')

    # Fetch the user data based on ID
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Create an instance of the Rule Engine for the user
    engine = RuleEngine(user)
    result = engine.evaluate(rule)

    return jsonify({"user_id": user_id, "eligible": result, "rule": rule})

if __name__ == '__main__':
    app.run(debug=True)
