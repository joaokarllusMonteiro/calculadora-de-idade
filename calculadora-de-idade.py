from datetime import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    return ano_atual - ano_nascimento

def obter_ano_nascimento_valido():
    while True:
        try:
            ano = int(input("Digite o seu ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("Erro: Ano inválido. Por favor, digite um ano entre 1922 e 2021.")
        except ValueError:
            print("Erro: Por favor, digite um número válido.")

def main():
    nome_completo = input("Digite o seu nome completo: ")
    ano_nascimento = obter_ano_nascimento_valido()
    idade = calcular_idade(ano_nascimento)
    print(f"{nome_completo}, você completou ou completará {idade} anos no ano de 2022.")

# Executa o programa principal
main()
