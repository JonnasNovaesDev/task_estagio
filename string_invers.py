def inverter_string(string):
    inverted_string = ""
    for i in range(len(string) - 1, -1, -1):
        inverted_string += string[i]
    return inverted_string

entrada = input("Digite uma string: ")
string_invertida = inverter_string(entrada)
print("String invertida:", string_invertida)