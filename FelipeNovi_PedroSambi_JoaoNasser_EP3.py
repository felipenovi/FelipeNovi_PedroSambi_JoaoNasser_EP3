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


IMC = peso/(altura**2)
if IMC < 17:
	imc_usuario = "muito abaixo do peso"
elif IMC > 17 and IMC < 18.49:
	imc_usuario = "abaixo do peso"
elif IMC >=18.5 and IMC < 24.99:
	imc_usuario = " no seu peso normal"
elif IMC >25 and IMC <29.99:
	imc_usuario = "acima do peso"
elif IMC >30 and IMC< 34.99:
	imc_usuario = "no nivel de obesidade 1"
elif IMC >35 and IMC <39.99:
	imc_usuario = "no nivel de obesidade 2"
elif IMC>40:
	imc_usuario = "no nível de obesidade morbida"
print(imc_usuario)


arquivo_txt = open("newfile.txt","w")
arquivo_txt.write("O seu Indice de massa corporea é %s \n"%IMC)
arquivo_txt.write("voce esta %s \n"%imc_usuario)


"""
formula consumo de caloria ideal
if sexo == "m" or sexo =="M":
	HBh = (88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)) * atividade
	
elif sexo == "f" or sexo == "F":
	HBm = (447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)) * atividade	
"""	


diario = {}
entrada_usuario.readline()
linhasdiario = entrada_usuario.readlines() 
for line in linhasdiario:
    print(line)
    