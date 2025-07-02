"""Helper module with new code."""

import os
import sys  # S1128: Unused import


def get_message():
    """Get a message."""
    unused_var = "This is never used"  # S1854: Dead store
    
    # S1066: Collapsible if statements
    if os.path.exists("config.ini"):
        if os.path.isfile("config.ini"):
            return "Config found"
    
    return "Hello World"


def empty_function():
    """Empty function (S1186)."""
    pass


class HelperClass:
    """Helper class."""
    
    def method_with_too_many_returns(self, value):
        """Method with too many return statements (S1142)."""
        if value < 0:
            return "negative"
        if value == 0:
            return "zero"
        if value < 10:
            return "small"
        if value < 100:
            return "medium"
        if value < 1000:
            return "large"
        return "huge"
