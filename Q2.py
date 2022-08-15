num = int(input("Digite um número para verificar se ele pertence a Sequência de Fibonacci: "))
a, b = 0, 1
while b < num:
    a, b = b, a + b
if b == num:
    print(num, "pertence")
else:
    print(num, "não pertence")