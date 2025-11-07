import sqlite3 as sl
class DataBase:
    def __init__(self, dbPath: str = "exemplo.db"):
        self.dbPath = dbPath
        self.con = None

    def connectar(self):
        self.con = sl.connect(self.dbPath)#------isolation_level=None para seria o comit no automatico-----
        self.con.row_factory = sl.Row
        self.con.execute("PRAGMA foreing_keys = ON")

    def fechar(self):
        self.con.close()

    def meu_cursor(self):
        return self.con.cursor()
    
    def criarTabelas(self):
        cur = self.meu_cursor()
        cur.execute(
        '''
        create table if not exists participante
        (
        id_participante integer PRIMARY KEY AUTOINCREMENT, 
        NOME_COMPLETO VARCHAR(150),  
        CPF varchar(11) not null unique,
        GENERO CHAR(9),  
        IDADE integer check(idade> = 4 and idade <= 110),   
        altura real,
        peso real,
        TELEFONE varchar(14),  
        E_MAIL VARCHAR(50),
        observacao text, 
        valor varchar(50),    
        endereco varchar(150),
        momento_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        '''
        )
        cur.execute(
        '''
        create table if not exists categoria(
        id_participante primary key,
        faixa text not null
        )
        '''
        )
        self.con.commit()
    
    def limparTabelas(self):
        cur = self.meu_cursor()
        cur.execute("delete from tabela participante")
        cur.execute("delete from categoria")