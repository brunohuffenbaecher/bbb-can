#!/usr/bin/python
# coding=UTF-8

### Esse programa enviará periodicamente uma mensagem para a rede can

#Importando bibliotecas

import can
import time

#Definir qual controlador vamos usar

bus = can.interface.Bus(channel='can1', bustype='socketcan_ctypes') #Selecionamos o can0 como o controlador que monitorará as mensagens

#Definindo um id para nossas mensagens

id = 0x123

#Definindo o conteudo das mensagens
cont = [0xf5,0x23,0x1A]

#Main

while True:
    
    msg = can.Message(arbitration_id = id,data=cont)  #Criando a mensagem que será enviada na rede
    bus.send(msg) #Enviado para a rede
    print "Mensagem enviada"
    time.sleep(5) #espera 5 segundos antes de enviar a mesma mensagem