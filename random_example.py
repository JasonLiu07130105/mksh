# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 21:50:25 2025

@author: Jason
"""

import os, sys, random, time, shutil
def main(argv):
    creatfile()
    ospath_gettime()
    creatdir()
    
def creatfile():
    writein = open ("random.txt", mode="a")
    a = getnum()
    for i in range(0,len(a)):
        print(a[i], file = writein)
    writein.close()

def getnum():
    nums = list()
    while(True):
        num = random.randrange(1,1001)
        if(num not in nums):
            nums.append(num)
            if(len(nums) == 100):
                return nums

def ospath_gettime():
    rmd = os.path.getmtime("random.txt")
    rmd_time = time.ctime(rmd)   
    cmd = os.path.getctime("random.txt")
    cmd_time = time.ctime(cmd)
    print("最後修改時間：", rmd_time)
    print("最後建立日期：", cmd_time)
    
def creatdir():
    pathdir = 'test'
    pathfile = 'test/random.txt'
    if not os.path.isdir(pathdir):
        os.mkdir('test')
    if os.path.isfile(pathfile):
        count = int(random.uniform(0,1000))
        print(count)
        newfilename = 'random_'+str(count)+'.txt'
        os.rename('test/random.txt', 'test/'+ newfilename)
    shutil.move('random.txt', 'test/') 
    
if __name__ == '__main__':
    main(sys.argv)