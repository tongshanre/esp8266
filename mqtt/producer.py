import paho.mqtt.client as mqtt
import time


client = mqtt.Client()
client.on_connect = lambda clientp, userdata, flags, rc: print('连上了,code:'+str(rc))
client.on_disconnect = lambda: print('关闭连接了')
client.on_message = lambda clientp, userdata, msg: print('收到了消息：topic:'+ msg.topic + '\tpayload:'+str(msg.payload))
client.on_subscribe = lambda: print('订阅了')

client.connect('127.0.0.1', 1883, 60)

# client.publish('test', payload='hello world')
# client.publish("temperature", payload="24.0")
client.publish("test", payload="65%", qos=1)
client.disconnect()