# -*- coding: cp1252 -*-
from typing import List
import os
import glob
import re

#Leitura do arquivo de Entrada
home = os.path.expanduser('~')
caminhoEntrada = os.path.join(home, 'data\in')
os.chdir(caminhoEntrada)
for procura in glob.glob("*.dat"):
    arquivoEntrada = procura
lerArquivo = open(arquivoEntrada, 'r')

#Listas utilizadas
listaVendedor = list()
listaCliente = list()
listaVendedorDaVenda = list()
listaNomeVendedorPorVenda = list()
listaItemVenda = list()
listaIdVendedoresDaVenda = list()

#Lendo o arquivo
for linha in lerArquivo:

    #Limitador de linhas
    colunasLinhas = linha.split('c')

    #Montagem de lista de Vendedores
    if float(colunasLinhas[0]) == 1:
        listaVendedor.append(float(colunasLinhas[0]))

    #Montagem de Lista de Cliente
    elif float(colunasLinhas[0]) == 2:
        listaCliente.append(float(colunasLinhas[0]))

    #Montagem de Lista de Vendas
    elif float(colunasLinhas[0]) == 3:

        listaIdVendedoresDaVenda.append(int(colunasLinhas[1]))
        listaItemVenda.append(str(colunasLinhas[2]))

        #Nome dos vendedores e quantidade de venda listaVendedorDaVenda
        listaVendedorDaVenda.append(str(colunasLinhas[3]))

        listaNomeVendedorPorVenda.append({

            x:listaVendedorDaVenda.count(x)

            for x in set(listaVendedorDaVenda)

        })

#Vendedor que menos vendeu
indice = len(listaNomeVendedorPorVenda)-1
ultimo: dict = listaNomeVendedorPorVenda[indice]


#Impressões a serem gravadas no arquivo de saída
imprimirTotalDeVendedores = len(listaVendedor)
imprimirTotalDeClientes = len(listaCliente)
imprimirTotalDeVendas = len(listaVendedorDaVenda)
imprimirVendasPorVendedor = ultimo
imprimirVendedorMenosVendeu = min(ultimo)
imprimirVendas = listaItemVenda
imprimirIdVendas = listaIdVendedoresDaVenda


#Saída via arquivo
home = os.path.expanduser('~')
caminhoSaida = os.path.join(home, 'data\out')
os.chdir(caminhoSaida)

#Gravando no arquivo de saída
arquivo = open('home-data-out.dat', 'w')
arquivo.write('Abaixo os resultados gerados pela arquivo de entrada: ')
arquivo.write('\n\nTotal de Vendedores: {}'.format(str(imprimirTotalDeVendedores)))
arquivo.write('\nTotal de Cliente: {}'.format(str(imprimirTotalDeClientes)))
arquivo.write('\nTotal de Vendas: {}'.format(str(imprimirTotalDeVendas)))
arquivo.write('\nVendas Por Vendedor: {}'.format(str(imprimirVendasPorVendedor)))
arquivo.write('\nVendedor que Menos Vendeu: {}'.format(str(imprimirVendedorMenosVendeu)))
arquivo.write('\nListas de Vendas: {}'.format(str(imprimirVendas)))
arquivo.write('\n\nListas de IDs Vendas: {}'.format(str(listaIdVendedoresDaVenda)))