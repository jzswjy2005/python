# -*- coding:utf-8 -*-
#����ϵͳ����
from sys import argv

script, input_file = argv
#���庯��print_all
def print_all(f):
	print f.read()
#���庯��rewind   seekֻ�Ƕ�λ��0λ���޷���ֵ
def rewind(f):
	f.seek(0)
#���庯��print_a_line   readline��ȡ�ļ���һ��
def print_a_line(line_count,f):
	print line_count,f.readline()
#���ļ�
current_file = open(input_file)

print "First let's print the whole file:\n"
#���ú���print_all�Ҵ�����
print_all(current_file)

print "Now let's rewind,kind of like a tape."
#���ú���rewind�Ҵ�����
rewind(current_file)

print "Let's print three lines:"
#�������
current_line = 1
#���ú���print_a_line�Ҵ�����
print_a_line(current_line,current_file)
#�������
current_line = current_line + 1
#���ú���print_a_line�Ҵ�����
print_a_line(current_line,current_file)
# �������
current_line = current_line + 1
#���ú���print_a_line�Ҵ�����
print_a_line(current_line, current_file)



