# -*- coding:utf-8 -*-
# ���庯��
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):  #ȱ��ð��
    """Prints the first word after popping it off."""
    word = words.pop(0)   #��һ������poop�޸�Ϊpop
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)	#�ڶ�����������ȱ�������ţ�
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 5
print "This should be five: %d" % five   #����������%s��ʽ��������ַ��ģ�����Ӧ��ʹ��:%d

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000	#���Ĵ����󣺳�������д����Ӧ����"/"������"\"
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) #���崦���󣺲���������д����Ӧ����start_point������start-point,"=="�޸�Ϊ"="

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)   #������������д���󣬲���jeans,Ӧ����beans

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)   #���ߴ�����ȱ��"��"������������д����,crabapples�޸�Ϊ"crates"

#�ھŴ�����ȱ�ٵ��뺯�����

import ex25_Practice_Practice
sentence = "All god\tthings come to those who weight."

words = ex25_Practice_Practice.break_words(sentence)
sorted_words = ex25_Practice_Practice.sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)  #��ʮ�����󣺶�"."���ţ�ɾ��
print_last_word(sorted_words)

sorted_words = ex25_Practice_Practice.sort_sentence(sentence)
print  sorted_words    #��ʮһ������prin�޸�Ϊprint 

print_first_and_last(sentence)   #��ʮ��������:����������д����irst�޸�Ϊfirst

   
print_first_and_last_sorted(sentence)  #��ʮ���������ж���ո��"a"�޸�Ϊ"and"��ɾ������������д����"senence"�޸�Ϊ"sentence"
