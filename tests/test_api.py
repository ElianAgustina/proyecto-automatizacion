import requests
import pytest_check as check
from utils.logger import logger
def test_get_user(base_url, headers):

    try:
        logger.info("Testing GET user functionality.")
        # Headers para la solicitud, incluyendo la clave de API

        # Realizar la solicitud GET a la API
        response = requests.get(f"{base_url}/users/2", headers=headers)

        # Obtener el código de estado de la respuesta
        codigo = response.status_code

        # Obtener los datos de la respuesta en formato JSON
        data = response.json()

        # 1er nivel de validación: Verificar que el código de estado sea 200 (OK)
        assert codigo == 200

        #2do nivel encabezado: Verificar que el encabezado 'Content-Type' sea 'application/json'
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

        # 3er nivel de validación: Verificar que los datos de la respuesta sean un diccionario
        assert isinstance(data, dict) # Verificar que 'data' sea un diccionario
        assert 'data' in data 
        logger.info(f"Retrieved user data: {data['data']}")
        # Verificar que 'data' sea una lista
        assert isinstance(data["data"],dict)

        #assert 'id' in data["data"]
        check.is_in('id', data["data"])
        
        #assert 'email' in data["data"]
        check.is_in('email', data["data"])

        #assert 'first_name' in data["data"]
        check.is_in('first_name', data["data"])
        
        #assert 'last_name' in data["data"]
        check.is_in('last_name', data["data"])

        # 4to contenido
       # assert data["data"]["id"] == 2
        check.equal(data["data"]["id"], 2)
        
        #assert data["data"]["email"] == "janet.weaver@reqres.in"
        check.equal(data["data"]["email"], "janet.weaver@reqres.in")

        # NIVEL 5 : TIEMPO DE RESPUESTA
        assert response.elapsed.total_seconds() < 2  # Verificar que el tiempo de respuesta
        logger.info(f"GET user test completed successfully.")
    except Exception as e:
        logger.exception(f"An error occurred during the GET user test: {str(e)}")
        raise
    

def test_create_user(base_url, headers):
    try:
        logger.info("Testing create user functionality.")
        # Datos del nuevo usuario a crear
        new_user = {
            "first_name": "Felipe",
            "last_name": "Carillanca",
            "email": "felipe.carillanca@reqres.in",
            "job": "Developer"
        }

        # Realizar la solicitud POST a la API para crear un nuevo usuario
        response = requests.post(f"{base_url}/users", headers=headers, json=new_user)

        # Obtener el código de estado de la respuesta
        codigo = response.status_code

        # Obtener los datos de la respuesta en formato JSON
        data = response.json()

        # NIVEL 1: Validar que el código de estado sea 201 (Created)
        assert codigo == 201

        # NIVEL 2: Verificar el encabezado 'Content-Type'
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

        # NIVEL 3: ESTRUCTURA
        data = response.json()
        #assert "email" in data
        check.is_in("email", data)
        #assert "first_name" in data
        check.is_in("first_name", data)
        #assert "last_name" in data
        check.is_in("last_name", data)
        #assert "id" in data
        check.is_in("id", data)
        logger.info(f"User created with ID: {data['id']}")

        # NIVEL 4: Validar el contenido de los datos
        #assert data["email"] == new_user["email"]
        check.equal(data["email"], new_user["email"])
        #assert data["first_name"] == new_user["first_name"]
        check.equal(data["first_name"], new_user["first_name"])
        #assert data["last_name"] == new_user["last_name"]
        check.equal(data["last_name"], new_user["last_name"])
        logger.info(f"User data validated: {data['first_name']} {data['last_name']} - {data['email']}")

        # NIVEL 5 : TIEMPO DE RESPUESTA
        assert response.elapsed.total_seconds() < 2  # Verificar que el tiempo de respuesta
        logger.info("Create user test completed successfully.")
    except Exception as e:
        logger.exception(f"An error occurred during the create user test: {str(e)}")
        raise

def test_delete_user(base_url, headers):
    try:
        logger.info("Testing delete user functionality.")
        user_id = 1 # Lista de usuarios a eliminar

        response = requests.delete(f"{base_url}/users/{user_id}", headers=headers)

        # Obtener el código de estado de la respuesta
        codigo = response.status_code

        # NIVEL 1: Validar que el código de estado sea 204 (No Content)
        assert codigo == 204  # Verificar que el código de estado sea 204 (No Content)
        # NIVEL 2: Verificar que el encabezado 'Content-Type' no esté presente
        assert 'application/json' not in response.headers
        # NIVEL 3: Verificar que el contenido de la respuesta esté vacío
        assert response.content == b''  # Verificar que el contenido de la respuesta esté vacío

        assert response.elapsed.total_seconds() < 2  # Verificar que el tiempo de respuesta
        logger.info(f"User with ID {user_id} deleted successfully.")
    except Exception as e:
        logger.exception(f"An error occurred during the delete user test: {str(e)}")
        raise