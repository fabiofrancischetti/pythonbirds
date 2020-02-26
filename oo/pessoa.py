from builtins import print


class Pessoa:
    def __init__(self, *filhos, nome=None, idade=39):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    yasmin = Pessoa(nome='Yasmin')
    fabio = Pessoa(yasmin, nome='Fabio')
    print(Pessoa.cumprimentar(fabio))
    print(id(fabio))
    print(fabio.cumprimentar())
    print(fabio.nome)
    print(fabio.idade)
    for filho in fabio.filhos:
        print(filho.nome)