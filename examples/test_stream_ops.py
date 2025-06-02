# Пример 1: map + reduce
nodes = [STNNode(state=1), STNNode(state=-1)]
mapped = map_sense(nodes, lambda n: n.state)
total = reduce_sense(mapped, lambda a, b: a + b, 0)
print(total)  # 0

# Пример 2: lazy map
for processed in lazy_map_sense(nodes, lambda n: n.meta):
    print(processed)

# Пример 3: пайплайн
result = pipeline(
    nodes,
    lambda s: map_sense(s, lambda n: n.state),
    lambda s: reduce_sense(s, lambda a, b: a + b, 0)
)
print(result)  # 0