
class HashTable:
    """Implementacija heš tabele koristeći kvadratno sondiranje kao tehniku ponovnog heširanja."""
    
    def __init__(self, size):
        """Inicijalizacija heš tabele sa zadatom veličinom."""
        self.size = size
        self.hash_table = [None]*size
        
    def hash(self, key):
        """Računanje heš vrednosti za zadati ključ."""
        return key % self.size
    
    def rehash(self, old_hash, i):
        """Izvršavanje kvadratnog sondiranja za računanje nove heš vrednosti."""
        return (old_hash + i**2) % self.size
    
    def insert(self, key, value):
        """Ubacivanje para ključ-vrednost u heš tabelu."""
        hash_value = self.hash(key)
        if self.hash_table[hash_value] is None:
            self.hash_table[hash_value] = (key, value)
        else:
            i = 1
            while True:
                new_hash = self.rehash(hash_value, i)
                if self.hash_table[new_hash] is None:
                    self.hash_table[new_hash] = (key, value)
                    break
                else:
                    i += 1
    
    def get(self, key):
        """Dohvatanje vrednosti asociirane sa zadatim ključem iz heš tabele."""
        hash_value = self.hash(key)
        if self.hash_table[hash_value] is not None and self.hash_table[hash_value][0] == key:
            return self.hash_table[hash_value][1]
        else:
            i = 1
            while True:
                new_hash = self.rehash(hash_value, i)
                if self.hash_table[new_hash] is not None and self.hash_table[new_hash][0] == key:
                    return self.hash_table[new_hash][1]
                elif self.hash_table[new_hash] is None:
                    return None
                else:
                    i += 1
                    
                
                
                
                
                
                