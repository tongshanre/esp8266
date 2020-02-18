# -*- coding:utf-8 -*-
import socket, network, time, json
from machine import Pin

class WiFi:

    @staticmethod
    def connect_wifi(ssid, passwd):
        ap = network.WLAN(network.AP_IF)
        ap.active(False)
        sta = network.WLAN(network.STA_IF)
        sta.active(True)
        sta.connect(ssid, passwd)
        time.sleep(1)
        while True:
            if sta.isconnected():
                break
        return True

    @staticmethod
    def get_local_ip():
        sta = network.WLAN(network.STA_IF)
        return sta.ifconfig()[0]

    @staticmethod
    def get_mac():
        sta = network.WLAN(network.STA_IF)
        s = sta.config('mac')
        mac = ('%02x-%02x-%02x-%02x-%02x-%02x') %(s[0],s[1],s[2],s[3],s[4],s[5])
        return mac


class Init:

    @staticmethod
    def regist(address):
        led = Pin(2, Pin.OUT)
        WiFi.connect_wifi('HUAWEI-LJ4UPM', 'tongshanre123')
        Info = {}
        Info['IP'] = WiFi.get_local_ip()
        Info['UUID'] = WiFi.get_mac()
        Info['PORT'] = [2, 4, 5, 12, 14]
        jsonStr = json.dumps(Info)
        led.off()
        while True:
            try:
                s = socket.socket()
                s.connect(address)
                s.settimeout(200)
                msg = '''POST /esp_node_register HTTP/1.1\r\nContent-Length: '''+str(len(jsonStr)+5)+'''\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\ninfo='''+jsonStr
                s.send(bytes(msg, 'utf-8'))
                data = s.recv(1024)
                if str(data).find('200'):
                    break;
            except Exception as e:
                pass
            time.sleep(3)
        led.on()
