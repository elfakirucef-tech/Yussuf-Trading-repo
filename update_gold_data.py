import os
import requests
import json
from datetime import datetime

def get_market_data():
    print("Collecte des données de l'or...")
    # Utilisation d'une API gratuite pour récupérer le prix de l'or (XAU/USD)
    url = "https://binance.com" # PAXG réplique l'Or en temps réel
    try:
        response = requests.get(url).json()
        price = float(response['price'])
    except:
        price = "Indisponible (Week-end ou erreur API)"

    # Calcul de la session actuelle (Heure UTC)
    current_hour = datetime.utcnow().hour
    if 0 <= current_hour < 7:
        session = "Tokyo (Asie Range)"
    elif 7 <= current_hour < 13:
        session = "Londres (Forte Volatilité)"
    elif 13 <= current_hour < 16:
        session = "Londres / New York Overlap (Volatilité Maximale)"
    elif 16 <= current_hour < 22:
        session = "New York (Forte Volatilité)"
    else:
        session = "Marché Calme / Transition"

    # Simulation des indicateurs si l'API de base ne les fournit pas
    # (Note : Pour de vrais indicateurs précis MT5, l'utilisation d'une clé API payante est requise)
    data = {
        "timestamp_utc": datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        "prix_xau_usd": price,
        "session_actuelle": session,
        "note": "Données actualisées en temps zéro. Prêtes pour analyse SMC et Elliott."
    }

    # Sauvegarde dans le fichier lu par Claude
    with open("donnees_temps_zero.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    get_market_data()
