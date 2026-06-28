import os
from datetime import datetime
from first_step import validate_path
from utils import get_all_files_recursive

def get_file_metadata(filepath):
    stat = os.stat(filepath)
    size = stat.st_size
    mtime = stat.st_mtime
    mtime_str = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S")
    return {
        "path": filepath,
        "size": size,
        "mtime": mtime_str
    }

def scan_directory(path, extension=None):
    files_metadata = []
    all_files = get_all_files_recursive(path, extension)
    for filepath in all_files:
        try:
            meta = get_file_metadata(filepath)
            files_metadata.append(meta)
        except (PermissionError, FileNotFoundError):
            pass
        except Exception as e:
            print(f"ВНИМАНИЕ! Ошибка у файла {filepath}: {e}")
    return files_metadata

def run_second_step(path, extension=None):
    is_valid, message = validate_path(path)
    if not is_valid:
        print(f"[ОШИБКА] {message}")
        return
    metadata_list = scan_directory(path, extension)
    print(f"Найдено файлов: {len(metadata_list)}\n")
    for meta in metadata_list:
        print(f"Файл: {meta['path']}")
        print(f"  Размер: {meta['size']} байт")
        print(f"  Изменён: {meta['mtime']}")
        print()
    return metadata_list