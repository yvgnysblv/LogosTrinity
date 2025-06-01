from core.node import STNNode
from core.stream_ops import map_sense

# Создаём два подпотока (например, для двух параллельных процессов)
substream1 = [STNNode(state=1, annotation="A1"), STNNode(state=0, annotation="A2")]
substream2 = [STNNode(state=-1, annotation="B1"), STNNode(state=1, annotation="B2")]

# Вложенный поток — это список подпотоков
main_stream = [substream1, substream2]

# Применим ускорение ко всем узлам всех подпотоков (двойной map)
def speed_up_all(streams):
    for stream in streams:
        map_sense(stream, lambda n: setattr(n, "tempo", n.tempo * 2))
    return streams

speed_up_all(main_stream)

for i, stream in enumerate(main_stream):
    print(f"Подпоток {i+1}:")
    for node in stream:
        print(node)
