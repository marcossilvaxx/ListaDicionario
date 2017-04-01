funcionarios = []

def adicionarFuncionario(matricula, nome):
    funcionario = {matricula:nome}
    funcionarios.append(funcionario)
    print("Funcionário adicionado.")
    main()

def buscarFuncionario(matricula):
    has_funcionario = 0
    for funcionario in funcionarios:
        if matricula in funcionario:
            print("Funcionário encontrado.")
            print(list(funcionario.keys())[0],"-", list(funcionario.values())[0])
            has_funcionario += 1
    if has_funcionario == 0:
        print("Funcionário não encontrado.")
    main()

def exibirFuncionarios():
    for funcionario in funcionarios:
        print(list(funcionario.keys())[0],"-", list(funcionario.values())[0])
    main()
                    
def main():
    pergunta = eval(input("Digite 1 para cadastrar um funcionário; Digite 2 para buscar um funcionário; Digite 3 para exibir todos os funcionários.\n"))
    if pergunta == 1:
        matricula = eval(input("Informe a matrícula do funcionário:\n"))
        nome = str(input("Informe o nome do funcionário:\n"))
        adicionarFuncionario(matricula, nome)
    elif pergunta == 2:
        matricula = eval(input("Informe a matricula do funcionário que você quer buscar:\n"))
        buscarFuncionario(matricula)
    elif pergunta == 3:
        exibirFuncionarios()

if __name__ == "__main__":
    main()
