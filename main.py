import requests 
BASE_URL = "https://dummyjson.com"
DESCUENTO_MAXIMO = 12  # solo descuento estrictamente menor a 12%
 
 
def obtener_carritos():
    """Descarga todos los carritos de la API y los convierte a JSON."""
    response = requests.get(f"{BASE_URL}/carts?limit=0")
    if response.status_code == 200:
        datos = response.json()
        return datos["carts"]
    print(f"Error al obtener carritos: {response.status_code}")
    return []

