from funcoes import calcular_idade

nome = input("nome: ")

while nome != "0" and nome.lower() != "zero":
    idade = calcular_idade()

    print(f"seu nome é {nome}), sua idade é {idade}")
    
    nome = input("nome: ")

print("tchau")
