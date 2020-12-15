import json,requests,socket
import scapy.all as scapy
import uuid 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip= s.getsockname()[0]
s.close()
text = requests.get("https://ipinfo.io/")
data = json.loads(text.text)
target = "192.168.1.0/24"
arp = scapy.ARP(pdst=target)
ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp
sonuc = scapy.srp(packet, timeout=4, verbose=0)[0]


istemciler = []

for sent, received in sonuc:
    istemciler.append({'ip': received.psrc, 'mac': received.hwsrc})

print("İP","\t\tMAC")
print("------------------------")
for client in istemciler:
    print(client["ip"],client["mac"])
print("--------------------------")
print("My private ip:",data['ip'])
print ("My mac: ", end="") 
print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
for ele in range(0,8*6,8)][::-1])) 
print("My local ip:",local_ip)
