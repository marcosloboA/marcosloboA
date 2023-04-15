from datetime import date

hoje = date.today()

def calcular_idade():
    data_de_nascimento = input("Data de nascimento: ")
        
    if len(data_de_nascimento) != 10:
        print("Erro. Digite ex:00/00/0000")
        return -1

    if "/" not in data_de_nascimento:
        print("Erro. Digite ex:00/00/0000")
        return -1

    data_de_nascimento = data_de_nascimento.split('/')

    nascimento = {
        "dia" : int(data_de_nascimento[0]),
        "mês" : int(data_de_nascimento[1]),
        "ano" : int(data_de_nascimento[2])
    }

    idade = int(hoje.year - nascimento["ano"])

    if hoje < date(hoje.year, nascimento["Mês"], nascimento["dia"]):
        idade -= 1
    
    return idade
