import os
import sys


def validate_path(path):
    """Проверяет, что путь существует и является директорией."""
    if not os.path.exists(path):
        return False, f"Путь не существует: {path}"
    if not os.path.isdir(path):
        return False, f"Путь не является директорией: {path}"
    return True, "Путь корректен"


def run_first_step(path):
    """Этап 1: приём и проверка пути к папке."""
    is_valid, message = validate_path(path)

    if not is_valid:
        print(f"[ОШИБКА] {message}")
        sys.exit(1)

    return True