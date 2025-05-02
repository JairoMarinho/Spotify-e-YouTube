import json
import os

def load_credentials():
    path = os.path.join(os.path.dirname(__file__), "credentials.json")
    if not os.path.exists(path):
        raise FileNotFoundError("Arquivo de credenciais não encontrado.")
    
    with open(path, 'r') as file:
        return json.load(file)
