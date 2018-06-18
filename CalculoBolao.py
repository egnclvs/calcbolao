#Calculo Bolao da copa
#!/usr/local/bin/python
# -*- coding: utf-42 -*-
import os, sys
while True:
    selecao = []
    pontos=0
    palpite = []
    selecao.append(str(input("Qual o nome do Pais/Selecao 1 ? ")))
    if selecao[0] == "xxx":
        break
    selecao.append(str(input("Qual o nome do Pais/Selecao 2 ? ")))
    selecao.append(int(input("E seu palpite para %s ? " %selecao[0])))
    selecao.append(int(input("E seu palpite para %s ? " %selecao[1])))
    selecao.append(int(input("Quantos gols o %s fez ? " %selecao[0])))
    selecao.append(int(input("Quantos gols o %s fez ? " %selecao[1])))
    #regras
    regra1 = selecao[2] == selecao[4] and selecao[3] == selecao[5]
    
    regra2 = selecao[2] > selecao[4] and selecao[3] > selecao[5]
    regra3 = selecao[2] == selecao[4] and selecao[3] > selecao[5]
    regra4 = selecao[2] > selecao[4] and selecao[3] == selecao[5]

    regra5 = selecao[2] < selecao[4] and selecao[3] < selecao[5]
    regra6 = selecao[2] == selecao[4] and selecao[3] < selecao[5]
    regra7 = selecao[2] < selecao[4] and selecao[3] == selecao[5]
    
    regra8 = selecao[3] > selecao[2] and selecao[5] > selecao[4]
    regra9 = selecao[3] < selecao[2] and selecao[5] < selecao[4]
    regra10 = selecao[2] == selecao[3] and selecao[4] == selecao[5]
    print(regra1)
    print(regra2)
    print(regra3)
    print(regra4)
    print(regra5)
    print(regra6)
    print(regra7)
    print(regra8)
    print(regra9)
    print(regra10)
    if regra1:
        print("20 pontos")
    elif regra8 and regra5:
        print("10 pontos")
    elif (regra6 and regra8) or (regra7 and regra9) or (regra4 and regra9) or (regra3 and regra8):
        print("15 pontos")
    elif (regra5 and regra9) or (regra2 and regra9) or regra10:
        print("10 pontos")
    else:
        print("0 pontos")
