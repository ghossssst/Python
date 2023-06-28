import socket

socket.setdefaulttimeout(0.01)
target = input ("TARGET IP: ")
sport = int(input ("START PORT: "))
eport = int(input ("END PORT: "))

def portscan ():
    for port in range (sport, eport + 1):
        try:
            SCAN = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
            result = SCAN.connect_ex((target, port))
            if result == 0:
                print (target,"/",port,"= OPEN")
            SCAN.close()
        except Exception:
            pass

portscan ()
print("Scan Complete")