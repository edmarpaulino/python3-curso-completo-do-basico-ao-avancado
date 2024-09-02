# não é mas simboliza uma constante quando a variável é em SCREAMING_CASE
PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida'
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proíbida', palavra)
            found = True
            break
    if not found:
        print('Texto autorizado:', texto)
