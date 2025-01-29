#funcionalidade 0 -  menu de opções

print("Bem vindo ao sistema de biblioteca, oque deseja fazer?")
print("1 - Cadastrar Livros")
print("2 - Pesquisar Livros")
print("3 - Alugar livro")
print("4 - devolver livro")


#funcionalidade 1 - cadastrar livros 
#[Requisitos futuro] apenas o ADM poderá cadastrar livros

listaLivros = [{"nome": "Cálculo 2", "autor": "James Stewart"},{"nome": "O homem de giz", "autor": "C.J. Tudor"}]

if input() == "1":
    print("Digite o nome do livro")
    nome = input()
    print("Digite o autor do livro")
    autor = input()
    print("Livro cadastrado com sucesso")
    def cadastrarLivros(nome, autor):
        livroCadastrado = {"nome": nome, "autor": autor}
        listaLivros.append(livroCadastrado)


# funcionalidade 2 - pesquisar livros
elif input() == "2":
    print("Digito o Nome do Livro que deseja pesquisar")
    nomeLivro = input()

    def pesquisarLivro(nomeLivro):
        for livro in listaLivros:
            if livro["nome"] == nomeLivro:
                print(livro)
                return
            print("Livro não encontrado")          
    pesquisarLivro(nomeLivro)
        
elif input() == "3" or input() == "4":
    print("Funcionalidade em desenvolvimento")
    
else:
    print("Opção inválida") 
