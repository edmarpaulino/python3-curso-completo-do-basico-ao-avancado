generator = (i ** 2 for i in range(10) if i % 2 == 0)

# não precisa usar o next pois o for entende que é um generator
# range() no python3 é um generator
for numero in generator:
    print(numero)
