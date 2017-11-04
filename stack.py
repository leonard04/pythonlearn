class stack:
    def __init__(self):
        self.data=[]
    def __len__(self):
        return len(self.data)
    def isEmpty(self):
        return len(self.data) == 0
    def push(self,value):
        self.data.append(value)
    def top(self):
        if self.isEmpty():
            raise Exception('Stack kosong')
        return self.data[-1]
    def pop(self):
        if self.isEmpty():
            raise Exception('Stack kosong')
        return self.data.pop()
    def __repr__(self):
        return repr(self.data)

s=stack()
print s
s.push('uwiw')
print s
s.push('baru')
print s
print "element '",s.pop(),"'","diambil"
print s