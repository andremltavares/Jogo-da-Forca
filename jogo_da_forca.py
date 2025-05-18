import random
from historico import registrar_pontuacao, carregar_historico

historico_pontuacoes = []

# Lista de palavras para o jogo
palavras = {
    "tecnologia": ["python", "computador", "janela", "teclado", "monitor"],
    "animais": ["girafa", "elefante", "leopardo", "rinoceronte"],
    "frutas": ["banana", "abacaxi", "morango", "laranja"]
}

# Arte ASCII para o jogo da forca
hangman_art = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

def mostrar_menu():
    print("\n" + "="*30)
    print("  JOGO DA FORCA - MENU PRINCIPAL")
    print("="*30)
    print("1. Jogar (Modo Normal)")
    print("2. Escolher Categoria")
    print("3. Configurar Dificuldade")
    print("4. Ver Estatísticas")
    print("5. Sobre o Jogo")
    print("6. Sair")
    print("="*30)

def menu_categorias():
    print("\nCATEGORIAS DISPONÍVEIS:")
    for i, categoria in enumerate(palavras.keys(), 1):
        print(f"{i}. {categoria.capitalize()} ({len(palavras[categoria])} palavras)")

    while True:
        try:
            opcao = int(input("Escolha uma categoria (0 = Voltar): "))
            if opcao == 0:
                return None
            return list(palavras.keys())[opcao-1]
        except(ValueError, IndexError):
            print("Opção inválida! Tente novamente.")

def menu_dificuldade():
    dificuldades = {
        1: {"nome": "Fácil", "tentativas": 8},
        2: {"nome": "Normal", "tentativas": 6},
        3: {"nome": "Difícil", "tentativas": 4}
    }

    print("\nNÍVEIS DE DIFICULDADE:")
    for key, value in dificuldades.items():
        print(f"{key}. {value['nome']} ({value['tentativas']} tentativas)")

    while True:
        try:
            opcao = int(input("Escolha (0=Voltar): "))
            if opcao == 0:
                return None
            return dificuldades[opcao]["tentativas"]
        except (ValueError, KeyError):
            print("Opção inválida! Tente novamente.")

def sobre_jogo():
    print("\nSOBRE O JOGO:")
    print("Desenvolvedor: André Tavares")
    print("Jogo desenvolvido em Python")
    input("\nPressione Enter para voltar...")

def mostrar_forca(erros, max_erros):
    """Mostra a arte ASCII da forca de acordo com os erros"""
    # Ajusta para mostrar a arte completa quando chegar no máximo de erros
    etapa = min(erros, len(hangman_art) - 1)
    print(hangman_art[etapa])

def jogar(categoria=None, tentativas=6):
    palavra_secreta = random.choice(palavras[categoria]) if categoria else random.choice(sum(palavras.values(), []))
    letras_descobertas = ["_" for _ in palavra_secreta]
    letras_erradas = []

    print(f"\nCOMEÇANDO O JOGO! ({tentativas} tentativas)")

    while tentativas > 0 and "_" in letras_descobertas:
        print(hangman_art[len(letras_erradas)])
        print("\nPalavra:", " ".join(letras_descobertas))
        print("Tentativas restantes:", tentativas)
        if letras_erradas:
            print("Letras erradas:", ", ".join(letras_erradas))
        
        palpite = input("Digite uma letra: ").lower()
        if len(palpite) != 1 or not palpite.isalpha():
            print("Erro: Digite UMA letra válida (a-z).")
            continue

        if palpite in letras_descobertas + letras_erradas:
            print("Letra repetida!")
            continue

        if palpite in palavra_secreta:
            letras_descobertas = [palpite if letra == palpite else lt for lt, letra in zip(letras_descobertas, palavra_secreta)]
        else:
            letras_erradas.append(palpite)
            tentativas -= 1

    print(hangman_art[len(letras_erradas)])  # Mostra estado final

    if "_" not in letras_descobertas:
        pontos = calcular_pontuacoes(palavra_secreta, tentativas, len(letras_erradas))
        dificuldade = "Fácil" if tentativas > 6 else "Normal" if tentativas == 6 else "Difícil"
        #print(f"\nDEBUG: Antes de registrar pontuação")
        registrar_pontuacao(pontos, palavra_secreta, dificuldade)
        #print(f"\nDEBUG: Depois de registrar pontuação")
        print(f"\n🌟 Pontuação: {pontos}")
    else:
        print(f"\nFim de jogo! A palavra era: {palavra_secreta.upper()}")

def calcular_pontuacoes(palavra, tentativas_restantes, erros):
    """A pontuação é calculada baseada em:
    - Tamanho da palavra
    - Tentativas não usadas
    - Erros cometidos"""
    pontos = len(palavra) * 5 + tentativas_restantes * 2 - erros * 3
    return max(10, pontos)

def mostrar_estatisticas():
    historico = carregar_historico()
    if not historico:
        print("\n⚠️ Nenhuma pontuação registrada.")
    else:
        print("\n📊 ESTATÍSTICAS")
        print(f"🎯 Melhor pontuação: {max(h['pontos'] for h in historico)}")
        print(f"📅 Última vitória: {historico[-1]['data']}")
        print(f"🔠 Palavra: {historico[-1]['palavra'].upper()} (Dificuldade: {historico[-1]['dificuldade']})")

def main():
    config = {
        "categoria": None,
        "tentativas": 6
    }

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opcao [1-6]: ")

        if not opcao.isdigit() or int(opcao) not in range(1, 7):
            print("Erro: Digite um número entre 1 e 6!")
            continue

        opcao = int(opcao)

        if opcao == 1:
            jogar(config["categoria"], config["tentativas"])
            input("\nPressione ENTER para continuar...")
        elif opcao == 2:
            categoria = menu_categorias()
            if categoria:
                config["categoria"] = categoria
                print(f"Categoria selecionada: {categoria.capitalize()}")
        elif opcao == 3:
            tentativas = menu_dificuldade()
            if tentativas:
                config["tentativas"] = tentativas
                print(f"Dificuldade alterada para {tentativas} tentativas")
        elif opcao == 4:
            mostrar_estatisticas()
            input("Pressione Enter para continuar...")
        elif opcao == 5:
            sobre_jogo()
        elif opcao == 6:
            print("\nObrigado por jogar! Até a próxima!")
            break
        else:
            print("Opção inválida! Tente novamente.")
        

# Executar o jogo
if __name__ == "__main__":
    main()