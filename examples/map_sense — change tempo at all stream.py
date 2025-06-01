from core.node import STNNode
from core.stream_ops import map_sense

# Сначала создаём поток узлов!
stream = [
    STNNode(state=0),
    STNNode(state=1),
    STNNode(state=-1)
]

def slow_down(node):
    node.tempo *= 0.5
    return node

new_stream = map_sense(stream, slow_down)

print("Поток после замедления:")
for node in new_stream:
    print(node)
