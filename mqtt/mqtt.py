
import network
from umqtt.simple import MQTTClient
from machine import Pin
import time
p = Pin(2, Pin.OUT)
p.off()

wlan = network.WLAN(network.STA_IF)
wlan.connect('HUAWEI-LJ4UPM', 'tongshanre123')
while not wlan.isconnected():
    pass
print('wlan ready')

def msg_solve(topic, msg):
   print(topic,msg)
   p.off()
   time.sleep(1)
   p.on()
try:
    c = MQTTClient('umqtt_client', '192.168.3.21', 1883, '', '')
    c.set_callback(msg_solve)
    flag = c.connect()
    time.sleep(5)
    print('connect:')
    print(flag)
    c.subscribe('test')
except BaseException as exp:
    print(exp)
while 1:
   c.check_msg()
   time.sleep(1)
   print('.')