import paho.mqtt.client as mqtt
import time


client = mqtt.Client()
client.on_connect = lambda clientp, userdata, flags, rc: print('连上了,code:'+str(rc))
client.on_disconnect = lambda: print('关闭连接了')
client.on_message = lambda clientp, userdata, msg: print('收到了消息：topic:'+ msg.topic + '\tpayload:'+str(msg.payload))
client.on_subscribe = lambda: print('订阅了')

client.connect('192.168.3.21', 1883, 60)

client.subscribe('test', 0)
client.loop_forever()
# client.publish('test', payload='hello world')
# client.publish("temperature", payload="24.0")
# client.publish("humidity", payload="65%")
time.sleep(5)
client.disconnect()