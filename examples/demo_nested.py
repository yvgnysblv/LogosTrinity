from core.node import STNNode
from core.stream_ops import map_sense, reduce_sense
from core.annotation import annotate_stream
from collections import defaultdict

# 1. Вложенные потоки: каждый "родитель" содержит свой поток "детей"
parent_nodes = [
    STNNode(state=1, meta={"label": "A"}),
    STNNode(state=0, meta={"label": "B"}),
]

child_streams = [
    [STNNode(state=1, meta={"parent": "A", "val": 5}), STNNode(state=-1, meta={"parent": "A", "val": -3})],
    [STNNode(state=0, meta={"parent": "B", "val": 7}), STNNode(state=1, meta={"parent": "B", "val": 8})]
]

# Применим массовую аннотацию к каждому потоку детей
for stream, parent in zip(child_streams, parent_nodes):
    ann = [f"Дитя {i+1} родителя {parent.meta['label']}" for i in range(len(stream))]
    annotate_stream(stream, ann)

# 2. Группировка: по родителю собираем суммы state у детей
grouped_sums = {}
for parent, children in zip(parent_nodes, child_streams):
    state_sum = reduce_sense(children, lambda acc, n: acc + n.state, 0)
    grouped_sums[parent.meta["label"]] = state_sum

print("Суммы состояний по родителю:")
for k, v in grouped_sums.items():
    print(f"  Родитель {k}: сумма состояний детей = {v}")

# 3. Цепочка reduce: соберём общее количество “позитивных” детей по всем группам
def count_positive(acc, child):
    return acc + (1 if child.state > 0 else 0)

total_positive = sum(reduce_sense(children, count_positive, 0) for children in child_streams)
print("Общее количество позитивных детей во всех группах:", total_positive)

# 4. Сложный пайплайн: дерево событий (цепочка событий)
# Для каждого родителя: фильтруем только позитивных детей и собираем их метки в список
def collect_positive_labels(children):
    return [n.meta["val"] for n in children if n.state > 0]

event_tree = {
    parent.meta["label"]: collect_positive_labels(children)
    for parent, children in zip(parent_nodes, child_streams)
}
print("Дерево позитивных событий:")
for k, v in event_tree.items():
    print(f"  {k}: {v}")

# 5. Вложенные map/reduce: среднее значение meta["val"] среди всех детей всех родителей
all_children = [n for stream in child_streams for n in stream]
values = [n.meta["val"] for n in all_children]
mean_val = sum(values) / len(values)
print("Среднее значение meta['val'] среди всех детей:", mean_val)

# 6. Группировка по произвольному критерию (state): defaultdict
groups = defaultdict(list)
for node in all_children:
    groups[node.state].append(node)
print("Группировка детей по состоянию:")
for state, nodes in groups.items():
    print(f"  Состояние {state}: {[n.meta['val'] for n in nodes]}")

# 7. Edge-case: обработка пустой группы
empty_stream = []
try:
    res = reduce_sense(empty_stream, lambda acc, n: acc + n.state, 0)
    print("Сумма по пустому потоку:", res)
except Exception as e:
    print("Ошибка при агрегации пустого потока:", e)
