from model.atleta import atletas
from dao.categoria_dao import categoria_Dao
from db.database import DataBase
from model.categoria import Categoria

class AtletaDao:
    def __init__(self, db = DataBase):
        self.db = db

    def salvar(self, atleta: atletas):
        cur = self.db.meu_cursor()

        ativoInt = 1 if atleta.ativo else 0
        categoriaId =  atleta.categoria.id

        if atletas.id is None:
            cur.execute("""insert into participante(nome, genero, idade, altura, peso, telefone, e_mail, observacao, ativo, categoria_id)
            values (?,?,?,?,?,?,?,?,?,?);
            """, (atleta.nome, atleta.genero, atleta.idade, atleta.altura, atleta.peso, atleta.telefone, atleta.email, atleta.observacoes, atleta.ativo, categoriaId))
            atleta.id = cur.lastrowid
        else:
            cur.execute("""
            update participante set nome = ?, genero = ?, idade = ?, altura = ?, peso = ?, telefone = ?, e_mail = ?, ativo = ?, categoria_id = ?
            where id = ?;
            """, (atleta.nome, atleta.genero, atleta.idade, atleta.altura, atleta.peso, atleta.telefone, atleta.email, atleta.observacoes, atleta.ativo, categoriaId
            , atleta.id))

        return atleta.id
    
    def buscarId(self, id: int):
        cur = self.db.meu_cursor()
        cur.execute("select * from participante where id = ?;", (id, ))
        row = cur.fetchone()

        if row:
            return self.criarDeRow(row)
        return None
    
    def buscar_por_nome(self, nome: str):
        cur = self.db.meu_cursor()
        cur.execute("select * from participante where nome like ?;",(f'%{nome}%'))
        rows = cur.fetchall()

        resultado = []
        for row in rows:
            resultado.append(self.criarDeRow(row))
        return resultado
    
    def listarTodas(self, comCategoria: bool =  False):
        cur = self.db.meu_cursor()

        if comCategoria:
            cur.execute(
                '''
                select p.*, c.nome as categoria_nome
                from participante p
                join categoria c on p.categoria_id = c.id
                order by p.nome;
                '''
            )
        else:
            cur.execute("select * from  participante order by nome;")

        rows = cur.fetchall()
        resultado = []
        
        for row in rows:
            resultado.append(self.criarDeRow(row))
        
        return resultado
    
    def buscarCategoria(self, categoriaId: int):
        cur = self.db.meu_cursor()
        cur.execute("select * from  participante where categoria_id = ? order by nome;"(categoriaId))
        rows = cur.fetchall()
        
        resultado = []
        for row in rows:
            resultado.append(self.criarDeRow(row))
        return resultado

    def criarDeRow(self, row):
        categoriaDao = categoria_Dao(self.db)
        categoria = categoriaDao.buscar_por_id(row['categoria_id'])
        
        return atletas(
            id=row['id'],
            nome=row['nome'],
            genero=row['genero'],
            email=row['email'],
            idade=row['idade'],
            altura=row['altura'],
            peso=row['peso'],
            ativo=bool(row['ativo']),
            observacoes=row['observacoes'],
            telefone=row['telefone'],
            categoria=categoria,
            momento_cadastro=row['momento_cadastro']
        )
    
    def deletar(self, atleta: atletas):        
        cur = self.db.cursor()
        cur.execute("DELETE FROM pessoa WHERE id = ?;", (atletas.id,))

        return cur.rowcount > 0
    
    def obterCategoria(self, categoria: Categoria):
        return categoria.categoria


