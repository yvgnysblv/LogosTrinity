from core.node import STNNode
from core.stream_ops import map_sense, reduce_sense

def pipeline(data, *funcs):
    for f in funcs:
        data = f(data)
    return data

# Пайплайн: map -> reduce
nodes = [STNNode(state=1), STNNode(state=-1)]
result = pipeline(
    nodes,
    lambda s: map_sense(s, lambda n: n.state),
    lambda s: reduce_sense(s, lambda a, b: a + b, 0)
)
print("Пайплайн результат:", result)  # 0
