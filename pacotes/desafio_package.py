from app.utils.gerador import novo_nome
from app.negocio import nome_exite
from app.negocio.backend import add_nome


def main():
    while True:
        nome = novo_nome()
        if not nome_exite(nome):
            add_nome(nome)
            break

    print(f'Criado novo nome de testes: "{nome}"')


if __name__ == '__main__':
    main()
