def verificar_letra_a(string):
    # Converte a string para minúsculas para contar tanto 'a' quanto 'A'
    string_lower = string.lower()
    
    # Conta quantas vezes a letra 'a' aparece
    contagem = string_lower.count('a')
    
    # Verifica se a letra 'a' aparece e dá um retorno mais humano
    if contagem > 0:
        print(f"Legal! A letra 'a' aparece {contagem} vezes na sua frase.")
    else:
        print("Hmm... parece que a letra 'a' não aparece na sua frase.")

# Solicita ao usuário uma string com uma abordagem mais amigável
texto = input("Me diga uma palavra ou frase e eu vou contar quantas vezes a letra 'a' aparece: ")

# Chama a função para verificar a letra 'a'
verificar_letra_a(texto)
