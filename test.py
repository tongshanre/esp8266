# -*- coding:utf-8 -*-
import socket, time
from machine import Pin
from base import MSG
from init import Init


address = ('192.168.3.76', 5000)

def blink(times):
    led = Pin(2, Pin.OUT)
    led.on()
    for i in range(times):
        led.off()
        time.sleep_ms(200)
        led.on()
        time.sleep_ms(200)


def msg_trans(msg):  # 消息处理
    if 'CTL' == msg['type']:   # （控制）消息处理
        pass
    elif 'HEART' == msg['type']:    # （心跳）消息处理
        msg = MSG.get_heart_msg()
        msg['response'] = 200
        return msg
    elif 'DATA' == msg['type']:     # （数据）消息处理
        if 1 == msg['code']:
            info = msg['data'].split('-')
            # 执行GPIO控制
            Pin(int(info[0]), Pin.OUT).value(int(info[1]))
            msg['response'] = 200
            return msg
        elif 2 == msg['code']:
            Init.regist(address)
            msg['response'] = 200
            return msg
        else:
            pass
    else:
        print("error msg type:", msg)


def start_engine(port=8266):
    # 1.注册节点
    Init.regist(address)
    blink(1)
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.bind(('0.0.0.0', 8266))
    ss.listen(1)
    blink(2)
    while 1:
        cs, addr = ss.accept()
        try:
            # 1. 接收消息
            buffer = cs.recv(1024)
            rMsg = MSG.str_to_json(str(buffer, 'utf-8'))
            # 2. 处理消息
            msg = msg_trans(rMsg)
            # 3. 发送处理结果
            cs.send(bytes(MSG.json_to_str(msg), 'utf-8'))
        except OSError:
            pass

start_engine()
