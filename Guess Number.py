import random

def guess_the_number():
    nome = input("Bem-vindo! Qual é o teu nome? ")

    jogar_novamente = True

    while jogar_novamente:
        print(f"\nOlá, {nome}!Tenta adivinhar um número entre 0 e 20.")

        numero_secreto = random.randint(0, 20)
        tentativas = 6
        vencedor = False

        while tentativas > 0:
            print(f"Tens {tentativas} tentativa(s) restantes.")
            palpite = input("Adivinha o número: ")

            if not palpite.isdigit():
                print("Por favor, insere um número válido.")
                continue

            palpite = int(palpite)

            if palpite == numero_secreto:
                print(f"Parabéns, {nome}! Acertaste o número {numero_secreto}!")
                vencedor = True
                break
            elif palpite < numero_secreto:
                print("O número é maior.")
            else:
                print("O número é menor.")

            tentativas -= 1

        if not vencedor:
            print(f"Que pena, {nome}. O número era {numero_secreto}. Tenta outra vez!")

        resposta = input("Queres jogar outra vez? (sim/não): ").lower()
        if resposta != "sim":
            jogar_novamente = False

    print("Obrigado por jogar! Até à próxima.")


guess_the_number()
