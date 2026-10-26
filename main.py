import requests 
BASE_URL = "https://dummyjson.com/carts"
DESCUENTO_MAXIMO = 12  
 
 
def obtener_carritos():
    """Descarga todos los carritos de la API y los convierte a JSON."""
    response = requests.get(f"{BASE_URL}?limit=0")
    if response.status_code == 200:
        datos = response.json()
        return datos["carts"]
    print(f"Error al obtener carritos: {response.status_code}")
    return []
if __name__ == "__main__":
    carritos = obtener_carritos()
    print(f"Se descargaron {len(carritos)} carritos")
import requests

carritos = obtener_carritos()
print("Carritos descargados:", len(carritos))
print ("Carritos:", carritos)

resultados = []
numero = 0
for carrito in carritos:
    total = 0
    for producto in carrito["products"]:
        if producto["discountPercentage"] < 12:
            total += producto["quantity"]
    if total > 0:
        numero += 1
        resultados.append({"numero": numero, "userId": carrito["userId"], "total": total})
        print("Carrito:", numero, "| Usuario:", carrito["userId"], "| Productos válidos:", total)