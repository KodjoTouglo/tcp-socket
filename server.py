import socket
import threading

Port = 444
SERVER = socket.gethostname()
addr = (SERVER, Port)
FORMAT = "utf-8"
CLOSE_MESSAGE = "DECONNECTE !"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)

def gere_client(conn, addr):
    print(f"[NOUVELLE CONNEXION] {addr} connecté.")

    connected = True
    while connected:
        msg_length = conn.recv(4096).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == CLOSE_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
    conn.close()
       


def start():
    server.listen()
    print(f"[LISTENNING] Serveur en écoute sur {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=gere_client, args=(conn, addr))
        thread.start()
        print(f"[CONNEXIONS ACTIVES] {threading.activeCount() - 1 }")
        


print("[DEMARRAGE] Demarrage du serveur...")
start()

