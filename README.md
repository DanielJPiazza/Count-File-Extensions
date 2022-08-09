# Count File Extensions
A Python program that counts the frequency of each file extension in a directory (recursive and includes hidden files).

Written and tested on macOS 12.5 in Visual Studio Code, however it is intended to work on Windows and Linux as well.
 
# Usage
```
usage: __main__.py [-h] -d DIRECTORY [-e EXTENSIONS [EXTENSIONS ...]] [-H] [-s]

options:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        directory path the program will target
  -e EXTENSIONS [EXTENSIONS ...], --extensions EXTENSIONS [EXTENSIONS ...]
                        only count specified extensions (space-separated)
  -H, --hidden_disabled
                        skip all hidden files (defined by '.' prefix)
  -s, --sort_alphabetically
                        sort output (a-z) by extension
```

# Example
```
>> python3 __main__.py -d /Users/DemoUser/Documents/ExampleDir

DIRECTORY:      /Users/DemoUser/Documents/ExampleDir
SKIP HIDDEN:    False
EXTENSIONS:     All
SORT:           Frequency

EXTENSION |     COUNT
----------+----------
JPG       |     10626
HEIC      |      1226
JPEG      |       200
MP4       |       160
MOV       |        66
PNG       |         5
GIF       |         1
3GP       |         1
----------+----------
TOTAL           12285
```

# To-do
- [X] Add option to skip hidden files (starting with '.')
- [X] Add option to sort output by extension name instead of frequency/count
- [X] Add option to only count specific extensions
- [ ] Add option to disable recursion
- [ ] Add consistent casing for output when extension filtering is used
- [ ] Fix extension filtering only working if input is lowercase