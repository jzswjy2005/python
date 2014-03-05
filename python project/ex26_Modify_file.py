# -*- coding:utf-8 -*-
# 定义函数
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):  #缺少冒号
    """Prints the first word after popping it off."""
    word = words.pop(0)   #第一处错误：poop修改为pop
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)	#第二处错误：括号缺少右括号）
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
print "This should be five: %d" % five   #第三处错误：%s格式符是输出字符的，数字应该使用:%d

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000	#第四处错误：除号输入写有误，应该是"/"，不是"\"
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) #第五处错误：参数名称输写有误，应该是start_point，不是start-point,"=="修改为"="

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)   #第六处错误：输写有误，不是jeans,应该是beans

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)   #第七处错误：缺少"）"及参数名称输写有误,crabapples修改为"crates"

#第九处错误：缺少导入函数语句

import ex25_Practice_Practice
sentence = "All god\tthings come to those who weight."

words = ex25_Practice_Practice.break_words(sentence)
sorted_words = ex25_Practice_Practice.sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)  #第十处错误：多"."符号，删除
print_last_word(sorted_words)

sorted_words = ex25_Practice_Practice.sort_sentence(sentence)
print  sorted_words    #第十一处错误：prin修改为print 

print_first_and_last(sentence)   #第十二处错误:函数名称输写有误，irst修改为first

   
print_first_and_last_sorted(sentence)  #第十三处错误：有多余空格和"a"修改为"and"，删除，参数名输写有误，"senence"修改为"sentence"
