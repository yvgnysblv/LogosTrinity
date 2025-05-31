def trinary_and(a, b):
    # Таблица троичного AND: -1, 0, +1
    table = [
        [1, 0, -1],
        [0, 0, -1],
        [-1, -1, -1]
    ]
    return table[a + 1][b + 1]

def trinary_or(a, b):
    table = [
        [1, 1, 1],
        [1, 0, 0],
        [1, 0, -1]
    ]
    return table[a + 1][b + 1]

def trinary_not(a):
    return -a if a != 0 else 0

def superpose(node):
    node.state = 0

def collapse(node, value):
    assert value in [-1, 1]
    node.state = value
