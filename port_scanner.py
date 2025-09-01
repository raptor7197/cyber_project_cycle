# ports are like a virtual usb port which are used to connect to oterh to the internt or other devices 

import socket


# a simple tcp port scanner.
# this script checks the status of a predefined list of tcp ports on a specific
# target host. it iterates through each port, attempts to establish a connection,
# and reports whether the port is open or closed.
# attributes:
    # target (str): the hostname or ip address to be scanned.
    # ports (list): a list of integer ports to check on the target.

# if a port is closed you cannot access information through it its like a closed door while an open port is like an open door you can access information through it


target = "scanme.nmap.org" #change the url to any other websites [DO NOT SCAN VIT WEBSITES!!!] 
ports = [22, 80, 443]
# 22 is for ssh 443 is for https 80 is for http remember th numbers

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is for ipv4 ip addresses and SOCK_STREAM is for tcp connections
    
    try:
        s.connect((target, port)) # connect to the port 
        print(f"Port {port} is OPEN on {target}")
    except socket.error:
        print(f"Port {port} is CLOSED on {target}")
    finally:
        s.close() # close the connection after talking to it not needed but nice practice


from IPy import IP
# IPy is used to check and analyse IP addresses.
# single ip
ip = IP("192.168.1.10")
print("IP:", ip)
print("Version:", ip.version())
print("Reverse DNS name:", ip.reverseNames()[0])

# ip range (CIDR block)
network = IP("192.168.1.0/28") #scans all the networks from port 0-28 
print("\nNetwork size:", network.len()) #the size is the number of open ports in it 
print("All IPs in network:")
for addr in network:
    print(addr)
