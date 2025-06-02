# stnlib/pipeline.py
from typing import TypeVar, Callable, Iterable
from .stream_ops import map_sense, reduce_sense

T = TypeVar('T')
U = TypeVar('U')

class StreamPipeline:
    def __init__(self, source: Iterable[T]):
        self.source = source

    def map(self, func: Callable[[T], U]) -> 'StreamPipeline':
        self.source = map_sense(self.source, func)
        return self

    def filter(self, func: Callable[[T], bool]) -> 'StreamPipeline':
        self.source = [x for x in self.source if func(x)]
        return self

    def reduce(self, func: Callable[[U, T], U], initial: U) -> U:
        return reduce_sense(self.source, func, initial)

    def collect(self) -> list:
        return list(self.source)

    @classmethod
    def of(cls, iterable: Iterable[T]) -> 'StreamPipeline':
        return cls(iterable)