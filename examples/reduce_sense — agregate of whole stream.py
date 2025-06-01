from core.stream_ops import reduce_sense

# Например, считаем сумму всех состояний (state)
total = reduce_sense(stream, lambda acc, node: acc + node.state, 0)
print("Сумма state во всём потоке:", total)
