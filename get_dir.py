# -*- coding: utf-8 -*-
"""
Created on Sat Mar 05 20:55:08 2016

@author: Pjer1

for testing the dir
"""
from os.path import basename, isdir
from os import listdir,getcwd,sep
 
def traverse(path, depth=0,dictionary={},keys=[]):
    #print depth* '| ' + '|_', basename(path)
    #print basename(path)
    if(not isdir(path)):
        dictionary[basename(path)]=path
        keys.append(basename(path))
    if(isdir(path)):
        for item in listdir(path):
            traverse(path+sep+item, depth+1,dictionary,keys)

    
if __name__ == '__main__':
    d={}
    traverse(getcwd()+sep+'DataBase',depth=0,dictionary=d)