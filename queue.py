class queue:
	def __init__(self):
		self.data=[]
		self.size=0
		self.front=0 #posisi element terdepan
	def __len__(self):
		return self.size
	def isEmpty(self):
		return self.size==0
	def getFirstElement(self):
		if self.isEmpty():
			raise Exception('queue kosong')
		return self.data[self.front]
	def enqueue(self,element):
		self.data.append(element)
		self.size+=1
	def dequeue(self):
		if self.isEmpty():
			raise Exception('queue kosong')
		result = self.data[self.front]
		del self.data[self.front]
		self.size-=1
		return result
	def __repr__(self):
		return repr(self.data)

q = queue()
print q
q.enqueue('leo')
q.enqueue('dzul')
q.enqueue('rangga')
q.enqueue('aslam')
print q
print "jumlah element dalam antrian:",len(q)
print q.getFirstElement()
q.dequeue()
print q