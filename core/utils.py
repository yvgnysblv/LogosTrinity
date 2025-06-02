# stnlib/utils.py
def ensure_callable(func):
    if not callable(func):
        raise TypeError("Функция должна быть вызываемой")
    return func