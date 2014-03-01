# -*- coding:utf-8 -*-
#定义加、减、乘、除函数
def add(a,b):
	print "ADDING %d + %d" % (a,b)
	return a + b  #返回相关的数值

def subtract(a,b):
	print "SUBTRACTING %d - %d" % (a,b)
	return a - b
	
def multiply(a,b):
	print "MULTIPLYING %d * %d" % (a,b)
	return a * b

def divide(a,b):
	print "DIVDING %d / %d" % (a ,b)
	return a / b
	
	
print "Let's do some math with just fuctions!"
#函数调用传入相关的参数
age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)
#输出函数计算后的结果
print "Age:%d,Height:%d,Weight:%d,IQ:%d" %(age,height,weight,iq)

# A puzzle for the extra credit,type it in anyway.
print "Here is a puzzle."
#再次调用加减乘除函数，要从里往外计算
what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print "That becomes:",what,"Can you do it by hand?"