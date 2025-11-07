'''
classe modelo para a categoria
'''

class Categoria:
    def __init__(self, id: int, nome: str):
        self.id = id
        self.nome = nome
    
    def __str__(self):
        return f"categoria: id = {self.id}\n nome da categoria: '{self.nome}'"