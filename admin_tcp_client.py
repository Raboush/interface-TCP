# admin_tcp_client.py (mock)

def send_to_admin(message):
    print(f"[Admin MOCK] Message reçu: {message}")
    
    if message.startswith("SUBSCRIBE"):
        # Simule une réponse : rôle et ID du joueur
        return "villager:23"
    elif message == "LIST_GAMES":
        # Simule une liste d'ID de parties
        return "1,2,3"
    else:
        return "KO"
