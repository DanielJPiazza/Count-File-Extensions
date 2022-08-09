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
    # objects
    count = Counter()
    parser = argparse.ArgumentParser()
    
    # cli arguments
    parser.add_argument("-d", "--directory", help="directory path the program will target", type=str, required=True)
    parser.add_argument("-e", "--extensions", nargs="+", help="only count specified extensions (space-separated)")
    parser.add_argument("-H", "--hidden_disabled", help="skip all hidden files (defined by '.' prefix)", action="store_true", default=False)
    parser.add_argument("-s", "--sort_alphabetically", help="sort output (a-z) by extension", action="store_true", default=False)

    # cli argument parsing
    args = parser.parse_args()
    dir = os.path.abspath(args.directory)
    extensions = args.extensions
    exts = extensions if extensions is not None else "All"
    skip_hidden = args.hidden_disabled
    sort_alphabetically = args.sort_alphabetically
    sort = "A-Z" if sort_alphabetically else "Frequency"

    # exit if specified path doesn't exist
    if not os.path.exists(dir):
        print(f"\nThe following path does not exist: {dir}\n\nExiting...\n")
        sys.exit()

    # print specified options
    print(f"\nDIRECTORY:\t{dir}")
    print(f"SKIP HIDDEN:\t{skip_hidden}")
    print(f"EXTENSIONS:\t{exts}")
    print(f"SORT:\t\t{sort}\n")

    # count files
    file_count_sum = 0
    for dirpath, dirnames, filenames in os.walk(dir):
        
        # filter for specified file extensions
        if extensions is not None:
            filenames = [f for f in filenames if f.endswith((tuple(extensions)))]
        
        # skip hidden files (defined by '.' prefix)
        if skip_hidden:
            filenames = [f for f in filenames if not f[0] == '.']
        
        for filename in filenames:
            root, ext = os.path.splitext(filename)
            if ext is None or ext == "":
                ext = "no_ext"
            ext = ext.strip(".").upper()
            count[ext] += 1
            file_count_sum += 1

    print(f"{'EXTENSION':{const.EXT_COL_WIDTH}}|{'COUNT':>{const.EXT_COL_WIDTH}}")
    print_divider()

    # decide how to sort output
    if sort_alphabetically:
        output = sorted(count.items(), key=lambda pair: pair[0])
    else:
        output = count.most_common()
    
    # print results
    for ext_name, count in output:
        print(f"{ext_name:{const.EXT_COL_WIDTH}}|{count:>{const.COUNT_COL_WIDTH}}")

    print_divider()
    print(f"{'TOTAL':{const.EXT_COL_WIDTH}} {file_count_sum:>{const.COUNT_COL_WIDTH}}\n")

if __name__ == '__main__':
    main()