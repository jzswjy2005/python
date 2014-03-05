#  -*- coding:utf-8 -*-
#导入2个方法
from sys import argv
from os.path import exists
#定义2个变量
script,from_file, to_file = argv
#格式化字符
#print "Copying from %s to %s" %(from_file, to_file)

# we could do these two on one line too,how?
#使用变量来存储文件的内容
in_file = open(from_file)
#打开文件
indata = in_file.read()
#读取文件
#一段英文解释
print "The input file is %d bytes long" % len(indata)

print "Does the output file exist?%r" % exists(to_file)
print "Ready, hit RETURN to confinue, CTRL-C TO abort."
raw_input()#获取键盘的输入值
#使用变量来存储文件的内容
#以写的方式打开文件
out_file = open(to_file,'w')
#写入文件内容
out_file.write(indata)

print "Alright,all done."
#正常关闭文件
out_file.close()
in_file.close()

