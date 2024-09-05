class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'nome: {self.nome} - idade: {self.idade} anos'

    def is_adult(self):
        return self.idade >= 18


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def __str__(self):
        return super().__str__() + f' - salario: {self.salario}'


class Compra():
    def __init__(self, vendedor: Vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registrar_compra(self, compra: Compra):
        self.compras.append(compra)

    def get_data_ultima_compra(self):
        ultima_compra = None
        for compra in self.compras:
            if compra.data > ultima_compra:
                ultima_compra = compra.data
        return ultima_compra

    def total_compras(self):
        total = 0
        for compra in self.compras:
            total += compra.valor
