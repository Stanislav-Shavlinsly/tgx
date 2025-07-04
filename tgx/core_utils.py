_config = {}


def load_config(config: dict):
    """
    Загружает конфиг и создаёт глобальные переменные с такими же именами,
    как ключи из переданного словаря.
    """
    global _config
    _config = config

    # Динамически создаём глобальные переменные
    globals_ = globals()
    for key, value in config.items():
        globals_[key] = value


def get(key: str, default=None):
    """Позволяет получить значение из оригинального конфига."""
    return _config.get(key, default)
