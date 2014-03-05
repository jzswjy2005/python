# -*-  coding:utf-8 -*- 
#定义变量cars并赋值
cars = 100
#定义变量space_in_a_car并赋值
space_in_a_car = 4.0
#定义变量drivers并赋值
drivers = 30
#定义变量passengers并赋值
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are",cars,"cars available."
print "There are only",drivers,"drivers available."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."

