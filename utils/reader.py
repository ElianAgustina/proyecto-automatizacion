# archivo lector de csv


import csv
import json


def read_users_csv():
   # Abrir el archivo CSV y leer su contenido
    with open("data/users.csv", newline="") as csvfile:
       
        # Crear un lector de CSV que interprete cada fila como un diccionario
        reader = csv.DictReader(csvfile)
        return list(reader)

print(read_users_csv())
def read_products_json():
    #Lee un archivo JSON y devuelve su contenido.
    #return: Contenido del archivo JSON.
    with open("data/products.json") as jsonfile:
        data = json.load(jsonfile)
    return data
print(read_products_json())
