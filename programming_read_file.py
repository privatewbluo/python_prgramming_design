###
###  读取文件
###  2021.01.16

import os
import sys
print(sys.path)
print(os.getcwd())
print(__file__)

file = open('浏览器.txt',encoding='UTF-8')
data = file.read()
line = file.readline()
print(data)
print('##############')
print('realine output{}'.format(file.readline()))
while line:
    print(line)
    line = file.readline()
file.close()
print()