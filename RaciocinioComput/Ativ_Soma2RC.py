import json

def incluir_registros(nome_arquivo, titulo, campos_adicionais):
    titulo_desejado = titulo.split('MENU DE OPERAÇÕES')[0].strip()
    while True:
        if titulo_desejado == '[ESTUDANTE]' or titulo_desejado == '[PROFESSOR]':
                codigo_pessoas = int(input(f'Digite o código do/a {titulo_desejado}: '))
                if validar_codigo_existente('estudantes.json', codigo_pessoas) or validar_codigo_existente('professores.json', codigo_pessoas):
                    print(f"Aviso:{titulo_desejado} já adicionado. ")
                    break
                nome_pessoas = input(f'Digite o nome do/a {titulo_desejado}: ')
                cpf_pessoas = input(f'Digite o cpf do/a {titulo_desejado}: ')
                dados_pessoas = {
                'Código': codigo_pessoas,
                'Nome': nome_pessoas,
                'CPF': cpf_pessoas,
                }

                lista_pessoas = ler_arquivo(nome_arquivo)
                lista_pessoas.append(dados_pessoas)
                salvar_arquivo(lista_pessoas, nome_arquivo)
                print(f"\n{titulo_desejado} '{dados_pessoas['Nome']}' adicionado com sucesso!")
                return

        elif titulo_desejado == '[DISCIPLINA]':
            while True:
                codigo_disciplina = int(input(f'Digite o código da {titulo_desejado}: '))
                if validar_codigo_existente('disciplinas.json', codigo_disciplina):
                    print(f'Aviso: Disciplina {codigo_disciplina} já adicionada.')
                    break
                nome_disciplina = input(f'Digite o nome da {titulo_desejado}: ')
                dados_disciplina = {
                    'Código': codigo_disciplina,
                    'Nome': nome_disciplina,
                }
                lista_registros = ler_arquivo(nome_arquivo)
                lista_registros.append(dados_disciplina)
                salvar_arquivo(lista_registros, nome_arquivo)
                print(f"\n{titulo_desejado} '{dados_disciplina['Nome']}' adicionado com sucesso!")
                return

        elif titulo_desejado == '[TURMA]':
            while True:
                codigo_turma = int(input(f'Digite o código da {titulo_desejado}: '))
                if validar_codigo_existente('turmas.json', codigo_turma):
                    print(f'Aviso: Código da turma {codigo_turma} já adicionado.')
                    break
                codigo_professor = int(input(f'Digite o código do/a professor/a para a {titulo_desejado}: '))
                if not validar_codigo_existente('professores.json', codigo_professor):
                    print(f'Aviso: Código do/a professor/a {codigo_professor} não encontrado.')
                    return
                codigo_disciplina = int(input(f'Digite o código da disciplina para a {titulo_desejado}: '))
                if not validar_codigo_existente('disciplinas.json', codigo_disciplina):
                    print(f'Aviso: Código da disciplina {codigo_disciplina} não encontrada.')
                    return
                dados_turma = {
                    'Código': codigo_turma,
                    'Professor': codigo_professor,
                    'Disciplina': codigo_disciplina,
                }
                lista_registros = ler_arquivo(nome_arquivo)
                lista_registros.append(dados_turma)
                salvar_arquivo(lista_registros, nome_arquivo)
                print(f"\n{titulo_desejado} com código {codigo_turma} adicionada com sucesso!")
                return
        elif titulo_desejado == '[MATRÍCULA]':
            while True:
                codigo_turma = int(input(f'Digite o código da turma para a {titulo_desejado}: '))
                if not validar_codigo_existente('turmas.json', codigo_turma):
                    print(f'Aviso: Código da turma {codigo_turma} não adicionado')
                    break
                codigo_estudante = int(input(f'Digite o código do/a estudante para a {titulo_desejado}: '))
                if not validar_codigo_existente("estudantes.json", codigo_estudante):
                    print(f'Aviso: Código do/a estudante {codigo_estudante} não encontrado.')
                    break
                dados_matricula = {
                    'Código': codigo_turma,
                    'Estudante': codigo_estudante,
                }
                lista_registros = ler_arquivo(nome_arquivo)
                lista_registros.append(dados_matricula)
                salvar_arquivo(lista_registros, nome_arquivo)
                print(f"\nMatrícula do/a estudante {codigo_estudante} na turma {codigo_turma} realizada com sucesso!")
                return

