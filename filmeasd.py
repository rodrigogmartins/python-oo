
def listar():
    arquivo = open('banco.txt', 'r')
    conteudo = arquivo.readlines()
    arquivo.close()

    lista = []

    for i in range(1, len(conteudo)):
        linha_em_vetor = conteudo[i].split(',')
        elemento = Filme(linha_em_vetor[1], linha_em_vetor[2], linha_em_vetor[3], linha_em_vetor[4].replace('\n', ''))
        elemento._id = linha_em_vetor[0]
        lista.append(elemento)

    for i in range(len(lista)):
        print(str(lista[i]) + '\n')

def buscar(id):
    arquivo = open('banco.txt', 'r')
    conteudo = arquivo.readlines()
    arquivo.close()

    for i in range(1, len(conteudo)):
        linha_em_vetor = conteudo[i].split(',')
        if (int(linha_em_vetor[0]) == id):
            posicao = i

    return conteudo[posicao].replace('\n', '')

def deletar(id):
    arquivo = open('banco.txt', 'r')
    conteudo = arquivo.readlines()

    for i in range(1, len(conteudo)):
        linha_em_vetor = conteudo[i].split(',')
        if (int(linha_em_vetor[0]) == id):
            posicao = i

    conteudo.pop(posicao)

    arquivo = open('banco.txt', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()

def alterar(obj):
    arquivo = open('banco.txt', 'r')
    conteudo = arquivo.readlines()
    id_objeto = obj._id

    for i in range(1, len(conteudo)):
        linha_em_vetor = conteudo[i].split(',')
        if (int(linha_em_vetor[0]) == id_objeto):
            posicao = i

    obj_formato_string = obj.formata_para_escrever_no_banco()
    conteudo[posicao] = obj_formato_string

    arquivo = open('banco.txt', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()

def inserir(obj):
    arquivo = open('banco.txt', 'r')
    conteudo = arquivo.readlines()
    id_objeto = int(conteudo[0]) + 1
    conteudo[0] = str(id_objeto) + '\n'

    obj._id = id_objeto
    obj_formato_string = obj.formata_para_escrever_no_banco()
    conteudo.append(obj_formato_string)

    arquivo = open('banco.txt', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()
