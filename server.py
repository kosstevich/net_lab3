from socket import *

def tcp_server(ip:str = "127.0.0.1", port:int = 5000):
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.bind((ip,port))
    print("Server running")
    try:  
        pass
    except:
        tcp_socket.close()
        print("Error! Server stopped!")
        print("Error log:")
        print(e)


def udp_server(ip:str = "127.0.0.1", port:int = 5000):
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind((ip,port))
    print("Server running")
    try:  
        while True:
            data, addr = udp_socket.recvfrom(1024)
            print('Client addr: ', addr)
            print('Client data: ', data)
            udp_socket.sendto(data, addr)
    except Exception as e:
        udp_socket.close()
        print("Error! Server stopped!")
        print("Error log:")
        print(e)

if __name__ == "__main__":
    try:
        udp_server("10.1.6.120")
    except Exception as e:
        udp_socket.close()
        print("Error! Server stopped!")
    

