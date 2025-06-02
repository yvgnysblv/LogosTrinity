from typing import Callable, Any, List, Iterable, Union

# --- Типы для удобства ---
Stream = List[Any]  # например, List[STNNode]
Reducer = Callable[[Any, Any], Any]
Mapper = Callable[[Any], Any]


def map_sense(stream: Iterable, func: Mapper) -> List:
    """
    Применяет функцию `func` ко всем элементам потока.
    
    :param stream: Итерируемый объект (например, список узлов)
    :param func: Функция, принимающая элемент из stream
    :return: Новый список результатов
    :raises TypeError: если аргументы неверны
    """
    if not isinstance(stream, Iterable):
        raise TypeError("stream должен быть итерируемым объектом")
    if not callable(func):
        raise TypeError("func должен быть вызываемым объектом")

    return [func(item) for item in stream]


def reduce_sense(stream: Iterable, func: Reducer, initial: Any) -> Any:
    """
    Агрегирует значения потока с помощью функции `func`.
    
    :param stream: Итерируемый объект
    :param func: Функция редукции, принимающая аккумулятор и элемент
    :param initial: Начальное значение аккумулятора
    :return: Результат редукции
    :raises TypeError: если аргументы неверны
    """
    if not isinstance(stream, Iterable):
        raise TypeError("stream должен быть итерируемым объектом")
    if not callable(func):
        raise TypeError("func должен быть вызываемым объектом")

    acc = initial
    for item in stream:
        acc = func(acc, item)
    return acc


def lazy_map_sense(stream: Iterable, func: Mapper):
    """
    Ленивая версия map_sense — возвращает генератор.
    
    :param stream: Итерируемый объект
    :param func: Функция преобразования
    :yield: Преобразованные элементы по одному
    """
    if not isinstance(stream, Iterable):
        raise TypeError("stream должен быть итерируемым объектом")
    if not callable(func):
        raise TypeError("func должен быть вызываемым объектом")

    for item in stream:
        yield func(item)


def pipeline(stream: Iterable, *funcs: Union[Mapper, Reducer]) -> Any:
    """
    Последовательное применение функций к потоку.
    
    Пример:
        pipeline(stream, map_sense(f), reduce_sense(g, 0))
    
    :param stream: Входной поток
    :param funcs: Функции, которые будут применены последовательно
    :return: Результат последней функции
    """
    result = stream
    for func in funcs:
        if func.__code__.co_argcount == 2 and not isinstance(func, Reducer):
            # Если это reduce (требует два аргумента)
            result = func(result, next(filter(lambda x: x != 'initial', []), None))
        else:
            result = func(result)
    return result