# -*- coding:utf-8 -*-
# �������x����ֵ
x = "There are %d types of people." % 10
# �������binary����ֵ
binary = "binary"
# ������do_not����ֵ
do_not = "don't"
# �������y����ֵ��ʹ�ø�ʽ���ַ�����֮ǰ�������������
y = "Those who know %s and those who %s." % (binary,do_not)
# ���x��ֵ
print x
# ���y��ֵ
print y
# ʹ�ø�ʽ���ַ�����x�������������
print "I said: %r." % x
#  ʹ�ø�ʽ���ַ�����y�������������
print "I also said: '%s'." % y
# �������hilarious����ֵ
hilarious = False
# �������joke_evaluation����ֵ
joke_evaluation = "Isn't that joke so funny?! %r"
# ʹ�ø�ʽ���ַ�����hilarious�������������
print joke_evaluation % hilarious
# �������w����ֵ
w = "This is the left side of...."
# �������e����ֵ
e = "a string with a right side."
# ʹ�á�+������2��������ֵ
print w + e

