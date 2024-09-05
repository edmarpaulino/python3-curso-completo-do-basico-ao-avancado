
class Carro:
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self, delta=5):
        if (self.velocidade_atual + delta > self.velocidade_maxima):
            self.velocidade_atual = self.velocidade_maxima
        else:
            self.velocidade_atual += delta
        return f'Acelerando... velocidade atual {self.velocidade_atual} km/h'

    def frear(self, delta=5):
        if (self.velocidade_atual - delta < 0):
            self.velocidade_atual = 0
        else:
            self.velocidade_atual -= delta
        return f'Freando... velocidade atual {self.velocidade_atual} km/h'


if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(delta=20))
