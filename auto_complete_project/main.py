from avl_tree import AVLTree
from avl_tree import visualize_avl_tree
from clean_text import clean_text


texto = """Uma idosa de 90 anos que trabalhava como doméstica em uma casa no Grajaú, na Zona Norte do Rio, foi resgatada por uma força-tarefa que envolve o Ministério do Trabalho e Emprego, o Ministério Público do Trabalho e Emprego e agentes da Polícia Federal. O resgate aconteceu no dia 22 de agosto, após uma denúncia anônima.
Segundo os órgãos envolvidos, a vítima é a trabalhadora doméstica mais idosa encontrada em condição de trabalho análogo à escravidão no Brasil. Ela não tinha nenhum vínculo trabalhista registrado.
A idosa, que não teve o nome divulgado, trabalhava para a família há 50 anos, e como empregada doméstica há 16 anos. Ela também cuidava de outra idosa, de mais de 100 anos, que é mãe da sua antiga empregadora.
A idosa dormia em um sofá, caso precisasse se levantar de madrugada para cuidar da mulher de 100 anos. Ela usava um pequeno banheiro localizado na parte externa da casa"""

palavras_sem_parada = clean_text(texto)

avl = AVLTree()
for v in palavras_sem_parada:
    avl.add(v)
print(avl.root.height)

visualize_avl_tree(avl)

prefixo = input("What the prefix that You want to search a word?")
final = avl.search_word(prefixo)
print(final)