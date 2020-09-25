# diff_files
Simple script that prints files that are not in directory from list of files

## Usage

Create a file with expected files (labeled expectedFiles.txt)

```
# This file contains my expected files
file1.txt
file2.txt
file4.txt
file5.txt
```

```
diff_files <directory> expectedFiles.txt
```

Any files in the expected file path not matching files in the directory will be printed

## Installation:

Clone repository

Add alias `.bashrc`, `.zshrc`, `.alias` file:

```
alias diff_files='python3 <path to repo>/diff_files.py'
```

## Requirements
- python3
