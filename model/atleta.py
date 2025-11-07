from categoria import Categoria
class atletas:
    def __init__(self, id: int, nome: str, categoria: Categoria, email: str,
                idade: int | None = None, altura: float | None = None, 
                peso: float | None = None, ativo: bool = True, observacoes: str | None = None,
                telefone: int | None = None, momento_cadastro: str | None = None):
        self.id = id
        self.nome = nome
        self.email = email
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.ativo = ativo
        self.observacoes = observacoes
        self.telefone = telefone
        self.momento_cadastro = momento_cadastro
        self.categoria = categoria

    def __str__(self):
        return (f"Pessoa id={self.id}\n nome: {self.nome}\n",
                f"email = {self.email}\n idade = {self.idade}",
                f"id da categoria: {self.categoria.id}\n nome da categoria: {self.categoria.id}")

infantil = Categoria(1,"infantil")
jogador1 = atletas(1,"hiago do prado oliveira",infantil,"hiago@gmail.com", 19, 1.75, 58.5, True, None, 988536691, "01 de novembro de 2025")
print(jogador1)