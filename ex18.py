# this one is like your scripts with argv

def print_two(*args):
    arg1, arg2 = args
	print "arg1:%r, arg2: %r" %(arg1, arg2)

# ok , that *argv is actually pointless, we can just do this 

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2:%r" %(arg1, arg2)

# this just takes one argument 
def print_one(arg1):
	print "arg1:%r" % arg1
	
# this one takes no arguments
def print_none():
	print "I got nothing."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

# python 函数是用固定格格式来表示的，函数体必须有4个空格。

# 2017-06-09 15:10:01
