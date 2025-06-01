from core.node import STNNode
from core.stream_ops import map_sense

# Цепочка событий: вход -> обработка -> выход
stream = [
    STNNode(state=0, annotation="Вход"),
    STNNode(state=1, annotation="Обработка"),
    STNNode(state=-1, annotation="Ошибка")
]

print("Исходная цепочка:")
for node in stream:
    print(node)

# Шаг 1: все “обработки” ускоряем
def process_step(node):
    if node.annotation == "Обработка":
        node.tempo *= 5
        node.annotation += " (ускорено)"
    return node

stream = map_sense(stream, process_step)

# Шаг 2: все “Ошибка” — замедляем
def error_step(node):
    if "Ошибка" in str(node.annotation):
        node.tempo *= 0.1
        node.annotation += " (замедлено)"
    return node

stream = map_sense(stream, error_step)

print("Цепочка после событий:")
for node in stream:
    print(node)
