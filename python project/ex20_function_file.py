# -*- coding:utf-8 -*-
#导入系统函数
from sys import argv

script, input_file = argv
#定义函数print_all
def print_all(f):
	print f.read()
#定义函数rewind   seek只是定位在0位，无返回值
def rewind(f):
	f.seek(0)
#定义函数print_a_line   readline读取文件的一行
def print_a_line(line_count,f):
	print line_count,f.readline()
#打开文件
current_file = open(input_file)

print "First let's print the whole file:\n"
#调用函数print_all且传参数
print_all(current_file)

print "Now let's rewind,kind of like a tape."
#调用函数rewind且传参数
rewind(current_file)

print "Let's print three lines:"
#定义变量
current_line = 1
#调用函数print_a_line且传参数
print_a_line(current_line,current_file)
#定义变量
current_line = current_line + 1
#调用函数print_a_line且传参数
print_a_line(current_line,current_file)
# 定义变量
current_line = current_line + 1
#调用函数print_a_line且传参数
print_a_line(current_line, current_file)



