import os
from datetime import datetime
from first_step import validate_path


def get_file_metadata(filepath):
    """Собирает метаданные для одного файла."""
    stat = os.stat(filepath)
    size = stat.st_size
    mtime = stat.st_mtime
    mtime_str = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S")

    return {
        "path": filepath,
        "size": size,
        "mtime": mtime_str
    }


def scan_directory(path):
    """Обходит папку и собирает метаданные файлов."""
    files_metadata = []

    for root, dirs, files in os.walk(path):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                meta = get_file_metadata(filepath)
                files_metadata.append(meta)
            except (PermissionError, FileNotFoundError):
                pass
            except Exception as e:
                print(f"ВНИМАНИЕ! Ошибка у файла {filepath}: {e}")

    return files_metadata


def run_second_step(path):
    """Этап 2: сканирование папки и вывод метаданных."""
    is_valid, message = validate_path(path)
    if not is_valid:
        print(f"[ОШИБКА] {message}")
        return

    metadata_list = scan_directory(path)

    print(f"Найдено файлов: {len(metadata_list)}\n")

    for meta in metadata_list:
        print(f"Файл: {meta['path']}")
        print(f"  Размер: {meta['size']} байт")
        print(f"  Изменён: {meta['mtime']}")
        print()

    return metadata_list