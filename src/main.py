import argparse
import sys
from first_step import run_first_step

def parse_args():
    parser = argparse.ArgumentParser(description="Консольный индексатор папок")
    parser.add_argument("path", help="Путь к папке для индексации")
    return parser.parse_args()

def main():
    args = parse_args()
    if run_first_step(args.path):
        print("Путь корректен")

if __name__ == "__main__":
    main()