import os

def collect_files(path, file_list, extension=None):
    """
    Рекурсивно обходит папку и наполняет file_list путями файлов.
    Если extension задан (например, 'txt'), включаются только файлы с этим расширением.
    """
    try:
        entries = os.listdir(path)
    except PermissionError:
        return

    for entry in entries:
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            collect_files(full_path, file_list, extension)
        else:
            if extension is not None:
                # Проверяем расширение (без учёта регистра)
                if not full_path.lower().endswith('.' + extension.lower()):
                    continue
            file_list.append(full_path)


def get_all_files_recursive(root_path, extension=None):
    """
    Возвращает список всех файлов (или отфильтрованных по расширению)
    в root_path и подпапках.
    """
    result = []
    collect_files(root_path, result, extension)
    return result