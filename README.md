# Sistema de Controle de Sala de Reunião 🏢👥

Um sistema cliente-servidor para gerenciar o acesso concorrente a uma sala de reunião virtual, implementado em Python com sockets e threads.

## 📋 Pré-requisitos

- Python 3.6 ou superior
- Git (para clonar o repositório)

## 🚀 Como começar

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/sala-reuniao.git
cd sala-reuniao
```

### 2. Configuração

O projeto já inclui o arquivo `CONSTANTS.py` com as configurações padrão:

```python
HOST = 'localhost'  # Endereço do servidor
PORT = 12345       # Porta de comunicação
```

Para alterar essas configurações, edite este arquivo antes de iniciar os componentes.

## ⚙️ Executando o sistema

### Iniciar o servidor

Em um terminal:

```bash
python server.py
```

O servidor mostrará:
```
Servidor iniciado em localhost:12345. Aguardando conexões...
```

### Iniciar clientes

Em terminais separados (quantos desejar):

```bash
python client.py
```

Cada cliente solicitará:
```
Digite o nome do funcionário: 
```

## 🖥️ Como usar

### Fluxo do cliente

1. **Fora da sala**:
   - `1. Tentar entrar na sala` → Solicita acesso
   - `2. Ver status da sala` → Mostra ocupação atual
   - `3. Sair do sistema` → Encerra o cliente

2. **Dentro da sala**:
   - `1. Sair da sala` → Libera sua vaga
   - `2. Ver status da sala` → Mostra ocupação atual

### Capacidade da sala
- Máximo de 5 pessoas simultâneas (configurável no servidor)

## 🛠️ Personalização

Para alterar a capacidade da sala, edite `server.py`:

```python
self.capacidade_maxima = 5  # Altere este valor
```

## 📜 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## ⁉️ Problemas conhecidos

- Se o servidor for encerrado abruptamente, os clientes podem ficar em estado inconsistente
- Não há persistência de estado (reiniciar o servidor zera a sala)

Sinta-se à vontade para reportar issues ou contribuir com melhorias!
