import socket

Port = 444
FORMAT = "utf-8"
CLOSE_MESSAGE = "DECONNECTE !"
SERVER = "192.168.1.95"
addr = (SERVER, Port)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (4096 -len(send_length))
    client.send(send_length)
    client.send(message)


send("Bonjour tout le monde.")

