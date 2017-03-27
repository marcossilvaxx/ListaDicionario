semana = []

def adicionarDia(posicao, dia):
    diaDaSemana = {}
    diaDaSemana[posicao] = dia
    semana.append(diaDaSemana)
    print("Dia adicionado.")
    main()

def exibirDias(semana):
    for dia in semana:
        for posicao, nomeDia in dia.items():
            print(posicao, "-", nomeDia)
    main()

def main():
    pergunta = int(input("Para adicionar um dia, digite 1. Para exibir os dias, digite 2.\n"))

    if pergunta == 1:
        posicao = int(input("Informe a posição do dia:\n"))
        dia = str(input("Informe o dia:\n"))
        adicionarDia(posicao, dia)

    elif pergunta == 2:
        exibirDias(semana)


if __name__ == "__main__":
    main()
