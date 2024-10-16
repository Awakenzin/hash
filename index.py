texto = str(input('Digite algo: ')).strip()

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '@', '#', '$', '%', '&']

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


def incript(x): 
    
    novo_texto = list (x.upper())
    hash_text = []
    for letra in novo_texto: 
        index = alfabeto.index(letra)
        hash_text.append(num[index])
    
    final_hash =  ''.join(str(hn) for hn in hash_text)

    print("Seu hash code é: ", final_hash) 


incript(texto)
