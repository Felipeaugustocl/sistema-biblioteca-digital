# Lista para armazenar os metadados dos documentos.
# Cada documento será um dicionário com 'nome', 'tipo' e 'ano'.
documentos_db = []

def adicionar_documento():
    """Adiciona um novo documento ao sistema."""
    print("\n--- Adicionar Novo Documento ---")
    nome = input("Digite o nome do arquivo (ex: artigo_ia.pdf): ")
    tipo = input("Digite o tipo do arquivo (ex: PDF, ePUB, DOCX): ")
    ano = input("Digite o ano de publicação: ")

    # Neste passo, ainda não temos validações ou conversão de tipo para o ano.
    documento = {"nome": nome, "tipo": tipo, "ano": ano}
    documentos_db.append(documento)
    print(f"Documento '{nome}' adicionado com sucesso!")

def menu_principal():
    """Exibe o menu principal e gerencia a interação com o usuário."""
    while True:
        print("\n====== Sistema de Gestão de Documentos da Biblioteca ======")
        print("1. Adicionar Documento")
        print("5. Sair") # Usaremos 5 para Sair por enquanto, ajustaremos depois.
        print("==========================================================")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_documento()
        elif escolha == '5':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    menu_principal()
