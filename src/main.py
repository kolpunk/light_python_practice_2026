import argparse
import sys
from second_step import run_second_step
from third_step import run_third_step
from fourth_step import run_fourth_step

def parse_args():
    parser = argparse.ArgumentParser(description="Консольный индексатор папок")
    parser.add_argument("path", help="Путь к папке для индексации")
    parser.add_argument("--backup", help="Путь к папке с резервной копией для сравнения", default=None)
    parser.add_argument("--ext", help="Фильтр по расширению (например, txt)", default=None)
    return parser.parse_args()

def main():
    args = parse_args()
    ext = args.ext
    # Этап 2: сканирование и метаданные
    run_second_step(args.path, ext)
    # Этап 3: дубликаты
    run_third_step(args.path, ext)
    # Этап 4: сравнение с бэкапом, если указан
    if args.backup:
        run_fourth_step(args.path, args.backup, ext)

if __name__ == "__main__":
    main()