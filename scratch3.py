import re
import sys
import os

if len(sys.argv)>1:
    pattern = re.compile(sys.argv[1])
    pattern_1 = re.compile(sys.argv[2])

else:
    pattern = re.compile('.')

def repr(dir):
    try:
        files = os.listdir(dir)
    except:
        return
    for file in files:
        line = dir+'/'+file
        if (pattern.search(file)) or ( pattern_1.search(file)):
            lst.append(line)
            print(line)
        if os.path.isdir(line):
            repr(line)
for t in lst:
    
cwd = os.getcwd()
repr(cwd)
