turmas = []

def adicionarTurma():
    nTurma = str(input("Informe a turma:\n"))
    alunos = []
    turma = {nTurma: alunos}
    turmas.append(turma)
    print("Turma criada.")
    voltarMenu()

def adicionarAlunoNotas():
    matricula = int(input("Informe a matrícula do aluno:\n"))
    notas = input("Informe as notas do aluno:\n")
    turma = input("Informe a turma que você quer adicionar esse aluno:\n")
    notas = notas.split(", ")
    notas = list(map(float, notas))
    aluno = {matricula: notas}
    has_turma = 0
    for i in turmas:
        if turma in i:
            i[turma].append(aluno)
            print("Aluno adicionado à turma.")
            has_turma += 1
    if has_turma == 0:
        print("Turma não encontrada.")
    voltarMenu()

def calcularMediaAluno():
    matricula = int(input("Informe a matrícula do aluno que você quer calcular a média:\n"))
    has_aluno = 0
    for turma in turmas:
        for alunos in turma.values():
            for aluno in alunos:
                if matricula in aluno:
                    media = sum(aluno[matricula]) / len(aluno[matricula])
                    print("A média aritmética deste aluno é:", media)
                    has_aluno += 1
    if has_aluno == 0:
        print("Aluno não encontrado.")
    voltarMenu()

def calcularMediaTurma():
    turmaM = str(input("Informe a turma que você quer calcular a média:\n"))
    mediasTurma = []
    for turma in turmas:
        if turmaM in turma:
            for alunos in turma.values():
                for aluno in alunos:
                    notas = aluno.values()
                    for notasAluno in notas:
                        media = sum(notasAluno) / len(notasAluno)
                        mediasTurma.append(media)
            mediaTurma = sum(mediasTurma) / len(mediasTurma)
            print("A média aritmética da turma é:", mediaTurma)
    voltarMenu()

def menu():
    print("MENU\n")
    print("Opções: I - Adicionar Turma, II - Adicionar Aluno e Notas, III - Calcular média de um Aluno, IV - Calcular média de uma Turma")
    print("Para sair, digite: sair\n")
    opção = str(input("Qual opção você deseja?\n"))
    if opção.lower() == "i":
        adicionarTurma()
    elif opção.lower() == "ii":
        adicionarAlunoNotas()
    elif opção.lower() == "iii":
        calcularMediaAluno()
    elif opção.lower() == "iv":
        calcularMediaTurma()
    elif opção.lower() == "sair":
        print("Programa encerrado.")

def voltarMenu():
    pergunta = str(input("Deseja voltar para o Menu?\n"))
    if pergunta.lower() == "sim":
        menu()
    elif pergunta.lower() == "não":
        print("Programa encerrado.")

if __name__ == "__main__":
    menu()