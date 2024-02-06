from itertools import product


def error_operator():
    raise Exception()


def hello_world_operator(name: str):
    return f"Hello, {name}!"


OPERATORS = {
    'sum': sum,
    'product': product,
    'error_operator': error_operator,
    'hello_world_operator': hello_world_operator,
}
