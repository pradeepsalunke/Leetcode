class HashTable:
    #constructor
    def __init__(self):
        #max size of dict in python
        self.size = 2
        #creating an empty list
        self.map = [None] * self.size #[[],[],[]]
        print(self.map)

    #hash funcation
    def hash_func(self,key):
        hashed_key=0
        #creating an hash using ASCII value by adding ascii values of each char
        # and by dividing by total size to distribute equally among map -list

        for char in key:
            hashed_key += ord(char)
        return hashed_key%self.size

    #add or set
    def add(self,key,value):
        #get memory address where we wanna store our key, value this address is a hashed one
        hashed_key=self.hash_func(key)
        #map [[slot1],[slot2],[slot3]]
        #slot=[key,value]
        #row==slot==bucket
        slot=[key,value]
        #if the address is empty place our slot in that address
        if self.map[hashed_key] is None:
            self.map[hashed_key] = list([slot])
            return True
        #if data exist on that address then
        #1.check if key are same that is operation of update
        #2.if keys are different then append to the list(chain, linkedList)
        else:
            for pair in self.map[hashed_key]:
                #[key,value]
                #[  0 , 1  ]
                if pair[0]==key:
                    #update
                    pair[1] = value
                    return True
            #else append
            self.map[hashed_key].append(slot)
            return True
    #lookup operation
    def get(self,key):
        #get hash of key  or get location of that key
        hashed_key=self.hash_func(key)
        #if data at location is not none
        if self.map[hashed_key] is not None:
            #get the key value on that address
            for pair in self.map[hashed_key]:
                #if key matchs return value
                if pair[0]==key:
                    return pair[1]
        return None

    def delete(self,key):
        hashed_key=self.hash_func(key)
        if self.map[hashed_key] is None:
            return False
        #we use range because we need index in the list to pop
        for i in range(0,len(self.map[hashed_key])):
            #
            if self.map[hashed_key][i][0]==key:
                self.map[hashed_key].pop(i)
                return True
        return False
    def print(self):
        print('---PHONEBOOK----')
        print(self.map)
        for item in self.map:
            if item is not None:
                print(str(item))

h = HashTable()
h.add('Bob', '567-8888')
h.add('Ming', '293-6753')
h.add('Ming', '333-8233')
h.add('Ankit', '293-8625')
h.add('Aditya', '852-6551')
h.add('Alicia', '632-4123')
h.add('Mike', '567-2188')
h.print()
print(h.get('Mike'))
h.print()
h.delete('Bob')
h.print()












'''
H = HashTable()
H.set('key1','value1')
H.set('key2','value2')
H.set('key3','value3')

H.set(10,'value10')
H.set(20, 'value20')

H['NEWWWWWWWWW'] = 'newwwwwwwww'

print(H['key1'])
print(H[10])
print(H[20])
print(H[30])
print(H.hashmap)
'''