import socket
import time
from CONSTANTS import HOST, PORT

class FuncionarioCliente:
    def __init__(self, nome):
        self.nome = nome
        self.host = HOST
        self.port = PORT
        self.na_sala = False
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def conectar(self):
        try:
            self.socket.connect((self.host, self.port))
            print(f"{self.nome} conectado ao servidor.")
            self.menu_principal()
        finally:
            self.socket.close()
    
    def enviar_comando(self, comando):
        try:
            self.socket.sendall(comando.encode())
            return self.socket.recv(1024).decode()
        except:
            return "ERRO: Conexão com o servidor perdida"
    
    def menu_principal(self):
        while True:
            if self.na_sala:
                self.menu_dentro_sala()
            else:
                self.menu_fora_sala()
    
    def menu_fora_sala(self):
        print(f"Menu - {self.nome} (FORA da sala)")
        print("1. Tentar entrar na sala")
        print("2. Ver status da sala")
        print("3. Sair do sistema")
        
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            resposta = self.enviar_comando("ENTRAR")
            if "ENTRADA_PERMITIDA" in resposta:
                self.na_sala = True
                print(f" {self.nome} entrou na sala. {resposta}")
            else:
                print(f" {resposta}")
        
        elif opcao == "2":
            resposta = self.enviar_comando("STATUS")
            print(f"Status da sala: {resposta}")
        
        elif opcao == "3":
            print(f"{self.nome} está saindo do sistema...")
        
        else:
            print("Opção inválida. Tente novamente.")
        
        time.sleep(1)          
    
    def menu_dentro_sala(self):
        print(f"Menu - {self.nome} (DENTRO da sala)")
        print("1. Sair da sala")
        print("2. Ver status da sala")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            resposta = self.enviar_comando("SAIR")
            if "SAIDA_CONFIRMADA" in resposta:
                self.na_sala = False
                print(f" {self.nome} saiu da sala. {resposta}")
            else:
                print(f" {resposta}")
        
        elif opcao == "2":
            resposta = self.enviar_comando("STATUS")
            print(f"Status da sala: {resposta}")
        
        else:
            print("Opção inválida. Tente novamente.")
        
        time.sleep(1)  # Pequena pausa para melhor legibilidade
            

if __name__ == "__main__":
    nome_funcionario = input("Digite o nome do funcionário: ")
    cliente = FuncionarioCliente(nome_funcionario)
    
    cliente.conectar()
