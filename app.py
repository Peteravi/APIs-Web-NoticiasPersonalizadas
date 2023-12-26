import requests

def solicitar_noticias(api_key, tema, idioma='es'):
    url = 'https://newsapi.org/v2/everything'
    parametros = {'q': tema, 'language': idioma, 'apiKey': api_key}

    try:
        respuesta = requests.get(url, params=parametros)
        respuesta.raise_for_status()
        return respuesta.json()['articles']

    except requests.exceptions.HTTPError as errh:
        print(f"Error HTTP: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error de conexión: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Error de tiempo de espera: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error en la solicitud: {err}")
    return None

def imprimir_noticias(noticias):
    if noticias:
        for i, noticia in enumerate(noticias, 1):
            print(f"{i}. {noticia['title']} - {noticia['url']}")
    else:
        print("No se pudieron obtener noticias.")

def main():
    api_key = '2d86aea7d53648508f829b7f2de29dcb'
    
    tema = input("Ingresa el tema de noticias que te interesa (ej. Apple): ")

    noticias = solicitar_noticias(api_key, tema)
    imprimir_noticias(noticias)

if __name__ == "__main__":
    main()
