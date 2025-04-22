import socket
import threading
from threading import Semaphore
from CONSTANTS import HOST, PORT

class SalaReuniaoServer:
    def __init__(self):
        self.host = HOST
        self.port = PORT
        self.capacidade_maxima = 5
        self.semaforo = Semaphore(self.capacidade_maxima)
        self.clientes_na_sala = 0
        self.lock = threading.Lock()
        
    def iniciar(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Servidor iniciado em {self.host}:{self.port}. Aguardando conexões...")
            
            while True:
                conn, addr = s.accept()
                threading.Thread(target=self.tratar_cliente, args=(conn, addr)).start()
    
    def tratar_cliente(self, conn, addr):
        with conn:
            print(f"Conexão estabelecida com {addr}")
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    print('Disconnected')
                    with self.lock:
                        if self.clientes_na_sala > 0:
                            self.clientes_na_sala -= 1
                            self.semaforo.release()
                    break
                
                if data == "ENTRAR":
                    if self.semaforo.acquire(blocking=False):
                        with self.lock:
                            self.clientes_na_sala += 1
                        resposta = f"ENTRADA_PERMITIDA. Pessoas na sala: {self.clientes_na_sala}/{self.capacidade_maxima}"
                    else:
                        resposta = f"SALA_CHEIA. Pessoas na sala: {self.clientes_na_sala}/{self.capacidade_maxima}"
                elif data == "SAIR":
                    with self.lock:
                        if self.clientes_na_sala > 0:
                            self.clientes_na_sala -= 1
                            self.semaforo.release()
                            resposta = f"SAIDA_CONFIRMADA. Pessoas na sala: {self.clientes_na_sala}/{self.capacidade_maxima}"
                        else:
                            resposta = "ERRO: Ninguém na sala para sair"
                elif data == "STATUS":
                    resposta = f"Pessoas na sala: {self.clientes_na_sala}/{self.capacidade_maxima}"
                else:
                    resposta = "COMANDO_INVALIDO"
                
                conn.sendall(resposta.encode())
                print(resposta)
        
        print(f"Conexão encerrada com {addr}")

if __name__ == "__main__":
    server = SalaReuniaoServer()
    server.iniciar()
