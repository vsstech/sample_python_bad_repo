import os  # unused import (ruff F401)


def dangerous(user_input: str):
    return eval(user_input)  # bandit issue: eval


def add(a: int, b: int) -> int:
    return a + b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b
