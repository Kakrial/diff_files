import os
import shutil

def getPath(resource) -> str:
    dirPath = os.path.relpath(resource)
    if not os.path.exists(dirPath):
        print(f"{dirPath}: file or directory doesn't exist")
        return None
    return dirPath

def containsPrefix(value: str, cmpList:list) -> bool:
    pref = value.split(".")[0]
    val: str
    for val in cmpList:
        if val.startswith(pref):
            return True
    return False

def getPrefixFile(value: str, cmpList:list) -> str:
    pref = value.split(".")[0]
    val: str
    for val in cmpList:
        if val.startswith(pref):
            return val
    return None

def moveFile(name: str, fromPath: str, toPath: str):
    name1 = fromPath + "/" + name
    name2 = toPath + "/" + name
    shutil.move(name1, name2)