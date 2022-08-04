import os, argparse, sys
import constant as const
from collections import Counter

# functions
def print_divider():
    print('-' * const.EXT_COL_WIDTH,end = "")
    print("+",end = "")
    print('-' * const.COUNT_COL_WIDTH)

# main
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", "-d", help="The directory path the program will target.", type=str, default=" ")
    args = parser.parse_args()
    dir = args.directory

    count = Counter()

    if not os.path.exists(dir):
        print(f"\nThe following path does not exist: {dir}\n\nExiting...\n")
        sys.exit()

    print(f"\nCounting file extensions recursively in: {dir}\n")

    file_count_sum = 0
    for dirpath, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            root, ext = os.path.splitext(filename)
            if ext is None or ext == "":
                ext = "no_ext"
            ext = ext.strip(".").upper()
            count[ext] += 1
            file_count_sum += 1

    print(f"{'EXTENSION':{const.EXT_COL_WIDTH}}|{'COUNT':>{const.EXT_COL_WIDTH}}")
    print_divider()

    for ext_name, count in count.most_common():
        print(f"{ext_name:{const.EXT_COL_WIDTH}}|{count:>{const.COUNT_COL_WIDTH}}")

    print_divider()
    print(f"{'TOTAL':{const.EXT_COL_WIDTH}} {file_count_sum:>{const.COUNT_COL_WIDTH}}\n")

if __name__ == '__main__':
    main()