from builtins import print


class Pessoa:
    olhos = 2
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
    fabio.sobrenome = 'Francischetti'
    del fabio.filhos
    fabio.olhos = 1
    del fabio.olhos
    print(fabio.__dict__)
    print(yasmin.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(fabio.olhos)
    print(yasmin.olhos)
    print(id(Pessoa.olhos), id(fabio.olhos), id(yasmin.olhos))