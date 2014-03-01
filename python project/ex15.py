#!/usr/bin/env python

class inputTest:
	
	def rawString(self):
		self.input = raw_input("please input:")
		print self.input
		print "%s" % self.input
		print "%10.3s" % self.input
		print "%.3s" % self.input
		print "%s" % self.input
	
	
	def rawInt(self):
		self.input = int(raw_input('please input int:'))
		print self.input
		
	def rawFloat(self):
		self.input = float(raw_input('please input float:'))
		print self.input
	
	def run(self):
		self.rawString()
		self.rawInt()
		self.rawFloat()
		
input = inputTest()
input.run()