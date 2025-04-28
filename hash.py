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
        result = []
        for i in range(self.size):
            chain = []
            current = self.table[i]
            while current:
                chain.append(f"({current.key}, {current.value})")
                current = current.next
            result.append(f"[{i}]: " + " -> ".join(chain))
        return "\n".join(result)

def find_duplicates(arr):
    tabla = HashTable()
    duplicados = []
    for elemento in arr:
        if tabla.search(elemento) is not None:
            if elemento not in duplicados:
                duplicados.append(elemento)
        else:
            tabla.insert(elemento, True)
    return duplicados


def count_elements(arr):
    tabla = HashTable()
    for elemento in arr:
        cantidad = tabla.search(elemento)
        if cantidad is None:
            tabla.insert(elemento, 1)
        else:
            tabla.delete(elemento)
            tabla.insert(elemento, cantidad + 1)

    resultado = {}
    for i in range(tabla.size):
        actual = tabla.table[i]
        while actual:
            resultado[actual.key] = actual.value
            actual = actual.next
    return resultado



'''
# Crear tabla hash
ht = HashTable()

# Insertar valores
ht.insert("a", 1)
ht.insert("b", 2)
ht.insert("c", 3)
print(ht)
# Buscar valores
print("Buscar 'a':", ht.search("a"))  # debería devolver 1
print("Buscar 'b':", ht.search("b"))  # debería devolver 2
print("Buscar 'c':", ht.search("c"))  # debería devolver 3

# Eliminar 'b'
ht.delete("b")

# Buscar 'b' de nuevo
print("Buscar 'b' después de eliminar:", ht.search("b"))  # debería devolver None

# Mostrar estado de la tabla
print("\nEstado de la tabla hash:")
print(ht)

'''
# Pruebas
if __name__ == "__main__":
    lista1 = ["manzana", "pera", "manzana", "uva", "pera", "pera", "kiwi"]
    lista2 = [1, 2, 3, 4, 5, 2, 1, 6, 7, 2]

    print("Duplicados en lista1:", find_duplicates(lista1))
    print("Duplicados en lista2:", find_duplicates(lista2))

    print("Frecuencia en lista1:", count_elements(lista1))
    print("Frecuencia en lista2:", count_elements(lista2))    
