# Lista para armazenar os metadados dos documentos.
documentos_db = []

def adicionar_documento():
    """
    Adiciona um novo documento ao sistema com detalhes expandidos.
    Solicita nome do arquivo, título completo, autores, ano, tipo,
    palavras-chave e caminho do arquivo.
    """
    print("\n--- Adicionar Novo Documento (Detalhado) ---")
    nome_arquivo = input("Digite o nome do arquivo (ex: tese_ia.pdf): ")
    # Verifica se o nome do arquivo já existe
    for doc_item in documentos_db:
        if doc_item['nome_arquivo'] == nome_arquivo:
            print(f"Erro: Documento com nome de arquivo '{nome_arquivo}' já existe.")
            return

    titulo_completo = input("Digite o título completo do documento: ")
    autores_str = input("Digite o(s) autor(es) (separados por vírgula): ")
    autores = [autor.strip() for autor in autores_str.split(',')] # Converte para lista

    ano_str = input("Digite o ano de publicação: ")
    if not ano_str.isdigit() or len(ano_str) != 4:
        print("Erro: Ano inválido. Por favor, insira um ano com 4 dígitos.")
        return
    ano = int(ano_str)

    tipo = input("Digite o tipo do arquivo (ex: PDF, ePUB, DOCX): ").upper()
    palavras_chave_str = input("Digite as palavras-chave (separadas por vírgula): ")
    palavras_chave = [kw.strip() for kw in palavras_chave_str.split(',')] # Converte para lista

    caminho_arquivo = input("Digite o caminho/localização do arquivo digital: ")


    documento = {
        "nome_arquivo": nome_arquivo,
        "titulo_completo": titulo_completo,
        "autores": autores,
        "ano": ano,
        "tipo": tipo,
        "palavras_chave": palavras_chave,
        "caminho_arquivo": caminho_arquivo
    }
    documentos_db.append(documento)
    print(f"Documento '{titulo_completo}' adicionado com sucesso!")

def renomear_documento():
    """
    Renomeia o nome do arquivo de um documento existente.
    Outros campos podem ser editados por uma futura função "editar_documento".
    """
    print("\n--- Renomear Nome do Arquivo do Documento ---")
    nome_antigo = input("Digite o nome do arquivo atual que deseja renomear: ")

    documento_encontrado = None
    indice_documento_original = -1
    for i, doc_item in enumerate(documentos_db):
        if doc_item['nome_arquivo'] == nome_antigo:
            documento_encontrado = doc_item
            indice_documento_original = i
            break

    if documento_encontrado:
        novo_nome_arquivo = input(f"Digite o novo nome do arquivo para '{nome_antigo}': ")
        # Verifica se o novo nome de arquivo já está em uso por outro documento
        for i_check, doc_check in enumerate(documentos_db):
            if doc_check['nome_arquivo'] == novo_nome_arquivo and i_check != indice_documento_original:
                print(f"Erro: O nome de arquivo '{novo_nome_arquivo}' já está em uso.")
                return
        documento_encontrado['nome_arquivo'] = novo_nome_arquivo
        print(f"Nome do arquivo '{nome_antigo}' renomeado para '{novo_nome_arquivo}' com sucesso!")
    else:
        print(f"Erro: Documento com nome de arquivo '{nome_antigo}' não encontrado.")

def remover_documento():
    """Remove um documento do sistema pelo nome do arquivo."""
    print("\n--- Remover Documento ---")
    nome_remover = input("Digite o nome do arquivo do documento que deseja remover: ")

    documento_encontrado = None
    for doc_item in documentos_db:
        if doc_item['nome_arquivo'] == nome_remover:
            documento_encontrado = doc_item
            break

    if documento_encontrado:
        documentos_db.remove(documento_encontrado)
        print(f"Documento com nome de arquivo '{nome_remover}' removido com sucesso!")
    else:
        print(f"Erro: Documento com nome de arquivo '{nome_remover}' não encontrado.")

def listar_documentos():
    """
    Lista todos os documentos com seus detalhes expandidos.
    A organização secundária é sempre por nome do arquivo.
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

    documentos_para_listar = list(documentos_db)

    if escolha_organizacao == '1':
        documentos_para_listar.sort(key=lambda doc: (doc['tipo'], doc['titulo_completo'].lower()))
        print("\n--- Documentos Organizados por Tipo ---")
    elif escolha_organizacao == '2':
        documentos_para_listar.sort(key=lambda doc: (doc['ano'], doc['titulo_completo'].lower()))
        print("\n--- Documentos Organizados por Ano de Publicação ---")
    elif escolha_organizacao == '3':
        print("\n--- Todos os Documentos (Ordem de Adição) ---")
    else:
        print("Opção de organização inválida. Listando na ordem padrão.")
        print("\n--- Todos os Documentos (Ordem de Adição) ---")

    for i, doc_item in enumerate(documentos_para_listar):
        print(f"\n{i+1}. Título: {doc_item['titulo_completo']}")
        print(f"   Nome do Arquivo: {doc_item['nome_arquivo']}")
        print(f"   Autores: {', '.join(doc_item['autores'])}") # Junta a lista de autores
        print(f"   Ano: {doc_item['ano']}")
        print(f"   Tipo: {doc_item['tipo']}")
        print(f"   Palavras-chave: {', '.join(doc_item['palavras_chave'])}") # Junta a lista
        print(f"   Caminho: {doc_item['caminho_arquivo']}")
    print("-" * 20)


def menu_principal():
    """Exibe o menu principal e gerencia a interação com o usuário."""
    # carregar_dados() # Será adicionado no próximo passo
    while True:
        print("\n====== Sistema de Gestão de Documentos da Biblioteca ======")
        print("1. Adicionar Documento")
        print("2. Renomear Nome de Arquivo de Documento")
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
            # salvar_dados() # Será adicionado no próximo passo
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    menu_principal()

