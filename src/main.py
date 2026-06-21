import argparse
import sys
from second_step import run_second_step

def parse_args():
    parser = argparse.ArgumentParser(description="Консольный индексатор папок")
    parser.add_argument("path", help="Путь к папке для индексации")
    return parser.parse_args()

def main():
    args = parse_args()
    run_second_step(args.path)

if __name__ == "__main__":
    main()