#!/usr/bin/python
# coding=UTF-8

### Esse programa monitorará a rede CAN, mostrando todas as mensagens recebidas.
### Também verificará se a mensagem possuem um id conhecido ou não


#Importando bibliotecas

import can #Biblioteca do python-can


#Definir qual controlador vamos usar

bus = can.interface.Bus(channel='can0', bustype='socketcan_ctypes') #Selecionamos o can0 como o controlador que monitorará as mensagens

#Definindo um id conhecido

id = 0x123

#Main
while True:
    
    message = bus.recv() ##Fica esperando receber mensagem no barramento CAN
    
    print("Recebemos uma mensagem")
    if message.arbitration_id == id:  #verifica se o id da mensagem é o mesmo que o id definido
        print("A mensagem possui um id conhecido!")
    else:
        print("A mensagem possui um id desconhecido!")
    
    #O loop a seguir irá formatar o conteudo do vetor para que possa ser apresentado na tela da forma de hexadecimal
    s=[]
    for i in range(len(message.data)): #loop que percorrerá todo o vetor message.data
        s.append(hex(message.data[i])) Convertendo o valor em hexadecimal e adicionando ao fim do vetor s
    print s