def mostrar_registros(nome_arquivo, titulo):
    titulo_desejado = titulo.split('MENU DE OPERAÇÕES')[0].strip()
    lista_registros = ler_arquivo(nome_arquivo)
    if len (lista_registros) == 0:
        print(f'\nNão há {titulo_desejado.lower()} cadastrado/a no sistema.')
    else:
        print(f"\nLista de {titulo_desejado}:")
        for registro in lista_registros:
            info = ' // '.join([f"{chave}: {valor}" for chave, valor in registro.items()])
            print(f"- {info}")

def editar_registros(nome_arquivo, titulo, campos_adicionais):
    titulo_desejado = titulo.split('MENU DE OPERAÇÕES')[0].strip()
    codigo_editar = int(input(f'Digite o código do/a {titulo_desejado.lower()} a ser editado: '))
    lista_registros = ler_arquivo(nome_arquivo)
    encontrado = False
    for registro in lista_registros:
        if 'Código' in registro and registro['Código'] == codigo_editar:
            if titulo_desejado == '[ESTUDANTE]' or titulo_desejado == '[PROFESSOR]':
                registro['Nome'] = input(f'Digite o novo nome do/a {titulo_desejado.lower()}: ')
                registro['CPF'] = input(f'Digite o novo CPF do/a {titulo_desejado.lower()}: ')
                if campos_adicionais:
                    for campo, tipo in campos_adicionais.items():
                        if campo not in ['Código','Nome','CPF']:
                            if tipo == int:
                                registro[campo] = int(input(f'Digite o novo {campo} do/a {titulo_desejado.lower()}: '))
                            else:
                                registro[campo] = input(f'Digite o novo {campo} do/a {titulo_desejado.lower()}: ')
                salvar_arquivo(lista_registros, nome_arquivo)
                print(f'\n{titulo_desejado} atualizado com sucesso!.')
                encontrado = True
                break
            elif titulo_desejado == '[DISCIPLINA]':
                registro['Nome'] = input(f'Digite o novo nome do/a {titulo_desejado.lower()}: ')
                if campos_adicionais:
                    for campo, tipo in campos_adicionais.items():
                        if campo not in ['Código','Nome']:
                            if tipo == int:
                                registro[campo] = int(input(f'Digite o novo {campo} do/a {titulo_desejado.lower()}: '))
                            else:
                                registro[campo] = input(f'Digite o novo {campo} do/a {titulo_desejado.lower()}: ')
                salvar_arquivo(lista_registros, nome_arquivo)
                print(f'\n{titulo_desejado} atualizado com sucesso!.')
                encontrado = True
                break
            elif titulo_desejado == '[TURMA]' or titulo_desejado == '[MATRÍCULA]':
                registro['Código'] = int(input(f'Digite o novo código da {titulo_desejado.lower()}: '))
                if campos_adicionais:
                    for campo, tipo in campos_adicionais.items():
                        if campo not in ['Código']:
                            if tipo == int:
                                salvar_arquivo(lista_registros, nome_arquivo)
                                print(f'\n{titulo_desejado} atualizado com sucesso!.')
                                encontrado = True
                                break
    if not encontrado:
        print(f'\n{titulo_desejado} com código {codigo_editar} não encontrado.')

def remover_registros(nome_arquivo, titulo):
    titulo_desejado = titulo.split('MENU DE OPERAÇÕES')[0].strip()
    codigo_remover = int(input(f'Digite o código do/a {titulo_desejado.lower()} a ser excluído: '))
    lista_registros = ler_arquivo(nome_arquivo)
    indice_encontrado = -1
    for i, registro in enumerate(lista_registros):
        if 'Código' in registro and registro['Código'] == codigo_remover:
            indice_encontrado = i
            break
    if indice_encontrado != -1:
        del lista_registros[indice_encontrado]
        salvar_arquivo(lista_registros, nome_arquivo)
        print(f'\n{titulo_desejado} com código {codigo_remover} excluído com sucesso!.')
    else:
        print(f'\n{titulo_desejado} com código {codigo_remover} não encontrado.')


