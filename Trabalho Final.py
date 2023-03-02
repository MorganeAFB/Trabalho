# Variaveis

Lista = []

# Classe


class Compromisso:
    Descricao = None
    Data = None
    Hora = None
    Duracao = None

# Funções


def IncluirCompromissos():

    print('\n==== Incluir Compromissos ====')
    while True:

        C = Compromisso()
        C.Descricao = input("\nDescrição: ")
        C.Data = input("Data: ")
        C.Hora = input("Hora: ")
        C.Duracao = float(input("Duração (em horas): "))
        Lista.append(C)

        Continuar1 = int(
            input('\nDeseja incluir mais compromissos? 0 - Não, ou qualquer número para sim: '))

        if Continuar1 == 0:
            break


def ConsultaCompromissos():
    NumConsultasA1 = []
    DataA2 = HoraA2 = 0

    print('\n==== Consulta de Compromissos ====')

    while True:

        Consulta1 = int(input(
            '\nComo deseja consultar? 1 para por datas, 2 para datas e horas e 0 para sair: '))

        if Consulta1 == 0:
            break

        if Consulta1 == 1:
            NumConsultasA1 = []

            DataA1 = input('\nDigite a data como foi escrita: ')

            for i in range(len(Lista)):

                # Salvar os números dos vetores onde estão presentes as informações

                if ((DataA1 in Lista[i].Data) == True):
                    NumConsultasA1.append(i)

            if len(NumConsultasA1) == 0:
                print('\nAgenda Vazia!')

            else:
                for i in range(len(NumConsultasA1)):

                    n1 = NumConsultasA1[i]

                    print(f'''
ID: {n1+1}
Descrição: {Lista[n1].Descricao}
Data: {Lista[n1].Data}
Hora: {Lista[n1].Hora}
Duração: {Lista[n1].Duracao}     
                            ''')

        elif Consulta1 == 2:
            NumConsultasA1 = []

            DataA1 = input('\nDigite a data como foi escrita: ')
            HoraA1 = input('Digite a hora como foi escrita: ')

            for i in range(len(Lista)):

                # Salvar os números dos vetores onde estão presentes as informações

                if ((DataA1 in Lista[i].Data) == True) and ((HoraA1 in Lista[i].Hora) == True):
                    NumConsultasA1.append(i)

            if len(NumConsultasA1) == 0:
                print('\nAgenda Vazia!')

            else:
                for i in range(len(NumConsultasA1)):

                    n1 = NumConsultasA1[i]

                    print(f'''
ID: {n1+1}
Descrição: {Lista[n1].Descricao}
Data: {Lista[n1].Data}
Hora: {Lista[n1].Hora}
Duração: {Lista[n1].Duracao}     
                        ''')
        else:
            print('\nErro! Tente novamente.')


def AlterarCompromissos():

    NumConsultasA1 = []

    print('\n==== Alterar Compromissos ====')

    while True:
        Sair3 = int(
            input('\nDigite 0 caso queira sair ou qualquer número para continuar: '))

        if Sair3 == 0:
            break

        print('\nPreencha as informações abaixo para achar o compromisso desejado')

        DataA1 = input('\nDigite a data como foi escrita: ')
        HoraA1 = input('Digite a hora como foi escrita: ')

        for i in range(len(Lista)):

            # Salvar os números dos vetores onde estão presentes as informações

            if ((DataA1 in Lista[i].Data) == True) and ((HoraA1 in Lista[i].Hora) == True):
                NumConsultasA1.append(i)

        if len(NumConsultasA1) == 0:
            print('\nCompromisso não encontrado.')

        else:
            for i in range(len(NumConsultasA1)):

                n1 = NumConsultasA1[i]

                print(f'''
ID: {NumConsultasA1[i]+1}°
Descrição: {Lista[n1].Descricao}
Data: {Lista[n1].Data}
Hora: {Lista[n1].Hora}
Duração: {Lista[n1].Duracao}     
                        ''')

            Consulta2 = int(input(
                'Qual compromisso deseja alterar (coloque o ID dele)? '))

            Lista[Consulta2-1].Descricao = input('\nDescrição: ')
            Lista[Consulta2-1].Duracao = float(input('Duração: '))


def ExcluirCompromissos():

    print('\n==== Excluir Compromissos ====')

    for i in range(len(Lista)):

        print(f'''
ID: {i+1}°
Descrição: {Lista[i].Descricao}
Data: {Lista[i].Data}
Hora: {Lista[i].Hora}
Duração: {Lista[i].Duracao}     
        ''')

    while True:

        Consulta2 = int(input(
            '\nQual compromisso deseja remover? Digite 0 para sair, 1 para continuar e 2 para ver a lista novamente: '))

        if Consulta2 == 0:
            break
        elif Consulta2 == 1:

            Consulta3 = int(
                input('Qual compromisso deseja remover (digite o ID dele)?: '))

            Lista[Consulta3-1].remove

        if Consulta2 == 2:
            for i in range(len(Lista)):

                print(f'''
ID: {i+1}°
Descrição: {Lista[i].Descricao}
Data: {Lista[i].Data}
Hora: {Lista[i].Hora}
Duração: {Lista[i].Duracao}     
                    ''')

        else:
            print('\nErro! Tente novamente.')


def ListarCompromissos():

    print('\n==== Listar Compromissos ====')

    for i in range(len(Lista)):

        print(f'''
ID: {i+1}°
Descrição: {Lista[i].Descricao}
Data: {Lista[i].Data}
Hora: {Lista[i].Hora}
Duração: {Lista[i].Duracao}     
            ''')


# Parte Usuário

print('Bem vindo a Agenda de Compromissos!')

while True:

    print('''
Ferramentas

1 - Incluir
2 - Consultar
3 - Alterar
4 - Excluir
5 - Listar todos
6 - Sair
''')

    acao = int(input('Digite a ação a ser tomada: '))

    if acao == 1:
        IncluirCompromissos()

    elif acao == 2:
        ConsultaCompromissos()

    elif acao == 3:
        AlterarCompromissos()

    elif acao == 4:
        ExcluirCompromissos()

    elif acao == 5:
        ListarCompromissos()

    elif acao == 6:
        break

    else:
        print('Erro. Tente novamente!')
