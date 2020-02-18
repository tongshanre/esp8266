import network
from umqtt.simple import MQTTClient
from machine import Pin
import time
p = Pin(2, Pin.OUT)
p.off()

def msg_solve(topic, msg):
   print(topic,msg)
   p.off()
   time.sleep(1)
   p.on()




network.WLAN(network.AP_IF).active(False)
wlan = network.WLAN(network.STA_IF)
act = wlan.active(True)
print('active: '+str(act))
wlan.scan()
isconn = wlan.isconnected()
print('isconnected: '+ str(isconn))
conn = wlan.connect('HUAWEI-LJ4UPM', 'tongshanre123')
print('conn:' + str(conn))
print(wlan.ifconfig())
time.sleep(3)
c = MQTTClient('umqtt_client', '192.168.3.21', 1883, '', '')
c.set_callback(msg_solve)
flag = c.connect()
print(flag)
c.subscribe('test')
p.on()
while 1:
   c.check_msg()
   print(1)