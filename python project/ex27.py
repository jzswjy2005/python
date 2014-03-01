# -*- coding:utf-8 -*-
#output show
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
#定义变量并赋值
poem = """
\tThe lovely world
with logic so firmly plated
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
#输出变量的内容 
print "----------------"
print poem
print "----------------"
#定义数值变量
five = 10 - 2 + 3 -6
print "This should be five:%s" %five
#定义函数 
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans,jars,crates
#定义变量
start_point = 10000
#调用函数
beans,jars,crates = secret_formula(start_point)
#输出结果
print "With a starting point of:%d" %start_point
print "We'd hava %d beans,%d jars,and %d crates." % (beans,jars,crates)
#定义变量
start_point = start_point / 10
#调用函数
#beans,jars,crates = secret_formula(start_point) 自己添加的语句
print "We can also do that this way:"
print "We'd have %d beans,%d jars,and %d crates." % (beans,jars,crates)



