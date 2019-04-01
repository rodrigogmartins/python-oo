# -*- coding: utf-8 -*-

from filme import Filme

class FilmeDAO:

    def __init__(self, nome_arquivo):
        self._nome_arquivo = nome_arquivo

    def _ler_arquivo(self):
        try:
            with open(self._nome_arquivo, 'r') as arquivo:
                return arquivo.readlines()
        except IOError:
            print('Arquivo não encontrado!')
        except:
            print('Ocorreu algum erro ao tentar ler o arquivo!')

    def _escrever_arquivo(self, conteudo):
        try:
            with open(self._nome_arquivo, 'w') as arquivo:
                arquivo.writelines(conteudo)
        except IOError:
            print('Arquivo não encontrado!')
        except:
            print('Ocorreu algum erro ao tentar escrever o arquivo!')

    def _get_posicao_objeto(self, id_objeto, lista):
        for i in range(1, len(lista)):
            linha_em_vetor = lista[i].split(',')
            if (int(linha_em_vetor[0]) == id_objeto):
                return i

        return -1

    def _criar_lista_de_obj(self, conteudo):
        lista = []

        for i in range(1, len(conteudo)):
            linha_em_vetor = conteudo[i].split(',')
            elemento = Filme(linha_em_vetor[1], linha_em_vetor[2], linha_em_vetor[3], linha_em_vetor[4].replace('\n', ''))
            elemento._id = linha_em_vetor[0]
            lista.append(elemento)

        return lista

    def inserir(self, obj):
        conteudo = self._ler_arquivo()
        id_objeto = int(conteudo[0]) + 1
        conteudo[0] = str(id_objeto) + '\n'

        if (isinstance(obj, Filme)):
            obj._id = id_objeto
            obj_formato_string = obj.formata_para_escrever_no_banco()
            conteudo.append(obj_formato_string)

            self._escrever_arquivo(conteudo)
        else:
            raise TypeError('Parameter <type \'Filme\'> is expected but found is: ' + str(type(obj)))

    def alterar(self, obj):
        conteudo = self._ler_arquivo()

        obj_formato_string = obj.formata_para_escrever_no_banco()
        posicao = self._get_posicao_objeto(obj._id, conteudo)
        conteudo[posicao] = obj_formato_string

        self._escrever_arquivo(conteudo)

    def buscar(self, id):
        if (isinstance(id, int)):
            conteudo = self._ler_arquivo()
            posicao = self._get_posicao_objeto(id, conteudo)

            if (posicao != -1):
                linha_em_vetor = conteudo[posicao].split(',')
                resultado = Filme(linha_em_vetor[1], linha_em_vetor[2], linha_em_vetor[3], linha_em_vetor[4].replace('\n', ''))
                resultado._id = linha_em_vetor[0]
                return resultado
            else:
                raise ValueError('Id '+str(id)+' do not exists')

        else:
            raise TypeError('Parameter <type \'int\'> is expected but found is: ' + str(type(id)))

    def deletar(self, id):
        if (isinstance(id, int)):
            conteudo = self._ler_arquivo()
            posicao = self._get_posicao_objeto(id, conteudo)

            if (posicao != -1):
                conteudo.pop(posicao)
                self._escrever_arquivo(conteudo)
            else:
                raise ValueError('Id '+str(id)+' do not exists')
        else:
            raise TypeError('Parameter <type \'int\'> is expected but found is: ' + str(type(id)))

    def listar(self):
        conteudo = self._ler_arquivo()
        lista_obj = self._criar_lista_de_obj(conteudo)

        for i in range(len(lista_obj)):
            print(str(lista_obj[i]) + '\n')

