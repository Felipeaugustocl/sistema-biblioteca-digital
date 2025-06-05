documentos_db = []

def adicionar_documento():
    """Adiciona um novo documento ao sistema."""
    print("\n--- Adicionar Novo Documento ---")
    nome = input("Digite o nome do arquivo (ex: artigo_ia.pdf): ")
    tipo = input("Digite o tipo do arquivo (ex: PDF, ePUB, DOCX): ")
    ano = input("Digite o ano de publicação: ")

    documento = {"nome": nome, "tipo": tipo, "ano": ano}
    documentos_db.append(documento)
    print(f"Documento '{nome}' adicionado com sucesso!")

def listar_documentos():
    """Lista todos os documentos cadastrados."""
    if not documentos_db:
        print("\nNenhum documento cadastrado no sistema.")
        return
    print("\n--- Todos os Documentos (Ordem de Adição) ---")
    for i, doc in enumerate(documentos_db):
        print(f"{i+1}. Nome: {doc['nome']}, Tipo: {doc['tipo']}, Ano: {doc['ano']}")

def renomear_documento(): # NOVA FUNÇÃO
    """Renomeia um documento existente no sistema."""
    print("\n--- Renomear Documento ---")
    nome_antigo = input("Digite o nome do arquivo atual que deseja renomear: ")

    documento_encontrado = None
    for doc_item in documentos_db: # Renomeada variável de iteração para evitar conflito
        if doc_item['nome'] == nome_antigo:
            documento_encontrado = doc_item
            break

    if documento_encontrado:
        novo_nome = input(f"Digite o novo nome para '{nome_antigo}': ")
        # Ainda não estamos verificando se o novo_nome já existe.
        documento_encontrado['nome'] = novo_nome
        print(f"Documento '{nome_antigo}' renomeado para '{novo_nome}' com sucesso!")
    else:
        print(f"Erro: Documento '{nome_antigo}' não encontrado.")

def menu_principal():
    """Exibe o menu principal e gerencia a interação com o usuário."""
    while True:
        print("\n====== Sistema de Gestão de Documentos da Biblioteca ======")
        print("1. Adicionar Documento")
        print("2. Listar Documentos")
        print("3. Renomear Documento") # NOVA OPÇÃO
        print("5. Sair")
        print("==========================================================")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_documento()
        elif escolha == '2':
            listar_documentos()
        elif escolha == '3': # NOVA CONDIÇÃO
            renomear_documento()
        elif escolha == '5':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    menu_principal()

