# -*- coding: utf-8 -*-

from datetime import datetime
from filme import Filme
from filme_dao import FilmeDAO
import traceback

filmeDao = FilmeDAO('banco.txt')
quer_fazer_algo = True

def _mostra_painel():
    print('')
    print('#### PAINEL INTERATIVO ####')
    print('')
    print('## PARA INTERAGIR DIGITE ##')
    print('')
    print('1 - ADICIONAR FILME')
    print('2 - BUSCAR FILME')
    print('3 - ALTERAR FILME')
    print('4 - DELETAR FILME')
    print('5 - LISTAR FILMES')
    print('6 - SAIR')
    print('')
    print('###########################')
    print('')
    comando = input('INFORME UM COMANDO:')
    print('')
    return comando

while(quer_fazer_algo):
    comando = _mostra_painel()

    if (comando == 1):
        parametros = ['nome', 'genero', 'duracao', 'data de lançamento']
        valores = []

        for i in range(4):
            elemento = input('Informe '+parametros[i]+': ')
            valores.append(elemento)

        try:
            filmeDao.inserir(Filme(valores[0], valores[1], valores[2], valores[3]))
        except TypeError as err:
            traceback.print_exc()
    elif (comando == 2):
        print('')
        id_busca = input('INFORME O ID PARA BUSCAR:')
        print('')
        try:
            retorno = filmeDao.buscar(id_busca)
            print(retorno)
        except ValueError as err:
            traceback.print_exc()
        except TypeError as err:
            traceback.print_exc()
    elif (comando == 3):
        print('')
        id_busca = input('INFORME O ID PARA BUSCAR:')
        print('')
        try:
            retorno = filmeDao.buscar(id_busca)
            parametros = ['NOME', 'GENERO', 'DURAÇÃO', 'DATA DE LANÇAMENTO']
            valores = []
            for i in range(4):
                elemento = input('INFORME O NOVO '+parametros[i]+': ')
                valores.append(elemento)
            retorno._nome = valores[0]
            retorno._genero = valores[1]
            retorno._duracao = valores[2]
            retorno._data_lancamento = datetime.strptime(valores[3], '%d/%m/%Y')
            filmeDao.alterar(retorno)
        except ValueError as err:
            traceback.print_exc()
        except TypeError as err:
            traceback.print_exc()
    elif (comando == 4):
        print('')
        entrada = input('INFORME O ID PARA DELETAR:')
        print('')

        try:
            filmeDao.deletar(entrada)
        except ValueError as err:
            traceback.print_exc()
        except TypeError as err:
            traceback.print_exc()

    elif (comando == 5):
        filmeDao.listar()
    elif (comando == 6):
        quer_fazer_algo = False
    else:
        print('erro')
