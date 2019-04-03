import socket, network, time, json


class WiFi:

    @staticmethod
    def connect_wifi(ssid, passwd):
        ap = network.WLAN(network.AP_IF)
        ap.active(False)
        sta = network.WLAN(network.STA_IF)
        sta.active(True)
        sta.connect(ssid, passwd)
        time.sleep(1)
        return sta.isconnected()

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
        Info = {}
        Info['IP'] = WiFi.get_local_ip()
        Info['UUID'] = WiFi.get_mac()
        Info['PORT'] = [0, 2, 12, 14]
        jsonStr = json.dumps(Info)
        s = socket.socket()
        s.connect(address)
        msg = '''POST /esp_node_register HTTP/1.1
        Content-Length: ''' + str(3+len(jsonStr)) + '''
        Content-Type: application/x-www-form-urlencoded

        info=''' + jsonStr
        s.send(bytes(msg, 'utf-8'))
        data = s.recv(1024)
        print(data)