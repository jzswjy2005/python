# -*- coding:utf-8 -*-
#定义一个函数
def cheese_and_crackers(cheese_count,boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
print "We can just give the function numbers directly:"
#传递参数第一次
cheese_and_crackers(20,30)

print "OR,we can use variables from our script:"
#定义2个变量并赋值，传递参数第二次
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can even do math inside too:"
#传递参数第三次
cheese_and_crackers(10 + 20,5 + 6)

print "And we can combine the two,variables and math:"
#传递参数第四次
cheese_and_crackers(amount_of_cheese + 100,amount_of_crackers + 1000)

