# encoding: utf-8
# 本程序为书中分析林肯演说的程序

from gettysburgAnalysis import*

def main():
    print 'Hello'
    wcDict={}
    data_path = r'E:\Programs\Python\PythonProgramming\PythonProgramming\ThePracticeOfComputingUsingPython\gettysburg.txt'
    fObj = open(data_path,'r')
    for line in fObj:
        processLine(line,wcDict)
    print 'Length:',len(wcDict)
    prettyPrint(wcDict)


main()

