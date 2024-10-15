def is_fibonacci(num):
    if num < 0:
        return False, []

    # Inicializa a sequência de Fibonacci
    fibonacci_sequence = [0, 1]
    
    # Gera a sequência até ultrapassar o número informado
    while fibonacci_sequence[-1] < num:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    
    # Verifica se o número informado está na sequência
    if num in fibonacci_sequence:
        return True, fibonacci_sequence
    else:
        return False, fibonacci_sequence

# Solicita ao usuário um número
numero_informado = int(input("Ei, me fala um número e eu te digo se ele está na sequência de Fibonacci: "))
pertence, sequencia = is_fibonacci(numero_informado)

# Exibe o resultado de forma amigável
if pertence:
    print(f"Uau! O número {numero_informado} faz parte da sequência de Fibonacci. Olha só a sequência até aqui: {sequencia}")
else:
    print(f"Hmm... o número {numero_informado} não está na sequência de Fibonacci. Mas veja a sequência gerada: {sequencia}")
