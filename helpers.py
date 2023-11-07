from datetime import datetime

def getVer():
    with open('CHANGELOG.md', 'r') as f:
        changes = f.readlines()
        vLine = changes[6]
        version = vLine[4:9]
        return version
    
def getLog():
    with open('CHANGELOG.md', 'r') as f:
        changelog = f.readlines()
        return changelog
    
def timestamp():
    cTime = datetime.now()
    print(f'{cTime}')
    print(f'----------')
    
