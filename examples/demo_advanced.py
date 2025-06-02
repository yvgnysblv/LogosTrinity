from core.node import STNNode
from core.stream_ops import map_sense, reduce_sense, imap_sense
from core.annotation import annotate_stream

# 1. Генерируем поток узлов с разными state, tempo, meta
nodes = [
    STNNode(state=1, tempo=1.0, meta={"role": "начало"}),
    STNNode(state=0, tempo=0.5, meta={"role": "нейтраль"}),
    STNNode(state=-1, tempo=2.0, meta={"role": "конец"}),
]

# 2. Массово добавляем аннотации (по-русски для наглядности)
annotations = ["Шаг 1: старт", "Шаг 2: промежуточный", "Шаг 3: финал"]
annotate_stream(nodes, annotations)

# 3. Демонстрируем лямбда-map: ускоряем только позитивные состояния
def accelerate_if_positive(node):
    if node.state > 0:
        node.speed(2)
    return node

new_nodes = map_sense(nodes, accelerate_if_positive)

# 4. Ленивый map — вытаскиваем аннотации
print("Аннотации узлов (ленивый map):")
for ann in imap_sense(new_nodes, lambda n: n.annotation):
    print("-", ann)

# 5. reduce: агрегируем темп потока (произведение)
from functools import reduce
total_tempo = reduce(lambda acc, n: acc * n.tempo, new_nodes, 1)
print("Произведение темпов всех узлов:", total_tempo)

# 6. Пайплайн обработки: state -> аннотация -> суммируем только state != 0
def pipeline(data, *funcs):
    for f in funcs:
        data = f(data)
    return data

pipeline_result = pipeline(
    new_nodes,
    lambda stream: [n for n in stream if n.state != 0],
    lambda stream: map_sense(stream, lambda n: f"{n.annotation} [state={n.state}]"),
)
print("Пайплайн по особым узлам:")
for out in pipeline_result:
    print("-", out)

# 7. Проверим работу аннотации с ошибкой (edge case)
try:
    annotate_stream(nodes[:2], ["Недостаточно аннотаций"])  # Ошибка!
except ValueError as e:
    print("Ловим ошибку аннотации:", e)
