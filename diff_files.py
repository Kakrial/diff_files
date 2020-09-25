import sys
import os

def missingFiles(dir1, file):
    dirPath = os.path.relpath(dir1)
    filePath = os.path.relpath(file)
    if not os.path.exists(dirPath):
        print(f"{dirPath}: directory doesn't exist")
        return
    if not os.path.exists(filePath):
        print(f"{filePath}: directory doesn't exist")
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
        # if not dirFiles.__contains__(f):
        #     print(f)
        #     missingFiles += 1
        if not containsPrefix(f, dirFiles):
            print(f)
            missingFiles += 1
        else:
            matchedFiles += 1
    
    print(f"\nMatched Files:\t{matchedFiles}\nMissing Files:\t{missingFiles}\nTotal Files:\t{matchedFiles+missingFiles}")

def containsPrefix(value: str, cmpList:list) -> bool:
    pref = value.split(".")[0]
    val: str
    for val in cmpList:
        if val.startswith(pref):
            return True
    return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: diff_files <directory to check> <files.txt>")
    else:
        missingFiles(sys.argv[1], sys.argv[2])