#coding:utf8
class nlist(list):
	def __init__(self,a_name):
		list.__init__([])
		self.name = a_name

	def listme(self):
		print(self)



t = nlist('Jhon')
print(t.name)
t.extend([1,2,3])
t.listme()