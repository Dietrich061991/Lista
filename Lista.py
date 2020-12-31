# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 02:36:11 2020

@author: Dietrich
@careers: specialist in machine learning
@linkedin : https://www.linkedin.com/in/dietrich-montcho-b13672121/

"""

##################################################################################################################################################################
# criando uma lista de frutas
lista_frutas1 = ['laranja', 'Abacaxi', 'manga', 'açai', 'guarrana', 'maça', 'banana', 'Uva', 'Morango', 'limão']
print(lista_frutas1) # imprimir a lista 

##################################################################################################################################################################
# imprimir a lista de forma horizontal (como uma string)
lista_frutas1_str = ', '.join(lista_frutas1)  # podemos substituir o ', ' por ' - ' se quisemos. o separador pode ser qualquer 
print(lista_frutas1_str)

##################################################################################################################################################################
# imprimir a lista de forma vertical 
for frutas in lista_frutas1:  # para cada frutas em lista_frutas1 retorne frutas
    print(frutas)

##################################################################################################################################################################
#contanto o quantidade de item na lista_frutas1
print(len(lista_frutas1))

                                
                                #                             FAZENDO FILTRAGEM                                #
                                
                                

##################################################################################################################################################################
#imprimir o primeiro elemento da lista (para printar um elemento da lista basta passar a posição do elemento lembrando que o primeiro elemento da lista é sempre  0)
'''
1er Metodo
'''
print(lista_frutas1[0])

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#imprimir o primeiro elemento da lista
'''
2nd Metodo
'''
print(lista_frutas1[-10])

##################################################################################################################################################################
#imprimir os dois primeiros elemento da lista
'''
1er Metodo
'''
print(lista_frutas1[0:2])

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#imprimir os dois primeiros elemento da lista
'''
1er Metodo
'''
print(lista_frutas1[:2])

##################################################################################################################################################################
#imprimir os elementos da lista a partir segundo elemento da lista
print(lista_frutas1[2:])

##################################################################################################################################################################
#imprimir os dois ultimos elementos da lista
print(lista_frutas1[-2:])

##################################################################################################################################################################
#selecionando a partir do 2 elemento ate o quarto elemento da lista
print(lista_frutas1[2:4])

##################################################################################################################################################################
#index de um elemento em uma lista (posição do elemento)
print(lista_frutas1.index('banana'))

##################################################################################################################################################################
#index os elementos da lista  mais o posição de cada um deles
for index, frutas in enumerate(lista_frutas1):  
    print(index, frutas)

##################################################################################################################################################################
#vamos suppor que a nossa lista retorna os elementos e o index sem querer que o primeiro elemento tenha como index 1 e não 0
for index, frutas in enumerate(lista_frutas1, start=1):  
    print(index, frutas)

##################################################################################################################################################################
#verificando se um elemento está na lista (retorna 'True' se for verdade ou 'False' se não verdade)
print('banana' in lista_frutas1) 



                                #                             MANIPULANDO UMA LISTE                                #


##################################################################################################################################################################
#Acrescentando mais uma fruta na lista 
lista_frutas1.append('Graviola')
print(lista_frutas1)

##################################################################################################################################################################
#colocando mais uma fruta na posição 4 na lista (lembrando que a primeira posição na lista é 0)
lista_frutas1.insert(3,'ciriguela')
print(lista_frutas1)

##################################################################################################################################################################
#Vamos criar uma segunda lista chamada lista_frutas2 
lista_frutas2 = ['Abacate', 'Mamão', 'Acerola', 'Ameixa', 'Cacau', 'Cereja', 'Goiaba', 'Jaca', 'Jujuba', 'Kiwi']
print(lista_frutas2)

##################################################################################################################################################################
#inserindo a lista_frutas2 na posição 2 dentro da lista_frutas1 (inserir uma lista dentro de outra lista ) 0 é a primeira posição
lista_frutas1.insert(1,lista_frutas2)
print(lista_frutas1)

#################################################################################################################################################################
#Vamos criar uma terceira lista chamada lista_frutas3 e uma quarta lista chamada lista_fruta4. vamos completar as frutas da terceira com as da quarta.
lista_frutas3 = ['Tangerina', 'Laranja-de-pacu', 'Karité']
lista_frutas4 = ['Longan', 'Langsat', 'Mangaba']
lista_frutas3.extend(lista_frutas4)
print(lista_frutas3)

#################################################################################################################################################################
#Vamos criar uma terceira lista chamada lista_frutas5 e uma quarta lista chamada lista_fruta6. append é utilizado para incluir apenas 1 item por vez
lista_frutas5 = ['Mabolo', 'Mamey', 'Marang']
lista_frutas6 = ['Mirtilo', 'Murici']
lista_frutas5.append(lista_frutas6)
print(lista_frutas3)

#################################################################################################################################################################
#Vamos usar o metodo pop() serve para Remove elemento da lista através do índice
lista_frutas5 = ['Mabolo', 'Mamey', 'Marang']
lista_frutas5.pop()  # remove o utimo elemento da lista 
print(lista_frutas5)

pop_lista = lista_frutas5.pop()  # retorna o utimo elemento da lista (para que isso funciona precisa criara uma variavel para armazenar) vamos criar uma variavel chamada pop_lista
print(pop_lista)

#################################################################################################################################################################
#criando uma lista chamada lista_frutas7
lista_frutas7 = ['Massala', 'Murici', 'Naranjilla']
lista_frutas7.reverse()  #revertendo os elementos da lista 
print(lista_frutas7)

#################################################################################################################################################################
#criando uma lista chamada lista_frutas8
lista_frutas8 = ['Kiwano', 'Jamelão', 'Juá']
lista_frutas8.sort() #Em sort você altera a lista em si
print(lista_frutas8)

#criando uma lista chamada lista_frutas8
lista_frutas9 = ['Jamelão', 'Murici', 'Juá']
sorted_lista9 = sorted(lista_frutas9) #Em sorted você altera a lista em si mas armazenando em uma variavel 
print(sorted_lista9)



                                #                             MANIPULANDO UMA LISTE DE VALORES                                #

#################################################################################################################################################################
numero_lista = [ 23 , 12, 23, 56, 457, 123, 90, 2, 24]
print(numero_lista) # imprimir a lista numero_lista
print(min(numero_lista)) #retornando o valor minimo da lista
print(max(numero_lista)) #retornando o valor maximo da lista
print(sum(numero_lista)) #retornando a soma dos numeros da lista


                               #                             TRABALHANDO COM SETS                                #

#################################################################################################################################################################

# criando uma lista como dicionario
lista_frutas10 = {'Abiu', 'Akee', 'Amora', 'Ata', 'Bacuri'} # aqui temos valores unicos na lista 
print(lista_frutas10)

lista_frutas11 = {'Abiu', 'Bacuri', 'Cereja', 'Cajá', 'Cajá', 'Cereja'} # aqui temos valores duplicados como 'Cajá', 'Cereja' 
print(lista_frutas11) # vai retornar os valores sem duplicar 

#interceção entre listas 
print(lista_frutas10.intersection(lista_frutas11)) # retorno os elementos identicos entre as duas listas

#interceção entre listas 
print(lista_frutas10.difference(lista_frutas11)) # retorno a diferença entre as duas listas

#interceção entre listas 
print(lista_frutas10.union(lista_frutas11)) # unir as duas listas sem duplicar elementos

