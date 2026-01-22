import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8080))
server.listen(5)

print("Listening on 8080")

while True:
    conn, addr = server.accept()
    print("Connection from", addr)
    conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 5\r\n\r\nHello")
    conn.close()
