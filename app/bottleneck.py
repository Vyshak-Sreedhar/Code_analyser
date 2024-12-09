import ast

def analyze_code(code: str) -> dict:
    """
    Analyzes the provided code for potential performance bottlenecks.
    """
    issues = []
    suggestions = []

    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.For):
                if isinstance(node.iter, ast.Call) and isinstance(node.iter.func, ast.Name) and node.iter.func.id == "range":
                    issues.append("Nested loop detected")
                    suggestions.append("Consider optimizing nested loops to reduce computational complexity.")
            elif isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id == "sorted":
                    issues.append("Sorting operation detected")
                    suggestions.append("Ensure the sorting operation is necessary or use optimized libraries.")
    except SyntaxError:
        issues.append("Code syntax is invalid.")
        suggestions.append("Fix syntax errors before analysis.")

    return {"issues": issues, "suggestions": suggestions}
