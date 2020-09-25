import sys
import os
import myUtils as mu

def cpFiles(file, dir1, dir2):
    fromDirPath = mu.getPath(dir1)
    if fromDirPath is None:
        return

    toDirPath = os.path.relpath(dir2)
    os.makedirs(toDirPath)

    filePath = mu.getPath(file)
    if filePath is None:
        return

    dirFiles = os.listdir(fromDirPath)
    with open(filePath, 'r') as f:
        fFiles = f.read().splitlines()

    print("Following files missing in directory:\n")
    cpFiles = 0
    matchedFiles = 0

    for f in fFiles:
        if f == "\n":
            continue
        if f.startswith("#"):
            continue
        if not mu.containsPrefix(f, dirFiles):
            print(f)
            cpFiles += 1
        else:
            matchedFiles += 1
    
    print(f"\nMatched Files:\t{matchedFiles}\nMissing Files:\t{cpFiles}\nTotal Files:\t{matchedFiles+cpFiles}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: cp_files <files.txt> <from directory> <to directory>")
    else:
        cpFiles(sys.argv[1], sys.argv[2], sys.argv[3])