

#Noob Editors
#Posy you mother Editor
from colorama import init, Fore
init()
from random import choice, randint
print("     AMI-NOT")
print(Fore.RED+'                   ●○●○●○●○●○●○●○●○●○●○●○●')
print(Fore.RED+'                   ○                     ●')
print(Fore.RED+'                   ●                     ○')
print(Fore.RED+'                   ○                     ●')
print(Fore.RED+'                   ●                     ○')
print(Fore.GREEN+'                   》      AMI-NOT      《')
print(Fore.RED+'                   ○                     ●')
print(Fore.RED+'                   ●                     ○')
print(Fore.RED+'                   ○                     ●')
print(Fore.RED+'                   ●○●○●○●○●○●○●○●○●○●○●○●')
print(Fore.CYAN+'■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
print(Fore.RED+'         telegram : Mr_AMI_NOT ')
print(Fore.GREEN+'         instagram : me_AMI.NOT')
print(Fore.RED+'         GITHUB : https://github.com/AMI-NOT')
print(Fore.CYAN+'■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
import socket
print("                                                                  ")
domain = input("     yuore target : ").lower()

domain = domain.replace("http://","")
domain = domain.replace("https://","")
domain = domain.replace("www.","")

if domain[-3:] == "org" or domain[-3:] == "com" or domain[-3:] == "net":
    whois_server = "whois.internic.net"
else:
    whois_server =  "whois.iana.org"

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.connect((whois_server,43))

s.send((domain+"\r\n").encode())

msg = s.recv(10000)

print(msg.decode())