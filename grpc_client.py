# grpc_client.py (mock)

def send_move(id_player, id_party, row, col):
    print(f"[gRPC MOCK] Move reçu - player: {id_player}, party: {id_party}, row: {row}, col: {col}")
    # Simule un mouvement réussi
    return "OK"
