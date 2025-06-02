"""
LogosTrinity core package.
Импортирует основные классы и функции, выводит информативные сообщения, если что-то отсутствует.
"""

def _try_import(module, symbol, required=True):
    try:
        imported = __import__(f".{module}", globals(), locals(), [symbol])
        globals()[symbol] = getattr(imported, symbol)
    except ImportError as e:
        msg = f"Failed to import '{symbol}' from '{module}': {e}"
        if required:
            raise ImportError(msg)
        else:
            print(f"WARNING: {msg}")

# Обязательные модули и функции
_try_import('node', 'STNNode', required=True)
_try_import('ternary_ops', 'trinary_and', required=True)
_try_import('ternary_ops', 'trinary_or', required=True)
_try_import('ternary_ops', 'trinary_not', required=True)
_try_import('ternary_ops', 'superpose', required=True)
_try_import('ternary_ops', 'collapse', required=True)
_try_import('tempo', 'SPEED', required=True)
_try_import('stream_ops', 'map_sense', required=True)
_try_import('stream_ops', 'reduce_sense', required=True)
_try_import('annotation', 'annotate_stream', required=True)

# Пример для опционального модуля (если появится в будущем):
# _try_import('experimental', 'ExperimentalFeature', required=False)
