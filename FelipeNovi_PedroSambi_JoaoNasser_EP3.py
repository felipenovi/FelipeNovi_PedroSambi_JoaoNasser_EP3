# -*- coding: utf-8 -*-

#pedindo dados do usuario

#abrindo arquivo usuario, lendo linha 1, lendo linha 2, limpando e separando informacoes de usuario
entrada_usuario = open("usuario.csv","r")
entrada_usuario.readline()
entrada_informacoes = entrada_usuario.readline()
entrada_informacoes = entrada_informacoes.strip()
info = entrada_informacoes.split(",")


nome = info[0]
sexo = info[3]
idade = float(info[1])
altura = float(info[4])
peso = float(info[2])
atividade = info[5]


IMC = peso/(altura**2)
if IMC < 17:
	imc_usuario = "Você está muito abaixo do peso"
elif IMC > 17 and IMC < 18.49:
	imc_usuario = "Você está abaixo do peso"
elif IMC >=18.5 and IMC < 24.99:
	imc_usuario = "Você está no seu peso normal"
elif IMC >25 and IMC <29.99:
	imc_usuario = "Você está acima do peso"
elif IMC >30 and IMC< 34.99:
	imc_usuario = "Você está no nivel de obesidade 1"
elif IMC >35 and IMC <39.99:
	imc_usuario = "Você está no nivel de obesidade 2"
elif IMC>40:
	imc_usuario = "Você está no nível de obesidade morbida"
print(imc_usuario)
arquivo_txt = open("newfile.txt","w")
arquivo_txt.write("O seu Indice de massa corporea é %s \n"%IMC)
arquivo_txt.write("voce esta %s \n"%imc_usuario)


if atividade == ("minimo"):
    info[5] = 1.2
elif atividade == ("baixo"):
    info[5] = 1.375
elif atividade == ("medio"):
    info[5] = 1.55
elif atividade == ("alto"):
    info[5] = 1.725
elif atividade == ("muito alto"):
    info[5] = 1.9
#Fórmula consumo de caloria ideal
if sexo == "m" or sexo == "M":
    TMB = (88.362 + (13.397 * float(peso)) + (4.799 * float(altura)) - (5.677 * float(idade))) * float(info[5])
elif sexo == "f" or sexo == "F":  
    TMB = (447.593 + (9.247 * float(peso)) + (3.098 * float(altura)) - (4.330 * float(idade))) * float(info[5]) 	
print(TMB)


diario = {}
entrada_usuario.readline()
linhasdiario = entrada_usuario.readlines() 
a = []
for i in linhasdiario:
    a.append(i.strip())
for i in range(len(a)):
    a[i] = a[i].split(',')
    a[i][2] = float(a[i][2])
print("a ", a)


alimento = {}   
entrada_alimentos = open("alimentos.csv","r+")
linhas = entrada_alimentos.readlines()
linhas_limpas = []                            
for i in linhas:
    linhas_limpas.append(i.strip())
for l in linhas_limpas[1:]:                        
    info2 = l.split(',')
    alimento[info2[0]] = list()                                      #Alimento      
    alimento[info2[0]].append(float(info2[1]))                       #Quantidade
    alimento[info2[0]].append(float(info2[2])/float(info2[1]))       #Calorias
    alimento[info2[0]].append((float(info2[3])/float(info2[1])))     #Proteínas
    alimento[info2[0]].append((float(info2[4])/float(info2[1])))     #Carboidratos
    alimento[info2[0]].append((float(info2[5])/float(info2[1])))     #Gorduras


dic_calorias = {}
dic_proteinas = {}
dic_carbos = {}
dic_gorduras = {}


datas = []    
for i in range(len(a)):
    datas.append(a[i][0])
for i in range(len(a)):
    if a[i][1] in alimento.keys():
        calorias = (alimento[a[i][1]][1])
        proteinas = (alimento[a[i][1]][2])
        carbos = (alimento[a[i][1]][3])
        gorduras = (alimento[a[i][1]][4])
        calorias_totais = a[i][2]*calorias
        proteinas_totais = a[i][2]*proteinas
        carbos_totais = a[i][2]*carbos
        gorduras_totais = a[i][2]*gorduras
        
        
        if a[i][0] in dic_calorias:
            dic_calorias[a[i][0]] += calorias_totais
        else:
            dic_calorias[a[i][0]] = calorias_totais
            
        if a[i][0] in dic_proteinas:
            dic_proteinas[a[i][0]] += proteinas_totais
        else:
            dic_proteinas[a[i][0]] = proteinas_totais
            
        if a[i][0] in dic_carbos:
            dic_carbos[a[i][0]] += carbos_totais
        else:
            dic_carbos[a[i][0]] = carbos_totais
            
        if a[i][0] in dic_gorduras:
            dic_gorduras[a[i][0]] += gorduras_totais
        else:
            dic_gorduras[a[i][0]] = gorduras_totais
            
 
                
print("datas ", datas)

print("calorias por dia", dic_calorias,"kcal")
print("porteinas por dia", dic_proteinas,"g")
print("carboidratos por dia", dic_carbos,"g")
print("gorduras por dia", dic_gorduras, "g")      
        