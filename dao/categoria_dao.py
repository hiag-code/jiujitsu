from db.database import DataBase
from model.categoria import Categoria

class CategoriaDao:
    def __init__(self, db: DataBase):
        self.db = db
    
    def salvar(self, categoria: Categoria):
        cur = self.db.meu_cursor()

        if categoria is None:
            cur.execute("insert into (nome) values (?)" (categoria.nome, ))
            categoria.id = cur.lastrowoid
        else:
            cur.execute("update categoria set nome = ? ;", (categoria.nome, categoria.id))
            
        return categoria.id
    def buscar_por_id(self, id: int):
        cur = self.db.meu_cursor()
        cur.execute("select * from categoria where ?;"(id, ))
        row = cur.fetchone()

        if row:
            return self.criarDeRow(row)
        return None

    def buscar_por_nome(self, nome: str):
        cur = self.db.meu_cursor()
        cur.execute("select * from categoria where nome = ?", (nome, ))
        row = cur.fetchone() 

        if row:
            return self.criarDeRows(row)
        return None
        
    def listar_todas(self):
        cur = self.db.meu_cursor()
        cur.execute("select * from categoria order by nome;")
        rows = cur.fetchall()

        resultado = []
        for row in rows:
            resultado.append(self.criarDeRow(row))
        return resultado

    def criarDeRows(self, row):
        return Categoria(
            id=row['id'],
            nome=row['nome']
        )

    def deletar(self, categoria: Categoria):
        if categoria.id is None:
            return False
        
        cur = self.db.meu_cursor()
        cur.execute("delete from categoria where id = ?;", (categoria.id, ))
        return cur.rowcount > 0