from socket import *

def udp_client(ip:str = "127.0.0.1", port:int = 5000):
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    try:
        while True:
            data = input('Enter message: ')
            udp_socket.sendto(str.encode(data), (ip, port))
            input_data = udp_socket.recvfrom(1024)

    except Exception as e:
        udp_socket.close()
        print("Error! Server stopped!")
        print("Error log:")
        print(e)

def tcp_client(ip:str = "127.0.0.1", port:int = 5000):
    pass

if __name__ == "__main__":
    try:
        udp_client("10.1.6.120")
    except Exception as e:
        udp_socket.close()
        print("Error! Server stopped!")