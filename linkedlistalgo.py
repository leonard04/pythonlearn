class node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

class linked_list:
	def __init__(self):
		self.head=node()

	# menambahkan node baru di list terakhir
	def append(self,data):
		new_node=node(data)
		cur=self.head
		while cur.next!=None:
			cur=cur.next
		cur.next=new_node

	# mengembalikan panjang list(size) dalam integer
	def length(self):
		cur=self.head
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total 

	# cetak dalam sebuah array dengan nama elems 
	def display(self):
		elems=[]
		cur_node=self.head
		while cur_node.next!=None:
			cur_node=cur_node.next
			elems.append(cur_node.data)
		print elems

	# mencari nilai dalam suatu indeks tertentu di dalam array 
	def get(self,index):
		if index>=self.length():
			print "ERROR: 'Get' Index out of range!"
			return None
		cur_idx=0
		cur_node=self.head
		while True:
			cur_node=cur_node.next
			if cur_idx==index: 
				return cur_node.data
			cur_idx+=1

	# Delete node tertentu berdasarkan indeksnya
	def erase(self,index):
		if index>=self.length():
			print "ERROR: 'Erase' Index out of range!"
			return 
		cur_idx=0
		cur_node=self.head
		while True:
			last_node=cur_node
			cur_node=cur_node.next
			if cur_idx==index:
				last_node.next=cur_node.next
				return
			cur_idx+=1

mylist = linked_list()
mylist.append(0)
mylist.append(2)
mylist.append(1)
mylist.append(4)

mylist.display()

print(mylist.get(2))

mylist.display()