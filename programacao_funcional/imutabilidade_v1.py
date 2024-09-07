#! /usr/local/bin/python3

from locale import setlocale, LC_ALL
from calendar import mdays, month_name
# from functools import reduce


# Português do Brasil
setlocale(LC_ALL, 'pt_BR')

# Listar todos os meses do ano com 31 dias

month_days = zip(month_name, mdays)
has_31_days = filter(lambda month: month[-1] == 31, month_days)
print('Meses com 31 dias:')
[print(f'{mes[0]} tem {mes[-1]} dias.') for mes in list(has_31_days)]
