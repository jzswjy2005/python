#  -*- coding:utf-8 -*-
#����2������
from sys import argv
from os.path import exists
#����2������
script,from_file, to_file = argv
#��ʽ���ַ�
#print "Copying from %s to %s" %(from_file, to_file)

# we could do these two on one line too,how?
#ʹ�ñ������洢�ļ�������
in_file = open(from_file)
#���ļ�
indata = in_file.read()
#��ȡ�ļ�
#һ��Ӣ�Ľ���
print "The input file is %d bytes long" % len(indata)

print "Does the output file exist?%r" % exists(to_file)
print "Ready, hit RETURN to confinue, CTRL-C TO abort."
raw_input()#��ȡ���̵�����ֵ
#ʹ�ñ������洢�ļ�������
#��д�ķ�ʽ���ļ�
out_file = open(to_file,'w')
#д���ļ�����
out_file.write(indata)

print "Alright,all done."
#�����ر��ļ�
out_file.close()
in_file.close()

