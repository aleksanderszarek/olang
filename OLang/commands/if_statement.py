from structures import Structures
from instructions import Instructions

class IfCommand(Instructions):
    def __init__(self, struc):
        super().__init__()
        self.skip_block = False 
        self.struc = struc

    def evaluate_condition(self, condition, line):
        """
        Evaluate a single condition. Handles variables and comparisons.
        """
        operators = ["==", "!=", "<=", ">=", "<", ">"]
        for operator in operators:
            if operator in condition:
                left, right = condition.split(operator, 1)
                # Remove the leading underscore only when accessing the structure
                left_value = self.struc.getValue(left.strip()[1:], line) if left.strip().startswith("_") else self.parse_literal(left.strip(), line)
                right_value = self.struc.getValue(right.strip()[1:], line) if right.strip().startswith("_") else self.parse_literal(right.strip(), line)
                if left_value is None or right_value is None:
                    return False  # Error already handled
                return self.compare(left_value, right_value, operator, line)
        self.error(1, line, f"Invalid condition: '{condition}'")
        return False

    def compare(self, left, right, operator, line):
        """Perform a comparison based on the operator."""
        try:
            if operator == "==":
                return left == right
            elif operator == "!=":
                return left != right
            left = float(left)
            right = float(right)
            if operator == "<=":
                return left <= right
            elif operator == ">=":
                return left >= right
            elif operator == "<":
                return left < right
            elif operator == ">":
                return left > right
        except TypeError:
            self.error(2, line, f"Cannot compare {type(left).__name__} with {type(right).__name__}")
        return False

    def parse_literal(self, value, line):
        """Convert a string to a literal value (number, boolean, or string)."""
        if value.startswith('"') and value.endswith('"'):
            return value[1:-1]
        elif value.lower() == "true":
            return True
        elif value.lower() == "false":
            return False
        try:
            return float(value)
        except ValueError:
            self.error(2, line, f"Invalid literal: {value}")
            return None

    def evaluate_expression(self, expression, line):
        """
        Evaluate a logical expression using || (or), && (and), /\ (xor).
        """
        if "||" in expression:
            conditions = expression.split("||")
            return any(self.evaluate_condition(cond.strip(), line) for cond in conditions)
        elif "&&" in expression:
            conditions = expression.split("&&")
            return all(self.evaluate_condition(cond.strip(), line) for cond in conditions)
        elif "/\\" in expression:
            conditions = expression.split("/\\")
            return (sum(self.evaluate_condition(cond.strip(), line) for cond in conditions) != 1)
        else:
            return self.evaluate_condition(expression, line)

    def execute(self, condition, line):
        self.skip_block = not self.evaluate_expression(condition, line)
        return self.skip_block

    def should_skip(self):
        return self.skip_block
