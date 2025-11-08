import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.database import DataBase
from dao.categoria_dao import CategoriaDao
from model.categoria import Categoria

class CategoriaService:
    def __init__(self, db: DataBase):
        self.db = db
        self.CategoriaDao = CategoriaDao(db)
    
    def exibir_menu(self):
        """Exibe o menu principal de opções"""
        print("\n" + "="*50)
        print("  SISTEMA DE GERENCIAMENTO DE CATEGORIAS")
        print("="*50)
        print("1. Criar categoria")
        print("2. Listar todas as categorias")
        print("3. Buscar categoria por ID")
        print("4. Buscar categoria por nome")
        print("5. Atualizar categoria")
        print("6. Deletar categoria")
        print("0. Sair")
        print("="*50)
    
    def criar_categoria(self):
        """Solicita dados do usuário e cria uma nova categoria"""
        print("\n--- CRIAR CATEGORIA ---")
        nome = input("Digite o nome da categoria: ").strip()
        
        if not nome:
            print("Erro: O nome da categoria não pode ser vazio!")
            return
        
        try:
            # Verificar se já existe uma categoria com esse nome
            categoriaExistente = self.categoriaDao.buscarPorNome(nome)
            if categoriaExistente:
                print(f"Erro: Já existe uma categoria com o nome '{nome}' (ID: {categoriaExistente.id})")
                return
            
            # Criar nova categoria
            categoria = Categoria(id=None, nome=nome)
            categoriaId = self.categoriaDao.salvar(categoria)
            print(f"Categoria criada com sucesso!")
            print(f"   ID: {categoriaId}")
            print(f"   Nome: {categoria.nome}")
        
        except Exception as e:
            print(f"Erro ao criar categoria: {e}")
    
    def CriarCategorias(self):
        """Solicita dados do usuário e cria uma nova categoria"""
        print("\n--- CRIAR CATEGORIA ---")
        nome = input("Digite o nome da categoria: ").strip()
        
        if not nome:
            print("Erro: O nome da categoria não pode ser vazio!")
            return
        
        try:
            # Verificar se já existe uma categoria com esse nome
            categoriaExistente = self.categoriaDao.buscarPorNome(nome)
            if categoriaExistente:
                print(f"Erro: Já existe uma categoria com o nome '{nome}' (ID: {categoriaExistente.id})")
                return
            
            # Criar nova categoria
            categoria = Categoria(id=None, nome=nome)
            categoriaId = self.categoriaDao.salvar(categoria)
            print(f" Categoria criada com sucesso!")
            print(f"   ID: {categoriaId}")
            print(f"   Nome: {categoria.nome}")
        
        except Exception as e:
            print(f"Erro ao criar categoria: {e}")
        
    def listarCategorias(self):
        """Lista todas as categorias cadastradas"""
        print("\n--- LISTAR TODAS AS CATEGORIAS ---")
        
        try:
            categorias = self.categoriaDao.listarTodas()
            
            if not categorias:
                print(" Nenhuma categoria cadastrada.")
                return
            
            print(f"\nTotal de categorias: {len(categorias)}")
            print("\n" + "-"*50)
            print(f"{'ID':<5} | {'Nome':<30}")
            print("-"*50)
            
            for categoria in categorias:
                print(f"{categoria.id:<5} | {categoria.nome:<30}")
            
            print("-"*50)
        
        except Exception as e:
            print(f" Erro ao listar categorias: {e}")
    
    def buscarPorId(self):
        """Solicita um ID e busca a categoria correspondente"""
        print("\n--- BUSCAR CATEGORIA POR ID ---")
        
        try:
            idStr = input("Digite o ID da categoria: ").strip()
            categoriaId = int(idStr)
            
            categoria = self.categoriaDao.buscarPorId(categoriaId)
            
            if categoria:
                print("\n Categoria encontrada:")
                print(f"   ID: {categoria.id}")
                print(f"   Nome: {categoria.nome}")
            else:
                print(f"Categoria com ID {categoriaId} não encontrada.")
        
        except ValueError:
            print("Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"Erro ao buscar categoria: {e}")
    
    def buscarPorNome(self):
        """Solicita um nome e busca a categoria correspondente"""
        print("\n--- BUSCAR CATEGORIA POR NOME ---")
        
        nome = input("Digite o nome da categoria: ").strip()
        
        if not nome:
            print("❌ Erro: O nome não pode ser vazio!")
            return
        
        try:
            categoria = self.CategoriaDao.buscar_por_nome(nome)
            
            
            if categoria:
                print("\nCategoria encontrada:")
                print(f"   ID: {categoria.id}")
                print(f"   Nome: {categoria.nome}")
            else:
                print(f" Categoria '{nome}' não encontrada.")
        
        except Exception as e:
            print(f"Erro ao buscar categoria: {e}")