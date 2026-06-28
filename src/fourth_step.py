import os
from first_step import validate_path
from third_step import compute_file_hash
from utils import get_all_files_recursive

def scan_for_comparison(base_path, extension=None):
    file_hashes = {}
    all_files = get_all_files_recursive(base_path, extension)
    for filepath in all_files:
        rel_path = os.path.relpath(filepath, base_path)
        try:
            file_hashes[rel_path] = compute_file_hash(filepath)
        except (PermissionError, FileNotFoundError):
            pass
    return file_hashes

def run_fourth_step(source_path, backup_path, extension=None):
    is_valid1, msg1 = validate_path(source_path)
    is_valid2, msg2 = validate_path(backup_path)
    if not is_valid1 or not is_valid2:
        print(f"[ОШИБКА] {msg1 if not is_valid1 else msg2}")
        return

    source_files = scan_for_comparison(source_path, extension)
    backup_files = scan_for_comparison(backup_path, extension)

    source_keys = set(source_files.keys())
    backup_keys = set(backup_files.keys())

    missing_in_backup = source_keys - backup_keys
    extra_in_backup = backup_keys - source_keys
    common_keys = source_keys & backup_keys

    changed = []
    identical = []
    for k in common_keys:
        if source_files[k] != backup_files[k]:
            changed.append(k)
        else:
            identical.append(k)

    print("Сравнение с резервной копией:")
    print(f"  Исходная: {source_path}")
    print(f"  Бэкап: {backup_path}\n")

    print("Отсутствуют в бэкапе:")
    if missing_in_backup:
        for f in sorted(missing_in_backup):
            print(f"  - {f}")
    else:
        print("  (нет)")

    print("\nИзменены:")
    if changed:
        for f in sorted(changed):
            print(f"  - {f}")
    else:
        print("  (нет)")

    print("\nЛишние в бэкапе:")
    if extra_in_backup:
        for f in sorted(extra_in_backup):
            print(f"  - {f}")
    else:
        print("  (нет)")

    print(f"\nИдентичных файлов: {len(identical)}")