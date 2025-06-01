from core.node import STNNode
from core.annotation import annotate_stream

# Допустим, поток из 5 узлов
stream = [STNNode(state=i%3-1) for i in range(5)]  # [-1, 0, +1, -1, 0]

# Генерируем аннотации автоматически
annotations = [f"Шаг {i+1}: состояние {node.state}" for i, node in enumerate(stream)]
annotate_stream(stream, annotations)

for node in stream:
    print(node)
