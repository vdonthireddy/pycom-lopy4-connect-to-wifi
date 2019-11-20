import machine
import urequests as r
from network import WLAN
wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()
for net in nets:
    if net.ssid == 'ServiceChannel-Guest':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, 'scfacility81'), timeout=5000)
        while not wlan.isconnected():
            machine.idle() 
        print('WLAN connection succeeded!')
        break

res = r.get('https://testscaccess.servicechannel.com')
print(res.text)

