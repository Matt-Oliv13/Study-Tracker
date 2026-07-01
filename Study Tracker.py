
def menu():
    titulo = "MENU"
    largura = 35
    opcoes = [
        "1 - Adicionar Matéria/Tópico",
        "2 - Deletar Matéria/Tópico",
        "3 - Mostrar Lista de Estudos",
        "4 - Concluir Tópico",
        "5 - Mostrar Progresso",
        "6 - Salvar ou Carregar",
        "7 - Encerrar"
    ]
    print(" ")
    print("|" + "-" * largura + "|")
    print("|" + titulo.center(largura) + "|")
    print("|" + "-" * largura + "|")
    for opcao in opcoes:
        print(f"|   {opcao:<{largura-3}}|") 
        # :< alinhamento à esquerda
        # largura-3 é usado para informar quantos caracteres vazios serão usados para o alinhamento da string, sendo usado após ':<'.
    print("|" + "-" * largura + "|")
    print(" ")


def ver_lista():
    for materia in study_tracker:
        print(f"\n{materia}")
        for topico in study_tracker[materia]:
            print(f" - {topico}")



# PROGRAMA:

study_tracker = {}

print("Bem vindo ao seu Study Tracker!")
while True:
    menu()
    try:
        selecao = int(input("Digite o número da opção desejada: "))


        if selecao == 1: # Adicionar Matéria ou Tópico
            if study_tracker:
                ver_lista()
            print("")    
            print("1 - Adicionar Matéria")
            print("2 - Adicionar Tópico")
            print("3 - Retornar ao menu")

            selecao_adicionar = input("Digite o número da opção desejada: ")
            if selecao_adicionar == "1":
                materia = input("Digite o nome da materia que deseja adicionar: ")
                if materia in study_tracker:
                    print("Matéria já cadastrada.")
                    print("Retornando ao menu...")
                else:
                    print(f"A matéria {materia} foi adicionada à sua lista")
                    study_tracker[materia] = {} # Importante, a chave 'materia' deve ser relacionada à um dicionário {} pois usaremos os tópicos associados à um valor de true or false para marcar o progresso.
                    print("Retornando ao menu...")
            elif selecao_adicionar == "2":
                materia = input("Digite o nome da matéria que receberá o tópico: ")
                if materia in study_tracker:
                    topico = input("Digite o novo tópico: ")
                    if topico in study_tracker[materia]:
                        print("Tópico já existe. Retornando ao menu")
                    else:
                        study_tracker[materia][topico] = False 
                        # Aqui basicamente estou dizendo 'dicionário[chave]:([chave]:valor) ou seja, o valor da primeira chave é um outro dicionário, com chave e valor. Isso irá permitir registrar o progresso 'True or False'
                        print(f"O topico {topico} foi adicionado à {materia}")
                else:
                    print("Matéria não encontrada.")
            if selecao_adicionar == "3":
                print("Retornando ao menu...")


        elif selecao == 2: # Deletar Matéria / Tópico
            if study_tracker:
                ver_lista()
                print("")  
                print("1 - Deletar Matéria")
                print("2 - Deletar Tópico")
                print("3 - Retornar ao menu")
                selecao_deletar = input("Digite o número da opção desejada: ")
                if selecao_deletar not in ["1", "2", "3"]:
                    print("Opção inválida. Retornando ao menu...")
                    continue
                elif selecao_deletar == "1":
                    print("ATENÇÃO: Ao deletar uma matéria, todos os tópicos associados a ela serão deletados também.")
                    materia = input("Digite o nome da matéria que deseja deletar: ")
                    if materia in study_tracker:
                        del study_tracker[materia]
                        print(f"A matéria {materia} foi deletada com sucesso.")
                    else:
                        print(f"Matéria {materia} não encontrada.")
                    continue
                elif selecao_deletar == "2":
                    materia = input("Digite o nome da matéria que contém o tópico que deseja deletar: ")
                    if materia in study_tracker:
                        if not study_tracker[materia]:
                            print("A matéria não possui tópicos cadastrados.")
                            continue
                        topico = input("Digite o tópico que quer deletar: ")
                        if topico in study_tracker[materia]:
                            del study_tracker[materia][topico]
                            print(f"O topico {topico} foi deletado com sucesso.")
                        else:
                            print(f"Tópico {topico} não encontrado.")
                    else:
                        print(f"Matéria {materia} não encontrada.")
                    continue
                elif selecao_deletar == "3":
                    print("Retornando ao menu...")
            else: 
                print("Você ainda não registrou uma matéria")
                print("Retornando ao menu...")


        elif selecao == 3: # Mostrar Dicionário
            if study_tracker:
                ver_lista()
            else: 
                print("Você ainda não registrou uma matéria")
                print("Retornando ao menu...")


        elif selecao == 4: # Concluir Tópicos
            if study_tracker:
                ver_lista()
                print("")  
                materia = input("Digite o nome da matéria para concluir um tópico: ")
                if materia in study_tracker:
                    topico = input("Digite o tópico que quer concluir: ")
                    if topico in study_tracker[materia]:
                        if study_tracker[materia][topico] == True:
                            print("Este tópico já foi concluído.")
                        elif study_tracker[materia][topico] == False:
                            concluir = input("O tópico foi mesmo concluído? (S/N) ")
                            if concluir.lower() in ["s", "sim"]:
                                study_tracker[materia][topico] = True
                                print(f"{topico} concluído! Parabéns!")
                            if concluir.lower() in ["n", "nao", "não"]:
                                study_tracker[materia][topico] = False
                                print("Retornando ao menu...")
            else: 
                print("Você ainda não registrou uma matéria")
                print("Retornando ao menu...")


        elif selecao == 5: # Mostrar Progresso
            if study_tracker:
                for materia in study_tracker:
                    total_topicos = len(study_tracker[materia])
                    topicos_concluidos = 0
                    print(f"\n{materia}")
                    for topico, concluido in study_tracker[materia].items(): #.items() retorna chave e valor juntos.
                        if concluido: # Ou seja se o valor for True, concluído é verdadeiro, então o tópico foi concluído.
                            topicos_concluidos += 1
                            simbolo = "✓"
                        else:
                            simbolo = " "
                        print(f"[{simbolo}] {topico}")
                    if total_topicos > 0:
                        porcentagem = (topicos_concluidos/total_topicos)*100
                        print(f'Taxa de conclusão: {porcentagem:.0f}%')
                    else:
                        print("Nenhum tópico registrado para esta matéria.")

            #Dicionario = {materia:{topico:false},...}
            #cada matéria deve mostrar o progresso, ou seja, eu preciso saber quantos topicos existem ali, e depois fazer um calculo em cima deles.


        elif selecao == 6: # Salvar / Carregar
            print("1 - Salvar")
            print("2 - Carregar")
            print("3 - Retornar ao menu")
            selecao_salvar_carregar = input("Digite o número da opção desejada: ")
            if selecao_salvar_carregar not in ["1", "2", "3"]:
                print("Opção inválida. Retornando ao menu...")
                continue
            elif selecao_salvar_carregar == "1":
                with open("study_tracker.txt", "w") as arquivo:
                    for materia, topicos in study_tracker.items():
                        arquivo.write(f"{materia}\n")
                        for topico, concluido in topicos.items():
                            if concluido:
                                arquivo.write(f"{topico}:Finalizado\n")
                            else:
                                arquivo.write(f"{topico}:Incompleto\n")
                print("Dados salvos com sucesso.")
            elif selecao_salvar_carregar == "2":
                try:
                    with open("study_tracker.txt", "r") as arquivo:
                        study_tracker.clear()
                        materia_atual = None
                        for linha in arquivo:
                            linha = linha.strip()
                            if ":" not in linha:
                                materia_atual = linha
                                study_tracker[materia_atual] = {}
                            else:
                                topico, concluido = linha.split(":")
                                study_tracker[materia_atual][topico] = concluido == "Finalizado"
                    print("Dados carregados com sucesso.")
                except FileNotFoundError:
                    print("Arquivo não encontrado. Nenhum dado foi carregado.")
            elif selecao_salvar_carregar == "3":
                print("Retornando ao menu...")

            
        elif selecao == 7: # Encerrar
            encerrar = input("Tem certeza que deseja encerrar? (S/N) ")
            if encerrar.lower() in ["s", "sim"]:
                print("Programa Encerrado.")
                break
            if encerrar.lower() in ["n", "nao", "não"]:
                print("Retornando ao menu...")

        else:
            print("número inválido, tente novamente")

    except ValueError:
        print("Por favor, digite um número válido.")


