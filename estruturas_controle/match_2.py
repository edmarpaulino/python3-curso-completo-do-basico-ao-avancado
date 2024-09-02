def final_de_semana(dia):
    match dia:  # python >= 3.10
        case 2 | 3 | 4 | 5 | 6:
            return 'Dia de semana'
        case 1 | 7:
            return 'Final de semana'
        case _:
            return '** inválido **'


for i in range(9):
    print(f'{i}: {final_de_semana(i)}')
