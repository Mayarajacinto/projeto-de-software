from datetime import datetime as datatime

#funcionalidade 0 -  menu de opções

print("Bem vindo ao sistema de biblioteca, oque deseja fazer?")
print("1 - Cadastrar Livros")
print("2 - Pesquisar Livros")
print("3 - Alugar livro")
print("4 - Devolver livro")
print("5 - Cadastar pessoas")
print("6 - Cadastrar evento")
print("7 - Reservar livro")
opcao = input()

#data para teste de multa 
dataLocacao = datatime.strptime("31/01/2025", "%d/%m/%Y")

listaLivros = [{"nome": "Cálculo 2", "autor": "James Stewart", "status": "Disponível"}, {"nome": "O homem de giz", "autor": "C.J. Tudor", "status": "Alugado e Reservado"}]
listaUsuarios = [{"nome": "João", "usuario": "ADM"}] 
listaEventos = [{"nome": "Semana de tecnologia", "data": "20/10/2021", "local": "Auditório", "status": "Em desenvolvimento"}]
   
#Fucionalidade 1 - cadastrar livros
#[Requisitos futuro] apenas o ADM poderá cadastrar livros
#[Requisitos futuro] banco de dados para armazenar livros
def cadastrarLivros(nome, autor):
    livroCadastrado = {"nome": nome, "autor": autor, "status": "Disponível" "Alugado" "Reservado" "Alugado e Reservado"}
    listaLivros.append(livroCadastrado)
    print("Livro cadastrado com sucesso")
    
#funcionalidade 2 - cadastrar pessoas
#[Requisitos futuro] apenas o ADM poderá cadastrar pessoas
#[Requisitos futuro] banco de dados para armazenar pessoas
#[Requisito futuro] permissões de acesso para usuários dependendo do tipo 
def cadastrarpessoas(nome, usuario):
    usuarioCadastrado = {"nome": nome, "usuario": usuario}
    listaUsuarios.append(usuarioCadastrado)
    print("Usuário cadastrado com sucesso")

#funcionalidade 3 - cadastrar eventos
#[Requisito futuro] apenas ADM poderá cadastrar eventos 
def cadastarEvento(nomeEvento, dataEvento, localEvento):
    eventoCadastrado = {"nome": nomeEvento, "data": dataEvento, "local": localEvento, "status": "Em desenvolvimento" "Em andamento" "Finalizado" "Cancelado"}
    listaEventos.append(eventoCadastrado)
    print("Evento cadastrado com sucesso")

# funcionalidade 4 - pesquisar livros
def pesquisarLivro(nomeLivro):
    for livro in listaLivros:
        if livro["nome"] == nomeLivro:
            print(livro) 
            return livro
        print("Livro não encontrado")
        return None
    
if opcao == "1":
    print("Digite o nome do livro")
    nome = input()
    print("Digite o autor do livro")
    autor = input()
    cadastrarLivros(nome, autor)

elif opcao == "2":
    print("Digito o Nome do Livro que deseja pesquisar")
    nomeLivro = input()
    pesquisarLivro(nomeLivro)

#Funcionalidade 5 - Alugar livro
elif opcao == "3":
    print("Digite o nome do livro que deseja alugar")
    nomeLivro = input()
    livro = pesquisarLivro(nomeLivro)
    if livro: 
        if livro["status"] == "Alugado" or livro["status"] == "Reservado" or livro["status"] == "Alugado e Reservado":
            print("Livro indisponível") 
        else:
            print("Digite seu usuário:")
            usuario = input()
            print("Digite a data de locação")
            dataLocacao = input()
            livro["status"] == "Alugado"
            print("Livro alugado com sucesso!")
            print("Você tem 15 dias para devolver o livro")
    else: 
        print("Livro não encontrado")  

#Funcionalidade 6 - Devolver livro
#Funcionalidade 7 - cobraça de multa 
#[Requisitos futuro] ao ser alugado, o livro passará a ter um status de alugado, e não poderá ser alugado novamente
#[Requisitos futuro] ao pesquisar um livro, o sistema deverá informar se o livro está disponível para aluguel
elif opcao == "4":
    print("Digite o nome do livro que deseja devolver")
    nomeLivro = input()
    livro = pesquisarLivro(nomeLivro)
    if livro != "Livro não encontrado":
        print("Digite a data de devolução")
        dataDevolucao = input()
        dataDevolucao = datatime.strptime(dataDevolucao, "%d/%m/%Y")
        
        if dataDevolucao > dataLocacao:
            print("Você está atrasado, pague a multa")        
            print("Digite seu usuário:")
            usuario = input()
            print("Livro devolvido com sucesso")
        else:
            print("Digite seu usuário:")
            print("Livro devolvido com sucesso")

elif opcao == "5":
    print("Digite o nome do usuário")
    nome = input()
    print("Digite o tipo de usuário")
    usuario = input()
    cadastrarpessoas(nome, usuario)

elif opcao == "6":
    print("Digite o nome do evento")
    nomeEvento = input()
    print("digite a data do evento")
    dataEvento = input()
    print("Digite o local do evento")
    localEvento = input()
    
    cadastarEvento(nomeEvento, dataEvento, localEvento)

#Funcionalidade 8 - Reservar livro
elif opcao == "7":
    print("Digite o nome do livro que deseja reservar")
    nomeLivro = input()
    livro = pesquisarLivro(nomeLivro)
    if livro != "Livro não encontrado":
        print("Digite seu usuário:")
        usuario = input()
        print("Livro reservado com sucesso")
    
else:
    print("Opção inválida") 
