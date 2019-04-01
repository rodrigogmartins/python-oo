# -*- coding: utf-8 -*-

from datetime import datetime

class Filme:
    def __init__(self, nome, genero, duracao, data_lancamento):
        self._id = None
        self._nome = nome
        self._genero = genero
        self._duracao = duracao
        if (isinstance(data_lancamento, datetime)):
            self._data_lancamento = data_lancamento

        elif (isinstance(data_lancamento, str)):
            self._data_lancamento = datetime.strptime(data_lancamento, '%d/%m/%Y')

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @property
    def duracao(self):
        return self._duracao

    @duracao.setter
    def duracao(self, duracao):
        self._duracao = duracao

    @property
    def data_lancamento(self):
        return self._data_lancamento

    @data_lancamento.setter
    def data_lancamento(self, data_lancamento):
        if (isinstance(data_lancamento, datetime)):
            self._data_lancamento = data_lancamento

        elif (isinstance(data_lancamento, str)):
            self._data_lancamento = datetime.strptime(data_lancamento, '%d/%m/%Y')

    def formata_para_escrever_no_banco(self):
        return str(self._id) + ',' + self._nome + ',' + self._genero + ',' + str(self._duracao) + ',' + self._data_lancamento.strftime('%d/%m/%Y') + '\n'

    def __str__(self):
        return 'Id: ' + str(self._id) + '\nNome: ' + self._nome + '\nGenero: ' + self._genero + '\nDuracao: ' + self._duracao + ' minutos\nData de Lançamento: ' + self._data_lancamento.strftime('%d/%m/%Y')
