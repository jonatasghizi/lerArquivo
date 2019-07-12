# lerArquivo

Programa desenvolvido em python, utilizando a IDE Pycharm.

Rebemos arquivo .dat no repositório %homepath%data/in e o resultado é enviado para ao repositório %homepath%data/out.

Os dados recebidos possuem 3 categorias, Vendedores com ID (001), Clientes com ID (002) e Vendas com ID (003), as separação das informações são via a letra c, recebemos um arquivo inicial como exemplo abaixo:

001c1234567891234cPedroc50000
001c3245678865434cPauloc40000.99              < Vendedores
001c3245678865434cJoaoc40000.99
002c2345675434544345cJose da SilvacRural
002c2345675433444345cEduardo PereiracRural    < Clientes
002c2345675433444345cEduardo PereiracRural
003c01c[1-34-10,2-33-1.50,3-40-0.10]cPedro
003c02c[1-34-10,2-33-1.50,3-40-0.10]cPedro    < Vendas 
003c03c[1-34-10,2-33-1.50,3-40-0.20]cJoao

Temos as informações da vendas sendo as virgulas os separadores dos itens da venda sendo compostos por:
Categoria,IdVenda[ID-Produto-Quantidade-Valor],Vendedor.

Análise:
  As vendas são integradas pela sua categora 003 - Venda Exemplo: 003c01c[1-34-10,2-33-1.50,3-40-0.10]cPedro.
  Temos um ID para cada venda, no caso acima é o 01.
  Como exemplo acima o 1 é o ID do produto, 34 é a quantidade e 10 é o valor.
  Temos o Pedro como vendedor.
  
 Teremos no arquivo de saída:
 
● Quantidade de clientes no arquivo de entrada
● Quantidade de vendedor no arquivo de entrada
● O pior vendedor
● Lista de vendas
● IDs das vendas

Será necessário implementar o ID da venda mais cara
