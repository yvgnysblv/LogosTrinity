from core.node import STNNode
from core.stream_ops import map_sense, reduce_sense, imap_sense

# Пример 1: map + reduce (сумма состояний узлов)
nodes = [STNNode(state=1), STNNode(state=-1)]
mapped = map_sense(nodes, lambda n: n.state)
total = reduce_sense(mapped, lambda a, b: a + b, 0)
print("Сумма состояний:", total)  # 0

# Пример 2: ленивый map (метаданные)
print("Метаданные узлов:")
for processed in imap_sense(nodes, lambda n: n.meta):
    print(processed)
