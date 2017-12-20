# Joshua Hinojoas
# 12/20/17
# Mr. Davis
#IP Port Scanner
#v1.0
''' This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.'''
import socket, time, sys
from threading import Thread

def checkportofip(): #checks ports 20,22,80 of ip addresses between 172.17.2.100 to 172.17.2.254
    global portslist, iplist,openportlist
    iplist=[]
    openportlist = []
    ipfront="172.17.2."
    endnum=99
    for i in range(155):
        endnum+=1
        i=str(endnum)
        i=ipfront+i
        iplist.append(i)
    for port in portslist:
        thread = Thread(target=scanner, args=(port,))
        thread.start()
def scanner(port):
    global iplist, openportlist
    for i in iplist:
        ip=i
        print("Checking Ports: 20,22,80 of IP: " + ip + "...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            #if a socket is listening it will print out the port number\
            data=(ip + " " + "Port {}: \t Open".format(port))
            print(data)
            openportlist.append(data)
            sock.close()
    with open('openports.txt', 'a') as f:
        for i in openportlist:
            f.write(i+'\n')
    f.close()
    print("DONE")
def menu(): #main function that lists user choices of port scanner
    global portslist
    portslist=[20,22,80] #list of most common ports
    print("-------------PORT SCANNER---------------")
    print("1. Scan Ports 20,22,80 of IP addresses between 172.17.2.100 to 172.17.2.254")
    print("2. Quit")
    print("What do you want to do?")
    u = input()
    if u == '1':
        checkportofip()
    elif u == '2':
        quit()
    else:
        print("Invalid Choice!")
        menu()
menu()