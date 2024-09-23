from livro import Livro


class Biblioteca:
    def __init__(self, nome: str, livros: list[Livro]) -> None:
        self.nome = nome
        self.livros = livros

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)

    def remover_livro(self, livro: Livro):
        self.livros.remove(livro)

    def listar_livros(self):
        for livro in self.livros:
            print(f"- {livro.titulo} por {livro.autor} (ISBN: {livro.isbn})")
