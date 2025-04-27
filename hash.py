class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size


    def hash_multiplicativa(self,key):
        aurea = 0.6180339887
        hash_value = int(hash(key) * aurea) % self.size
        return hash_value
    
    def hash_XOR(self,key):
        hash_value = 0
        for i in key:
            hash_value ^= hash_value << 3 + hash_value >>7 + ord(i)
        return hash_value

    def hash_per(self,key):
        byte_data = str(key).encode()
        byte_sum = sum(byte_data)
        return (byte_sum * 31) % self.size

    def insert(self, key, value):
        index = self.hash_multiplicativa(key)
        
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key: 
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
            if index == original_index:  
                raise Exception("HashTable is full")
        
        self.table[index] = (key, value)



    def __str__(self):
        return str(self.table)
    