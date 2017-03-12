# encoding: utf-8
# 本程序为书中分析林肯演说的程序

import string

def addWord(w, wcDict):
    if w in wcDict:
        wcDict[w] += 1
    else:
        wcDict[w] = 1

def processLine(line,wcDict):
    line = line.strip()
    wordList = line.split()
    for word in wordList:
        if word != '--':
            word = word.lower()
            word = word.strip()
            word = word.strip(string.punctuation)
            addWord(word,wcDict)
def prettyPrint(wcDict):
    valkeyList=[]
    for key,val in wcDict.items():
        valkeyList.append((val,key))
    valkeyList.sort(reverse=True)
    print '%-10s%10s'%('Word','Count')
    print '_'*21
    for val,key in valkeyList:
        print '%-12s    %3d'%(key,val)



