# esp8266
esp8266服务程序

#控制命令
pip install adafruit-ampy
D:\esp8266>ampy --port=com4 ls

#格式化及安装固件
pip install esptool
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin
