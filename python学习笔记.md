Python 的语法特点

1、Python 的代码块不使用大括号{}来控制类，函数以及其他逻辑判断。

Python的特色是：用**缩进**了写模块。 

**缩进的空白数量是可变的，但是所有代码块语句必须包含相同的空白数量。**（必须严格执行。）

	#!/usr/bin/python
	# -*- coding: UTF-8 -*-
	# 文件名：test.py

	 if True:
	    print "Answer"
	    print "True"
	else:
	    print "Answer"
	    # 没有严格缩进，在执行时会报错
	  print "False"
	  
	  
因此，在 Python 的代码块中必须使用**相同数目的行首缩进空格数**。
建议你在每个缩进层次使用 单个制表符 或 两个空格 或 四个空格 , 切记不能混用


class Employee:
  	   empCount = 0
  	   
  	   # 创建对象的时候就会调用
  	   def __init__ (self, name, salary)
	  	  	self.name = name
	  	  	self.salary = salary
	  	  	Employee.empCount += 1
  	  	
  	  	def displayCount(self):
  	  	 	print "Total Employee %d" % Employee.empCount 
  	  	 	
  	  	def displayEmployee(self):
  	  		print "Name:", self.name, ", Salary:", self.salary
  	  		
class C (Employee)://这个继承也是足够简单

运算符重载。 可以重写， 运算符规则。 这也是狠厉害了。




  	  		
	
	
