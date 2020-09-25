import os

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
