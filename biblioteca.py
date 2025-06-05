documentos_db = []

def adicionar_documento(): # FUNÇÃO MODIFICADA
    """Adiciona um novo documento ao sistema."""
    print("\n--- Adicionar Novo Documento ---")
    nome = input("Digite o nome do arquivo (ex: artigo_ia.pdf): ")
    tipo = input("Digite o tipo do arquivo (ex: PDF, ePUB, DOCX): ").upper() # Padroniza para maiúsculas
    ano_str = input("Digite o ano de publicação: ")

    # Validação do ano
    if not ano_str.isdigit() or len(ano_str) != 4:
        print("Erro: Ano inválido. Por favor, insira um ano com 4 dígitos.")
        return
    ano = int(ano_str)

    # Verifica se o documento já existe (pelo nome)
    for doc_item in documentos_db:
        if doc_item['nome'] == nome:
            print(f"Erro: Documento '{nome}' já existe.")
            return

    documento = {"nome": nome, "tipo": tipo, "ano": ano}
    documentos_db.append(documento)
    print(f"Documento '{nome}' adicionado com sucesso!")

def listar_documentos():
    """Lista todos os documentos, com opção de organização."""
    if not documentos_db:
        print("\nNenhum documento cadastrado no sistema.")
        return

    print("\n--- Listar Documentos ---")
    print("Como você gostaria de organizar a lista?")
    print("1. Por Tipo de Arquivo")
    print("2. Por Ano de Publicação")
    print("3. Padrão (ordem de adição)")
    escolha_organizacao = input("Escolha uma opção (1, 2 ou 3): ")

    documentos_para_listar = list(documentos_db)

    if escolha_organizacao == '1':
        documentos_para_listar.sort(key=lambda doc: (doc['tipo'], doc['nome'].lower()))
        print("\n--- Documentos Organizados por Tipo ---")
    elif escolha_organizacao == '2':
        documentos_para_listar.sort(key=lambda doc: (doc['ano'], doc['nome'].lower()))
        print("\n--- Documentos Organizados por Ano de Publicação ---")
    elif escolha_organizacao == '3':
        print("\n--- Todos os Documentos (Ordem de Adição) ---")
    else:
        print("Opção de organização inválida. Listando na ordem padrão.")
        print("\n--- Todos os Documentos (Ordem de Adição) ---")

    for i, doc_item in enumerate(documentos_para_listar):
        print(f"{i+1}. Nome: {doc_item['nome']}, Tipo: {doc_item['tipo']}, Ano: {doc_item['ano']}")

def renomear_documento(): # FUNÇÃO MODIFICADA
    """Renomeia um documento existente no sistema."""
    print("\n--- Renomear Documento ---")
    nome_antigo = input("Digite o nome do arquivo atual que deseja renomear: ")

    documento_encontrado = None
    indice_documento_original = -1
    for i, doc_item in enumerate(documentos_db):
        if doc_item['nome'] == nome_antigo:
            documento_encontrado = doc_item
            indice_documento_original = i
            break

    if documento_encontrado:
        novo_nome = input(f"Digite o novo nome para '{nome_antigo}': ")
        # Verifica se o novo nome já está em uso por OUTRO documento
        for i_check, doc_check in enumerate(documentos_db):
            if doc_check['nome'] == novo_nome and i_check != indice_documento_original:
                print(f"Erro: O nome '{novo_nome}' já está em uso por outro documento.")
                return
        documento_encontrado['nome'] = novo_nome
        print(f"Documento '{nome_antigo}' renomeado para '{novo_nome}' com sucesso!")
    else:
        print(f"Erro: Documento '{nome_antigo}' não encontrado.")

def remover_documento():
    """Remove um documento do sistema."""
    print("\n--- Remover Documento ---")
    nome_remover = input("Digite o nome do arquivo que deseja remover: ")
    documento_encontrado = None
    for doc_item in documentos_db:
        if doc_item['nome'] == nome_remover:
            documento_encontrado = doc_item
            break
    if documento_encontrado:
        documentos_db.remove(documento_encontrado)
        print(f"Documento '{nome_remover}' removido com sucesso!")
    else:
        print(f"Erro: Documento '{nome_remover}' não encontrado.")

def menu_principal():
    """Exibe o menu principal e gerencia a interação com o usuário."""
    # Reorganizando a ordem do menu para a versão final
    while True:
        print("\n====== Sistema de Gestão de Documentos da Biblioteca ======")
        print("1. Adicionar Documento")
        print("2. Renomear Documento") # Movido
        print("3. Remover Documento")  # Movido
        print("4. Listar Documentos")  # Movido
        print("5. Sair")
        print("==========================================================")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_documento()
        elif escolha == '2':
            renomear_documento()
        elif escolha == '3':
            remover_documento()
        elif escolha == '4':
            listar_documentos()
        elif escolha == '5':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    menu_principal()

