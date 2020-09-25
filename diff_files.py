import sys
import os
import myUtils as mu

def missingFiles(dir1, file):
    dirPath = mu.getPath(dir1)
    if dirPath is None:
        return
    filePath = mu.getPath(file)
    if filePath is None:
        return

    dirFiles = os.listdir(dirPath)
    with open(filePath, 'r') as f:
        fFiles = f.read().splitlines()

    print("Following files missing in directory:\n")
    missingFiles = 0
    matchedFiles = 0

    for f in fFiles:
        if f == "\n":
            continue
        if f.startswith("#"):
            continue
        if not mu.containsPrefix(f, dirFiles):
            print(f)
            missingFiles += 1
        else:
            matchedFiles += 1
    
    print(f"\nMatched Files:\t{matchedFiles}\nMissing Files:\t{missingFiles}\nPercentage:\t{(int)(matchedFiles/(matchedFiles+missingFiles)*100)}%\nTotal Files:\t{matchedFiles+missingFiles}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: diff_files <directory to check> <files.txt>")
    else:
        missingFiles(sys.argv[1], sys.argv[2])