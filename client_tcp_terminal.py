# --- Client TCP Terminal ---
import socket
import json



# Paramètres du serveur
HOST = '127.0.0.1'
PORT = 65432

def send_request(request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(json.dumps(request).encode())
        data = s.recv(1024)
        print(f"[REPONSE] {data.decode()}")

if __name__ == '__main__':
    print("=== Client TCP Terminal ===")
    while True:
        print("\nCommandes disponibles: list / subscribe / party_status / gameboard_status / move / exit")
        action = input("Action: ").strip()

        if action == 'exit':
            break

        request = {"action": action, "parameters": []}

        if action == 'subscribe':
            player = input("Nom du joueur: ")
            party_id = input("ID de la partie: ")
            request['parameters'] = [{"player": player}, {"id_party": party_id}]

        elif action in ['party_status', 'gameboard_status']:
            party_id = input("ID de la partie: ")
            player_id = input("ID du joueur: ")
            request['parameters'] = [{"id_party": int(party_id)}, {"id_player": int(player_id)}]

        elif action == 'move':
            party_id = input("ID de la partie: ")
            player_id = input("ID du joueur: ")
            move = input("Move (ex: 01): ")
            request['parameters'] = [{"id_party": int(party_id)}, {"id_player": int(player_id)}, {"move": move}]

        send_request(request)
