#-*- coding:utf-8 -*-
import socket, json
from base import MSG,GPIO_Client

print(GPIO_Client.sendData(('192.168.3.205', 8266), 2,1))

#print(GPIO_Client.sendHeart(('192.168.3.205', 8266)))
