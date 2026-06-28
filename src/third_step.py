import os
import hashlib
from first_step import validate_path
from second_step import scan_directory

def compute_file_hash(filepath, chunk_size=8192):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            sha256.update(chunk)
    return sha256.hexdigest()

def find_duplicates(path, extension=None):
    metadata_list = scan_directory(path, extension)   # передаём фильтр
    hash_to_files = {}
    for meta in metadata_list:
        filepath = meta["path"]
        try:
            file_hash = compute_file_hash(filepath)
            if file_hash not in hash_to_files:
                hash_to_files[file_hash] = []
            hash_to_files[file_hash].append(filepath)
        except (PermissionError, FileNotFoundError):
            pass
    return hash_to_files

def run_third_step(path, extension=None):
    is_valid, message = validate_path(path)
    if not is_valid:
        print(f"[ОШИБКА] {message}")
        return
    hash_to_files = find_duplicates(path, extension)
    duplicates = {h: paths for h, paths in hash_to_files.items() if len(paths) >= 2}
    print(f"Уникальных файлов: {len(hash_to_files)}")
    print(f"Групп дубликатов: {len(duplicates)}\n")
    if not duplicates:
        print("Дубликатов не найдено.\n")
    else:
        for i, (file_hash, paths) in enumerate(duplicates.items(), 1):
            print(f"Дубликаты #{i} (хэш: {file_hash[:16]}...):")
            for p in paths:
                print(f"  - {p}")
            print()
    return hash_to_files