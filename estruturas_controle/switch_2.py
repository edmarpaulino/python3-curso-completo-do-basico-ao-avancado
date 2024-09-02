def final_de_semana(dia):
    dias = {
        1: 'Final de semana',
        2: 'Dia de semana',
        3: 'Dia de semana',
        4: 'Dia de semana',
        5: 'Dia de semana',
        6: 'Dia de semana',
        7: 'Final de semana'
    }
    return dias.get(dia, '** inválido **')


for i in range(9):
    print(f'{i}: {final_de_semana(i)}')
