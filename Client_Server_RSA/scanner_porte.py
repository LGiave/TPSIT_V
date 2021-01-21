import socket

def main():
  
    available_ports = []
  
    ip = "127.0.0.1"	
  
    
    for port in range(8000,65536):
        print(f"port = {port}")
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        res = c.connect_ex((ip,port))

        if  res == 0:	#success
            print(f"{port} availalbe")
            available_ports.append(port)

        c.close()

    print(available_ports)
    

    

if __name__ == "__main__":
    main()