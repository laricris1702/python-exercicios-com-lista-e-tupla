lista_compras = ["frutas", "pao","carne", "arroz", "iogurte"]
print ( "Hoje vou comprar no mercado:", lista_compras)

#para saber o tipo da minha variavel

print( type(lista_compras))

# saber a quantidade de elementos na minha lista

print("A quantidade de itens para comprar no mercado:",len(lista_compras))

#como excluir um item especifico
lista_compras.append("feijao")
print("minha lista de compras é:", lista_compras)

#como organizar em ordem alfabetica

lista_compras.sort()
print(lista_compras)

#como remover um item pelo nome 
lista_compras.remove("iogurte")
print("Lista sem o elemento removido:", lista_compras)

print("lista saudavel :",lista_compras)

#indicando o terceiro elemento da lista
print("3 elemento da lista:",lista_compras[2])

#mostrando o uiltimo elemento da lista
print(" O ultimo elemento da lista é:",lista_compras[-1])

#mostrando os tres primeiros itens da lista
print("Os tres primeiros elementos sao:", lista_compras[0:3])

#remover o quarto elemento
print( " o 4 elemento removido foi:" ,lista_compras.pop(3))



