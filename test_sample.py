"""Example module demonstrating a simple increment function and its test."""

def increment(value):
    """Increment the given value by 1."""
    return value + 1

def test_answer():
    """Test if the increment function works as expected."""
    assert increment(3) == 4
