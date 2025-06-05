import json # Importa o módulo JSON
import os # Para verificar se o arquivo existe

# Nome do arquivo para persistência de dados
NOME_ARQUIVO_DADOS = "biblioteca_data.json"

# Lista para armazenar os metadados dos documentos.
# Será carregada do arquivo JSON ou iniciada como vazia.
documentos_db = []

def carregar_dados():
    """Carrega os dados dos documentos do arquivo JSON."""
    global documentos_db
    if os.path.exists(NOME_ARQUIVO_DADOS):
        try:
            with open(NOME_ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
                documentos_db = json.load(f)
            print(f"Dados carregados de '{NOME_ARQUIVO_DADOS}'.")
        except json.JSONDecodeError:
            print(f"Erro: Arquivo '{NOME_ARQUIVO_DADOS}' está corrompido ou não é um JSON válido. Iniciando com banco de dados vazio.")
            documentos_db = []
        except Exception as e:
            print(f"Erro inesperado ao carregar dados: {e}. Iniciando com banco de dados vazio.")
            documentos_db = []
    else:
        print(f"Arquivo '{NOME_ARQUIVO_DADOS}' não encontrado. Iniciando com banco de dados vazio.")
        documentos_db = []

def salvar_dados():
    """Salva os dados dos documentos no arquivo JSON."""
    try:
        with open(NOME_ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
            json.dump(documentos_db, f, indent=4, ensure_ascii=False)
        # print(f"Dados salvos em '{NOME_ARQUIVO_DADOS}'.") # Opcional: feedback a cada salvamento
    except Exception as e:
        print(f"Erro ao salvar dados em '{NOME_ARQUIVO_DADOS}': {e}")


def adicionar_documento():
    """
    Adiciona um novo documento ao sistema com detalhes expandidos.
    Solicita nome do arquivo, título completo, autores, ano, tipo,
    palavras-chave e caminho do arquivo.
    """
    print("\n--- Adicionar Novo Documento (Detalhado) ---")
    nome_arquivo = input("Digite o nome do arquivo (ex: tese_ia.pdf): ")
    for doc_item in documentos_db:
        if doc_item['nome_arquivo'] == nome_arquivo:
            print(f"Erro: Documento com nome de arquivo '{nome_arquivo}' já existe.")
            return

    titulo_completo = input("Digite o título completo do documento: ")
    autores_str = input("Digite o(s) autor(es) (separados por vírgula): ")
    autores = [autor.strip() for autor in autores_str.split(',')]

    ano_str = input("Digite o ano de publicação: ")
    if not ano_str.isdigit() or len(ano_str) != 4:
        print("Erro: Ano inválido. Por favor, insira um ano com 4 dígitos.")
        return
    ano = int(ano_str)

    tipo = input("Digite o tipo do arquivo (ex: PDF, ePUB, DOCX): ").upper()
    palavras_chave_str = input("Digite as palavras-chave (separadas por vírgula): ")
    palavras_chave = [kw.strip() for kw in palavras_chave_str.split(',')]

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
    salvar_dados() # Salva após adicionar
    print(f"Documento '{titulo_completo}' adicionado com sucesso!")

def renomear_documento():
    """
    Renomeia o nome do arquivo de um documento existente.
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
        for i_check, doc_check in enumerate(documentos_db):
            if doc_check['nome_arquivo'] == novo_nome_arquivo and i_check != indice_documento_original:
                print(f"Erro: O nome de arquivo '{novo_nome_arquivo}' já está em uso.")
                return
        documento_encontrado['nome_arquivo'] = novo_nome_arquivo
        salvar_dados() # Salva após renomear
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
        salvar_dados() # Salva após remover
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
        print(f"   Autores: {', '.join(doc_item['autores'])}")
        print(f"   Ano: {doc_item['ano']}")
        print(f"   Tipo: {doc_item['tipo']}")
        print(f"   Palavras-chave: {', '.join(doc_item['palavras_chave'])}")
        print(f"   Caminho: {doc_item['caminho_arquivo']}")
    print("-" * 20)


def menu_principal():
    """Exibe o menu principal e gerencia a interação com o usuário."""
    carregar_dados() # Carrega os dados ao iniciar o programa
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
            # salvar_dados() # Já é salvo após cada operação, mas pode ser um último save aqui se preferir.
            # Decidi salvar após cada operação para maior segurança em caso de fechamento inesperado.
            print("Saindo do sistema. Dados foram salvos. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    menu_principal()

