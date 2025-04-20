import random

# Lista de palavras para o jogo
palavras = ["python", "computador", "janela", "teclado", "monitor"]

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



# Executar o jogo
if __name__ == "__main__":
    jogar()