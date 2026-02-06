def greeting(name: str) -> str:
    return "Hello " + name


x: int = "wrong-type"  # mypy should complain
