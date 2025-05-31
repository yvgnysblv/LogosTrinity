def map_sense(stream, func):
    """
    Применяет func ко всем узлам потока (stream).
    """
    return [func(node) for node in stream]

def reduce_sense(stream, func, initial):
    """
    Агрегирует поток (stream) функцией func, начиная с initial.
    """
    acc = initial
    for node in stream:
        acc = func(acc, node)
    return acc
