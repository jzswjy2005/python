#求平均年龄的方法
#定义一个数组
people = [['John',42,'pants'],['James',36],['Sue',38]]
#定义变量
total_age = 0
#使用for循环取值算出年龄的总和
for person in people:
	age = person[1]
	total_age = total_age + age
#算出平均年龄值
avg_age = total_age / len(people)
#输出平均年龄值
print "Average age:",avg_age