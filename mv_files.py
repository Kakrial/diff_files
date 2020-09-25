import sys
import os
import shutil
import myUtils as mu

def cpFiles(file, dir1, dir2):
    fromDirPath = mu.getPath(dir1)
    if fromDirPath is None:
        return

    toDirPath = os.path.relpath(dir2)
    try:
        os.makedirs(toDirPath)
    except FileExistsError:
        pass

    filePath = mu.getPath(file)
    if filePath is None:
        return

    dirFiles = os.listdir(fromDirPath)
    with open(filePath, 'r') as f:
        fFiles = f.read().splitlines()

    print(f"Copying following files in {filePath}, from {fromDirPath} to {toDirPath}:\n")
    missedFile = 0
    matchedFiles = 0

    print("Missed files:")

    for f in fFiles:
        if f == "\n":
            continue
        if f.startswith("#"):
            continue
        fileToCopy = mu.getPrefixFile(f, dirFiles)
        if fileToCopy is None:
            print(f)
            missedFile += 1
        else:
            matchedFiles += 1
            mu.moveFile(fileToCopy, fromDirPath, toDirPath)
    
    print(f"\nMatched Files:\t{matchedFiles}\nMissing Files:\t{missedFile}\nTotal Files:\t{matchedFiles+missedFile}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: cp_files <files.txt> <from directory> <to directory>")
    else:
        cpFiles(sys.argv[1], sys.argv[2], sys.argv[3])