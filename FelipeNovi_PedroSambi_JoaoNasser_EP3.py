# -*- coding: utf-8 -*-

#pedindo dados do usuario
nome = str(input("digite seu nome"))
sexo = str(input("digite o seu sexo (F ou M)"))
idade = int(input("digite a sua idade"))
altura = int(input("digite sua altura em centimetros"))
peso = int(input("digite o seu peso"))
atividade = str(input("qual é o seu fator de atividade fisica?( 1 para minimo/ 2 para baixo/ 3 para medio/ 4 para alto/ 5 muito alto"))



if sexo == "m":
	HBh = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
	print(HBh)
elif sexo == "f":
	HBm = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)	
	print(HBm)


