from core.node import STNNode
from core.annotation import annotate_stream

# Создаём поток (список) узлов
stream = [
    STNNode(state=0),
    STNNode(state=1),
    STNNode(state=-1)
]

# Массово добавляем аннотации
annotations = ["Начало процесса", "Промежуточный шаг", "Завершение/ошибка"]
annotate_stream(stream, annotations)

print("Поток с аннотациями:")
for node in stream:
    print(node)
