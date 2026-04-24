import json

name = input("Name")
city = input("city")
age = input("age")

detalles = {
    "name": name,
    "city": city,
    "age": age
}
paquete = open("detalles.json", "w")
json.dump(detalles, paquete)
paquete.close()

print("Guardado correctamente")