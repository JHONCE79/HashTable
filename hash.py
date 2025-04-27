class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

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
        new_node = Node(key, value)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            new_node.next = self.table[index]
            self.table[index] = new_node

    def search(self, key):
        index = self.hash_per(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self.hash_per(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return
            prev = current
            current = current.next
        print("Key not found")

    def __str__(self):
        return str(self.table)
    