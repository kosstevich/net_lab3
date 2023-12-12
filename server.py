from socket import *

def tcp_server(ip:str = "127.0.0.1", port:int = 5000):
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    tcp_socket.bind((ip,port))
    tcp_socket.listen(0)
    print("Server running")
    try:
        while True:
            connection, addr = tcp_socket.accept()
            while True:
                data = connection.recv(1024).decode("utf-8")
                print('Client addr: ', addr)
                print('Client data: ', data)
                output_data = "Response: " + data
                connection.send(output_data.encode("utf-8"))
    except Exception as e:
        connection.close()
        tcp_socket.close()
        print("Error! Server stopped!")


def udp_server(ip:str = "127.0.0.1", port:int = 5000):
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    udp_socket.bind((ip,port))
    print("Server running")
    try:  
        while True:
            data, addr = udp_socket.recvfrom(1024)
            print('Client addr: ', addr)
            print('Client data: ', data.decode("utf-8"))
            output_data = "Response: " + data.decode("utf-8")
            udp_socket.sendto(output_data.encode("utf-8"), addr)

    except:
        udp_socket.close()
        print("Error! Server stopped!")

if __name__ == "__main__":
    try:
        tcp_server("10.1.6.120")
        #tcp_server()
        #udp_server()
        #udp_server("10.1.6.120")
    except Exception as e:
        print("Error! Server stopped!")
        print(e)
    

