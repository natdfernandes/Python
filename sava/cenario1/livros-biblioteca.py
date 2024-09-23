from biblioteca import Biblioteca
from livro import Livro


o_cao_eterno = Livro("o cão eterno", "não sei", "não sei tambem")

biblioteca_swiss_park = Biblioteca("biblioteca swiss park", [o_cao_eterno])

biblioteca_swiss_park.listar_livros()
print("================")

o_cao_eterno2 = Livro("o cão eterno2", "não sei 2", "não sei tambem 2")
biblioteca_swiss_park.adicionar_livro(o_cao_eterno2)

biblioteca_swiss_park.listar_livros()
print("================")
biblioteca_swiss_park.remover_livro(o_cao_eterno2)
biblioteca_swiss_park.listar_livros()

print("================")

