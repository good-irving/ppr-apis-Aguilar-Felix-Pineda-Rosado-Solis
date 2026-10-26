import requests 
BASE_URL = "https://dummyjson.com/carts"
DESCUENTO_MAXIMO = 12  
 
 
def obtener_carritos():
    """Descarga todos los carritos de la API y los convierte a JSON."""
    response = requests.get(f"{BASE_URL}")
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

mejor = resultados[0]
for r in resultados:
    if r["total"] > mejor["total"]:
        mejor = r

user_id = mejor["userId"]
total_validos = mejor["total"]
print("Usuario con más productos válidos:", user_id)
print("Total de productos válidos:", total_validos) 

respuesta = requests.get(f"https://dummyjson.com/users/{user_id}")
if respuesta.status_code == 200:
    usuario = respuesta.json()
else:
    print("Error:", respuesta.status_code)
    exit()
print("Información del usuario con más productos válidos:")
print("ID:", usuario["id"])
print("Nombre:", usuario["firstName"], usuario["lastName"])
print("Email:", usuario["email"])   

nombre = usuario["firstName"]
apellido = usuario["lastName"]
ciudad = usuario["address"]["city"]

mensaje = f"El cliente con más productos regulares es {nombre} {apellido} (ID: {user_id}), de la ciudad de {ciudad}. Compró un total de {total_validos} productos válidos."

print("=" * 60)
print(mensaje)
print("=" * 60)

with open("reporte_auditoria.txt", "w", encoding="utf-8") as archivo:
    archivo.write("=" * 60 + "\n" + mensaje + "\n" + "=" * 60)