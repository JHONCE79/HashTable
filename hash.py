class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)] 

    def hash_multiplicativa(self,key):
        aurea = 0.6180339887
        hash_value = int(hash(key) * aurea) % self.size
        return hash_value
    
    def hash_XOR(self,key):
        hash_value = 0
        for i in key:
            hash_value ^= (hash_value << 3) + (hash_value >> 7) + ord(i)
        return hash_value % self.size

    def hash_per(self,key):
        byte_data = str(key).encode()
        byte_sum = sum(byte_data)
        return (byte_sum * 31) % self.size
    
    def mi_hash(self, key):
        suma = 0
        for letra in str(key):
            suma += ord(letra)
        return suma % self.size


    def insert(self, key, value):
            index = self.hash_per(key)
            for pair in self.table[index]:
                if pair[0] == key:
                    pair[1] = value
                    return
            self.table[index].append([key, value])

    def search(self, key):
            index = self.hash_per(key)
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]  
            return None  


    def delete(self, key):
            index = self.hash_per(key)
            for i, pair in enumerate(self.table[index]):
                if pair[0] == key:
                    del self.table[index][i]  
                    return
            print("Key not found")

    def __str__(self):
        return str(self.table)
    