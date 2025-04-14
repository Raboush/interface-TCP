# --- Serveur TCP ---
import socket
import threading
import json

# Paramètres du serveur
HOST = '127.0.0.1'
PORT = 65432

# Fonction pour gérer les clients
def handle_client(conn, addr):
    print(f"[INFO] Connexion depuis {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            try:
                # Parse JSON
                request = json.loads(data.decode())
                print(f"[REQUETE] {request}")

                # Mock réponse du moteur d'administration/jeu
                response = {
                    "status": "OK",
                    "response": {
                        "message": f"Commande '{request.get('action')}' reçue avec succès."
                    }
                }

                conn.sendall(json.dumps(response).encode())
            except Exception as e:
                print(f"[ERREUR] {e}")
                conn.sendall(b'Erreur de traitement')

# Lancer le serveur
def start_server():
    print(f"[INFO] Démarrage du serveur sur {HOST}:{PORT}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("[INFO] Serveur en attente de connexion...")
        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

if __name__ == '__main__':
    start_server()
