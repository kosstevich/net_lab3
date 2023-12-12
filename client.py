from socket import *

def udp_client(ip:str = "127.0.0.1", port:int = 5000):
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    try:
        while True:
            data = input('Enter message: ')
            udp_socket.sendto(str.encode(data), (ip, port))
            input_data, addr = udp_socket.recvfrom(1024)
            print(input_data.decode("utf-8"))

    except:
        udp_socket.close()
        print("Error! Server stopped!")

def tcp_client(ip:str = "127.0.0.1", port:int = 5000):
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.connect((ip,port))
    try:
        while True:
            data = input('Enter message: ')
            tcp_socket.send(data.encode("utf-8"))
            input_data = tcp_socket.recv(1024)
            print(input_data.decode("utf-8"))
    except:
        tcp_socket.close()
        print("Error! Server stopped!")
    
if __name__ == "__main__":
    try:
        #udp_client("10.1.6.120")
        #tcp_client()
        #udp_client()
        tcp_client("10.1.6.120")
    except:
        print("Error! Server stopped!")