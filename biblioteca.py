# Lista para armazenar os metadados dos documentos.
# Cada documento será um dicionário com 'nome', 'tipo' e 'ano'.
documentos_db = []

def adicionar_documento():
    """
    Adiciona um novo documento ao sistema.
    Solicita nome, tipo e ano. Valida o ano e verifica duplicidade de nome.
    """
    print("\n--- Adicionar Novo Documento ---")
    nome = input("Digite o nome do arquivo (ex: artigo_ia.pdf): ")
    tipo = input("Digite o tipo do arquivo (ex: PDF, ePUB, DOCX): ").upper() # Padroniza para maiúsculas
    ano_str = input("Digite o ano de publicação: ")

    # Validação simples para o ano
    if not ano_str.isdigit() or len(ano_str) != 4:
        print("Erro: Ano inválido. Por favor, insira um ano com 4 dígitos.")
        return
    ano = int(ano_str)

    # Verifica se o documento já existe (pelo nome)
    for doc_item in documentos_db: # Renomeada variável de iteração
        if doc_item['nome'] == nome:
            print(f"Erro: Documento '{nome}' já existe.")
            return

    documento = {"nome": nome, "tipo": tipo, "ano": ano}
    documentos_db.append(documento)
    print(f"Documento '{nome}' adicionado com sucesso!")

def renomear_documento():
    """
    Renomeia um documento existente no sistema.
    Verifica se o novo nome já não está em uso por outro documento.
    """
    print("\n--- Renomear Documento ---")
    nome_antigo = input("Digite o nome do arquivo atual que deseja renomear: ")

    documento_encontrado = None
    indice_documento_original = -1 # Para não comparar o documento consigo mesmo
    for i, doc_item in enumerate(documentos_db): # Renomeada variável de iteração
        if doc_item['nome'] == nome_antigo:
            documento_encontrado = doc_item
            indice_documento_original = i
            break

    if documento_encontrado:
        novo_nome = input(f"Digite o novo nome para '{nome_antigo}': ")
        # Verifica se o novo nome já está em uso por outro documento
        for i_check, doc_check in enumerate(documentos_db):
            if doc_check['nome'] == novo_nome and i_check != indice_documento_original:
                print(f"Erro: O nome '{novo_nome}' já está em uso por outro documento.")
                return
        documento_encontrado['nome'] = novo_nome
        print(f"Documento '{nome_antigo}' renomeado para '{novo_nome}' com sucesso!")
    else:
        print(f"Erro: Documento '{nome_antigo}' não encontrado.")

def remover_documento():
    """Remove um documento do sistema pelo nome."""
    print("\n--- Remover Documento ---")
    nome_remover = input("Digite o nome do arquivo que deseja remover: ")

    documento_encontrado = None
    for doc_item in documentos_db: # Renomeada variável de iteração
        if doc_item['nome'] == nome_remover:
            documento_encontrado = doc_item
            break

    if documento_encontrado:
        documentos_db.remove(documento_encontrado)
        print(f"Documento '{nome_remover}' removido com sucesso!")
    else:
        print(f"Erro: Documento '{nome_remover}' não encontrado.")

def listar_documentos():
    """
    Lista todos os documentos, com opção de organização por tipo ou ano.
    A organização secundária é sempre por nome.
    """
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
        # Organiza por tipo e depois por nome dentro de cada tipo
        documentos_para_listar.sort(key=lambda doc: (doc['tipo'], doc['nome'].lower()))
        print("\n--- Documentos Organizados por Tipo ---")
    elif escolha_organizacao == '2':
        # Organiza por ano e depois por nome dentro de cada ano
        documentos_para_listar.sort(key=lambda doc: (doc['ano'], doc['nome'].lower()))
        print("\n--- Documentos Organizados por Ano de Publicação ---")
    elif escolha_organizacao == '3':
        print("\n--- Todos os Documentos (Ordem de Adição) ---")
    else:
        print("Opção de organização inválida. Listando na ordem padrão.")
        print("\n--- Todos os Documentos (Ordem de Adição) ---")

    for i, doc_item in enumerate(documentos_para_listar): # Renomeada variável de iteração
        print(f"{i+1}. Nome: {doc_item['nome']}, Tipo: {doc_item['tipo']}, Ano: {doc_item['ano']}")

def menu_principal():
    """Exibe o menu principal e gerencia a interação com o usuário."""
    while True:
        print("\n====== Sistema de Gestão de Documentos da Biblioteca ======")
        print("1. Adicionar Documento")
        print("2. Renomear Documento")
        print("3. Remover Documento")
        print("4. Listar Documentos")
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
    # Exemplo de alguns documentos para teste inicial (opcional, pode remover ou comentar)
    # documentos_db = [
    #     {"nome": "tese_doutorado_2023.pdf", "tipo": "PDF", "ano": 2023},
    #     {"nome": "manual_calouro_2022.epub", "tipo": "EPUB", "ano": 2022},
    #     {"nome": "artigo_historia_antiga.pdf", "tipo": "PDF", "ano": 2021},
    #     {"nome": "romance_classico.epub", "tipo": "EPUB", "ano": 2023},
    # ]
    menu_principal()

