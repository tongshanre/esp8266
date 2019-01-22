import socket,json
ss  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('0.0.0.0', 8266))
ss.listen(1)
while 1:
    cs, addr = ss.accept()
    print(addr)
    buffer  = cs.recv(1024)
    msg = json.loads(str(buffer, 'utf-8'))
    print('msg:', msg)
    msg['response'] = 200
    cs.send(bytes(json.dumps(msg), 'utf-8'))
    cs.close()


from machine import PWM, Pin
import time
flag = True
pwm = PWM(Pin(2), freq=1000, duty=512)
for i in range(30):
    for j in range(0, 1023):
        duty = j
        if not flag:
            duty = 1023 - j
        pwm.duty(duty)
        time.sleep_ms(2)
    flag = not flag