def salvar_arquivo(lista_registros, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_aberto:
        json.dump(lista_registros, arquivo_aberto, ensure_ascii=False, indent=4)

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_aberto:
            lista_registros = json.load(arquivo_aberto)
        return lista_registros
    except:
        return []

def validar_codigo_existente(nome_arquivo, codigo):
    lista_registros = ler_arquivo(nome_arquivo)
    for registro in lista_registros:
        if 'Código' in registro and registro['Código'] == codigo:
            return True
    return False

def menu_sec(titulo, nome_arquivo, campos_adicionais=None ,funcao_incluir_especial=None):
    while True:
        print('\n', titulo.center(40, "*"))
        print('\n(1) Incluir.\n(2) Listar.\n(3) Editar.\n(4) Excluir.')
        print('(9) Voltar ao menu principal.\n')

        opcao_sec = input('Informe a ação desejada: ')
        titulo_desejado = titulo.split('MENU DE OPERAÇÕES')[0].strip()

        if opcao_sec == '1':
            if funcao_incluir_especial:
                funcao_incluir_especial(nome_arquivo, titulo, campos_adicionais)
            else:
                incluir_registros(nome_arquivo, titulo, campos_adicionais)
        elif opcao_sec == '2':
            mostrar_registros(nome_arquivo, titulo)
        elif opcao_sec == '3':
            lista_registros = ler_arquivo(nome_arquivo)
            if not lista_registros:
                print(f'\nNão há {titulo_desejado.lower()} cadastrado/a no sistema. ')
            else:
                editar_registros(nome_arquivo, titulo, campos_adicionais)
        elif opcao_sec == '4':
            lista_registros = ler_arquivo(nome_arquivo)
            if not lista_registros:
                print(f'\nNão há {titulo_desejado.lower()} cadastrado/a no sistema. ')
            else:
                remover_registros(nome_arquivo, titulo)
        elif opcao_sec == '9':
            return
        else:
            print('\nOpção inválida. Tente novamente!')

def menu_principal():
    arquivo_estudante = "estudantes.json"
    arquivo_professor = "professores.json"
    arquivo_disciplina = "disciplinas.json"
    arquivo_turma = "turmas.json"
    arquivo_matricula = "matriculas.json"

    while True:
        name = ' MENU PRINCIPAL '
        print('\n',name.center(25, "*"))
        print('\n(1) Gerenciar estudantes.\n(2) Gerenciar professores.\n(3) Gerenciar disciplinas.\n(4) Gerenciar turmas.\n(5) Gerenciar matrículas.')
        print('(9) Sair.\n')

        opcao = input('Informe a opção desejada: ')
        if opcao == '1':
            titulo = '[ESTUDANTE] MENU DE OPERAÇÕES '
            menu_sec(titulo, arquivo_estudante, {'Código': int})
        elif opcao == '2':
            titulo = '[PROFESSOR] MENU DE OPERAÇÕES '
            menu_sec(titulo, arquivo_professor, {'Código': int})
        elif opcao == '3':
            titulo = '[DISCIPLINA] MENU DE OPERAÇÕES '
            menu_sec(titulo, arquivo_disciplina, {'Código': int})
        elif opcao == '4':
            titulo = '[TURMA] MENU DE OPERAÇÕES '
            menu_sec(titulo, arquivo_turma, {'Código': int, 'Código do professor': int, 'Código da disciplina': int})
        elif opcao == '5':
            titulo = '[MATRÍCULA] MENU DE OPERAÇÕES '
            menu_sec(titulo, arquivo_matricula, None)
        elif opcao == '9':
            print('\nFinalizando aplicação...')
            return
        else:
            print('\nOpção inválida. Tente novamente!\n')

if __name__ == '__main__':
    menu_principal()