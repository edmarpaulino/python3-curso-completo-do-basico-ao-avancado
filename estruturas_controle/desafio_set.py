PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida'
]

# minha solução
for texto in textos:
    palavras = set(texto.lower().split()).intersection(PALAVRAS_PROIBIDAS)
    if len(palavras) > 0:
        print('Texto possui pelo menos uma palavra proíbida', palavras)
    else:
        print('Texto autorizado:', texto)

# resposta
for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui palavras proíbidas', intersecao)
    else:
        print('Texto autorizado:', texto)
