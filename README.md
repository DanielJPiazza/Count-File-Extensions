# Count File Extensions
A Python program that counts the frequency of each file extension in a directory (recursive and includes hidden files).

Written and tested on macOS 12.5, however it is intended to work on Windows and Linux as well.
 
# Usage
```
usage: __main__.py [-h] [--directory DIRECTORY]

options:
  -h, --help            show this help message and exit
  --directory DIRECTORY, -d DIRECTORY
                        The directory path the program will target.
```

# Example
```
>> python3 __main__.py -d /Users/DemoUser/Documents/ExampleDir

Counting file extensions recursively in: /Users/DemoUser/Documents/ExampleDir

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