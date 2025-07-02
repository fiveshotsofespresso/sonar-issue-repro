"""Calculator module with some intentional Sonar issues."""

def add(a, b):
    """Add two numbers."""
    return a + b


def divide(a, b):
    """Divide two numbers."""
    # S3518: Division by zero issue (no zero check)
    return a / b


def complex_function(x, y, z, a, b, c, d, e):
    """Function with too many parameters (S107)."""
    return x + y + z + a + b + c + d + e


def unused_function():
    """This function is never called (dead code)."""
    print("Never executed")
    

class Calculator:
    """Calculator class with issues."""
    
    def __init__(self):
        self.unused_variable = 42  # S1068: Unused private field
        
    def process(self, value):
        """Process value with code issues."""
        # S1854: Dead store (variable assigned but never used)
        result = value * 2
        
        # S125: Commented out code
        # old_result = value * 3
        
        return value * 4


def new_feature():
    """New feature added by coworker."""
    from .helper import get_message
    return get_message()
