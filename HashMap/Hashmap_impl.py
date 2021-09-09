class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __setitem__(self, key, val):
       h = self.get_hash(key)
       self.arr[h] = val

    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()
print("Hash value for key {} is  : {}".format("march 6",t.get_hash("march 6")))

# setting the value for key = 'march 6'
t['march 6'] = 310

# getting the value for key = 'march 6'
print(t['march 6'])

# returns none if there is no value for key in array
print(t['dec 5'])

# deleting the value
del t['march 6']

# checking if it is deleted
print(t['march 6'])




