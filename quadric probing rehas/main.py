import HashTable


if __name__ == "__main__":

    hash_tabela = HashTable.HashTable(10)
    
    hash_tabela.insert(5, 'Jabuka')
    hash_tabela.insert(15, 'Banana')
    hash_tabela.insert(25, 'Trešnja')
    hash_tabela.insert(12, 'Kruška')
    
    print(hash_tabela.get(5)) 
    print(hash_tabela.get(12)) 
    print(hash_tabela.get(15))  
    print(hash_tabela.get(25))  
    
