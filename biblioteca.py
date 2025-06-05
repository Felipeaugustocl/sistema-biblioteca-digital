documentos_db = []

def adicionar_documento():
    """Adiciona um novo documento ao sistema."""
    print("\n--- Adicionar Novo Documento ---")
    nome = input("Digite o nome do arquivo (ex: artigo_ia.pdf): ")
    tipo = input("Digite o tipo do arquivo (ex: PDF, ePUB, DOCX): ")
    ano_str = input("Digite o ano de publicação: ")

    # Adicionando uma conversão básica para int para a ordenação funcionar.
    # Validação completa virá depois.
    try:
        ano = int(ano_str)
    except ValueError:
        print("Aviso: Ano inválido, usando 0 para ordenação.")
        ano = 0

    documento = {"nome": nome, "tipo": tipo, "ano": ano}
    documentos_db.append(documento)
    print(f"Documento '{nome}' adicionado com sucesso!")

def listar_documentos(): # FUNÇÃO MODIFICADA
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

    documentos_para_listar = list(documentos_db) # Cria uma cópia para não alterar a original

    if escolha_organizacao == '1':
        # Organiza por tipo (ignorando maiúsculas/minúsculas) e depois por nome
        documentos_para_listar.sort(key=lambda doc: (doc['tipo'].lower(), doc['nome'].lower()))
        print("\n--- Documentos Organizados por Tipo ---")
    elif escolha_organizacao == '2':
        # Organiza por ano e depois por nome
        documentos_para_listar.sort(key=lambda doc: (doc['ano'], doc['nome'].lower()))
        print("\n--- Documentos Organizados por Ano de Publicação ---")
    elif escolha_organizacao == '3':
        print("\n--- Todos os Documentos (Ordem de Adição) ---")
        # A cópia já está na ordem de adição
    else:
        print("Opção de organização inválida. Listando na ordem padrão.")
        print("\n--- Todos os Documentos (Ordem de Adição) ---")


    for i, doc_item in enumerate(documentos_para_listar):
        print(f"{i+1}. Nome: {doc_item['nome']}, Tipo: {doc_item['tipo']}, Ano: {doc_item['ano']}")

def renomear_documento():
    """Renomeia um documento existente no sistema."""
    print("\n--- Renomear Documento ---")
    nome_antigo = input("Digite o nome do arquivo atual que deseja renomear: ")
    documento_encontrado = None
    for doc_item in documentos_db:
        if doc_item['nome'] == nome_antigo:
            documento_encontrado = doc_item
            break
    if documento_encontrado:
        novo_nome = input(f"Digite o novo nome para '{nome_antigo}': ")
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
    while True:
        print("\n====== Sistema de Gestão de Documentos da Biblioteca ======")
        print("1. Adicionar Documento")
        print("2. Listar Documentos") # A opção de listar será movida para 4 no final
        print("3. Renomear Documento")
        print("4. Remover Documento")
        print("5. Sair")
        print("==========================================================")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_documento()
        elif escolha == '2':
            listar_documentos()
        elif escolha == '3':
            renomear_documento()
        elif escolha == '4':
            remover_documento()
        elif escolha == '5':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    menu_principal()

