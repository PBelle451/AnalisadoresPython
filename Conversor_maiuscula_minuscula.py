#BCC - 2º Exercício de Laboratório de Construção de Compiladores (1ª Avaliação)
#Pedro Belle Magalhães de Castro
#RA: 22103581
#Data: 05/03/2024
def converter(string):
    maiuscula = string.upper()
    minuscula = string.lower()
    lista = [maiuscula, minuscula]
    
    for i in range(len(string)):
        if string[i].islower():
            lista.append(string[:i] + maiuscula[i] + string[i+1:].upper())
            string = string[:i] + maiuscula[i] + string[i+1:]
        else:
            lista.append(string[:i] + minuscula[i] + string[i+1:].lower())
            string = string[:i] + minuscula[i] + string[i+1:]
    return lista

def main():
    while True:
        scanner = input("Insira a string... ")
        if not scanner:
            break
        if not scanner.isalpha():
            print("Por favor apenas letras")
            continue
        
        var = converter(scanner)
        print("Saída:")
        for char in var:
            print(char)

if __name__ == "__main__":
    main()
