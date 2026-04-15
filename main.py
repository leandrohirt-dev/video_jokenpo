import random
import time

print("=" * 30)
print("JOGO: PEDRA, PAPEL E TESOURA")
print("=" * 30)

opcoes = ["pedra", "papel", "tesoura"]

escolha_jogador = input("Escolha (pedra, papel ou tesoura): ").lower()

if escolha_jogador not in opcoes:
    print("Escolha inválida! Tente novamente.")
else:
    print("O computador está pensando...")
    time.sleep(1.5)

    escolha_computador = random.choice(opcoes)

    print(f"Você escolheu: {escolha_jogador.upper()}")
    print(f"Computador escolheu: {escolha_computador.upper()}")

    if escolha_jogador == escolha_computador:
        print("EMPATE! Ninguém ganhou.")
    elif (escolha_jogador == "pedra" and escolha_computador == "tesoura") or \
        (escolha_jogador == "papel" and escolha_computador == "pedra") or \
        (escolha_jogador == "tesoura" and escolha_computador == "papel"):
        print("VOCÊ VENCEU! PARABÉNS!")
    else:
        print("VOCÊ PERDEU! O computador ganhou.")