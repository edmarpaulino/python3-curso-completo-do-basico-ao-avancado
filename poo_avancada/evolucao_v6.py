#!/user/local/bin/python3
from abc import ABCMeta, abstractmethod


class Humano(metaclass=ABCMeta):
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    # @abstractproperty -> forma antiga
    @property
    @abstractmethod
    def inteligente(self):
        pass

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um número positivo!')
        self._idade = idade

    def das_cavernas(self):
        # atributo da instância
        self.especie = 'Homo Neanderthalensis'
        return self

    # é como um método definido fora da classe
    # não recebe nenhum paramêtro especial (self ou cls)
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    # recebe a classe como paramêtro
    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]

    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True


if __name__ == '__main__':

    try:
        anonimo = Humano('John Doe')
        print(anonimo.inteligente)
    except Exception as e:
        print('Classe abstrata:', str(e))

    jose = HomoSapiens('José')
    print('{} da classe {}, inteligente: {}'.format(
        jose.nome, jose.__class__.__name__, jose.inteligente))
    grokn = Neanderthal('Grokn')
    print('{} da classe {}, inteligente: {}'.format(
        grokn.nome, grokn.__class__.__name__, grokn.inteligente))
