#��ƽ������ķ���
#����һ������
people = [['John',42,'pants'],['James',36],['Sue',38]]
#�������
total_age = 0
#ʹ��forѭ��ȡֵ���������ܺ�
for person in people:
	age = person[1]
	total_age = total_age + age
#���ƽ������ֵ
avg_age = total_age / len(people)
#���ƽ������ֵ
print "Average age:",avg_age