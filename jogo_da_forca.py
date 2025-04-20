import random

# Lista de palavras para o jogo
palavras = {
    "tecnologia": ["python", "computador", "janela", "teclado", "monitor"],
    "animais": ["girafa", "elefante", "leopardo", "rinoceronte"],
    "frutas": ["banana", "abacaxi", "morango", "laranja"]
}

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

def jogar(categoria=None, tentativas=6):
    if categoria:
        palavra_secreta = random.choice(palavras[categoria])
    else:
        todas_palavras = []
        for cat in palavras.values():
            todas_palavras.extend(cat)
        palavra_secreta = random.choice(todas_palavras)

    letras_descobertas = ["_" for _ in palavra_secreta]
    letras_erradas = []

    print(f"\nCOMEÇANDO O JOGO! POSSUI ({tentativas} tentativas)")

    while tentativas > 0 and "_" in letras_descobertas:
            print("\nPalavra:", " ".join(letras_descobertas))
            print("Tentativas restantes:", tentativas)
            if letras_erradas:
                print("Letras erradas:", ", ".join(letras_erradas))
            
            palpite = input("Digite uma letra: ").lower()

            if len(palpite) != 1 or not palpite.isalpha():
                print("Entrada inválida. Digite apenas UMA letra.")
                continue
            
            if palpite in letras_descobertas or palpite in letras_erradas:
                print("Você já tentou esta letra!")
                continue

            if palpite in palavra_secreta:
                for i, letra in enumerate(palavra_secreta):
                    if letra == palpite:
                        letras_descobertas[i] = palpite
                print("Letra correta!") 

            else:
                letras_erradas.append(palpite)
                tentativas -= 1
                print(f"Letra incorreta! Restam {tentativas} tentativas.")

    if "_" not in letras_descobertas:
        print(f"\nPARABÉNS! Você acertou: {palavra_secreta.upper()}")
    else:
        print(f"\nFIM DE JOGO! A palavra era: {palavra_secreta.upper()}")

def main():
    config = {
        "categoria": None,
        "tentativas": 6
    }

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            jogar(config["categoria"], config["tentativas"])
            input("\nPressione ENTER para continuar...")
        elif opcao == "2":
            categoria = menu_categorias()
            if categoria:
                config["categoria"] = categoria
                print(f"Categoria selecionada: {categoria.capitalize()}")
        elif opcao == "3":
            tentativas = menu_dificuldade()
            if tentativas:
                config["tentativas"] = tentativas
                print(f"Dificuldade alterada para {tentativas} tentativas")
        elif opcao == "4":
            print("\nESTATÍSTICAS (em desenvolvimento)")
            input("Pressione Enter para continuar...")
        elif opcao == "5":
            sobre_jogo()
        elif opcao == "6":
            print("\nObrigado por jogar! Até a próxima!")
            break
        else:
            print("Opção inválida! Tente novamente.")
        


'''
def jogar():
    while True:
        palavra_secreta = random.choice(palavras)
        letras_descobertas = ["_" for _ in palavra_secreta]
        tentativas_restantes = 6
        letras_erradas = []
        
        print("Bem-vindo ao Jogo da Forca!")
        
        while tentativas_restantes > 0 and "_" in letras_descobertas:
            print("\nPalavra:", " ".join(letras_descobertas))
            print("Tentativas restantes:", tentativas_restantes)
            print("Letras erradas:", ", ".join(letras_erradas))
            
            palpite = input("Digite uma letra: ").lower()

            if not palpite.isalpha() or len(palpite) != 1:
                print("Entrada inválida. Digite apenas uma letra.")
                continue
            
            if palpite in letras_descobertas or palpite in letras_erradas:
                print("Já tentou essa letra.")
                continue

            if palpite in palavra_secreta:
                for i, letra in enumerate(palavra_secreta):
                    if letra == palpite:
                        letras_descobertas[i] = palpite
                print("Boa! Letra correta.")
            else:
                letras_erradas.append(palpite)
                tentativas_restantes -= 1
                print("Letra incorreta. Tente novamente!!!")
        
        if "_" not in letras_descobertas:
            print("\n Parabéns! Você descobriu a palavra:", palavra_secreta)
        else:
            print("\n Fim de jogo! A palavra era:", palavra_secreta)

        jogar_de_novo = input("\nDeseja jogar novamente? (s/n): ").lower()
        if jogar_de_novo != 's':
            print("Obrigado por jogar! Até à próxima!")
            break
'''


# Executar o jogo
if __name__ == "__main__":
    main()
