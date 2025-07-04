import sys
import yaml
from pathlib import Path

_config = {}

def load_config(config_or_path: dict | str | None = None):
    """
    Загружает конфигурацию и создаёт глобальные переменные с именами из ключей.

    Поддерживает:
    - переданный dict (конфиг напрямую)
    - путь до YAML-файла (str или Path)
    - если ничего не передано, берёт sys.argv[1] и загружает оттуда
    """

    global _config
    source = config_or_path

    # Если явно ничего не передано — берём из аргументов
    if source is None:
        if len(sys.argv) < 2:
            print("❌ Не передан путь до YAML-конфига (ожидался в sys.argv[1])")
            sys.exit(1)
        source = sys.argv[1]

    # Если передан путь — читаем YAML
    if isinstance(source, (str, Path)):
        config_path = Path(source)
        if not config_path.exists():
            print(f"❌ Конфиг-файл не найден: {config_path}")
            sys.exit(1)
        with config_path.open("r") as f:
            _config = yaml.safe_load(f)
    elif isinstance(source, dict):
        _config = source
    else:
        print("❌ Неподдерживаемый тип аргумента в load_config")
        sys.exit(1)

    # Создаём глобальные переменные по ключам
    globals_ = globals()
    for key, value in _config.items():
        globals_[key] = value


def get(key: str, default=None):
    return _config.get(key, default)
