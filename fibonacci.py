def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num

def main():
    try:
        numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
        if is_fibonacci(numero):
            print(f"{numero} pertence à sequência de Fibonacci.")
        else:
            print(f"{numero} não pertence à sequência de Fibonacci.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

if __name__ == "__main__":
    main()