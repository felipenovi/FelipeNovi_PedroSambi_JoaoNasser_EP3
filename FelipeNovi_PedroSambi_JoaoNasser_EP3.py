# -*- coding: utf-8 -*-

#pedindo dados do usuario

#abrindo arquivo usuario, lendo linha 1, lendo linha 2, limpando e separando informacoes de usuario
entrada_usuario = open("usuario.csv","r")
entrada_usuario.readline()
entrada_informacoes = entrada_usuario.readline()
entrada_informacoes.strip()
informacoes = entrada_informacoes.split(',')


nome = informacoes[0]
sexo = informacoes[3]
idade = int(informacoes[1])
altura = float(informacoes[4])
peso = float(informacoes[2])
atividade = informacoes[5]


if sexo == "m" or sexo =="M":
	HBh = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
	print(HBh)
elif sexo == "f" or sexo == "F":
	HBm = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)	
	print(HBm)


