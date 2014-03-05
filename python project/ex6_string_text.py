# -*- coding:utf-8 -*-
# 定义变量x并赋值
x = "There are %d types of people." % 10
# 定义变量binary并赋值
binary = "binary"
# 定义变更do_not并赋值
do_not = "don't"
# 定义变量y并赋值，使用格式化字符引用之前定义的两个变量
y = "Those who know %s and those who %s." % (binary,do_not)
# 输出x的值
print x
# 输出y的值
print y
# 使用格式化字符引用x变量且输出内容
print "I said: %r." % x
#  使用格式化字符引用y变量且输出内容
print "I also said: '%s'." % y
# 定义变量hilarious并赋值
hilarious = False
# 定义变量joke_evaluation并赋值
joke_evaluation = "Isn't that joke so funny?! %r"
# 使用格式化字符引用hilarious变量且输出内容
print joke_evaluation % hilarious
# 定义变量w并赋值
w = "This is the left side of...."
# 定义变量e并赋值
e = "a string with a right side."
# 使用“+”连接2个变量的值
print w + e

