def add(a: int, b: int) -> int:
    return a + b

x: int = add(1, 2)
y: int = "hello"  # type mismatch
print(x, y)
