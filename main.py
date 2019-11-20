import machine
import urequests as r
from network import WLAN
wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()
for net in nets:
    if net.ssid == '<Your ssid>':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, '<Your wifi password>'), timeout=5000)
        while not wlan.isconnected():
            machine.idle() 
        print('WLAN connection succeeded!')
        break

res = r.get('https://testscaccess.servicechannel.com')
print(res.text)

