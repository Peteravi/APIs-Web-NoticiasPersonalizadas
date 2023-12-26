import requests

def solicitar_noticias(api_key, tema, idioma='es'):
    url = 'https://newsapi.org/v2/top-headlines'
    parametros = {'apiKey': api_key, 'category': tema, 'language': idioma}

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
    api_key = '6edef1c1da2c412bba4b6235c2f68429'
    
    temas_validos = ['business', 'technology', 'science', 'health', 'sports', 'entertainment']
    tema = input("Ingresa el tema de noticias que te interesa (ej. business, technology, science): ")

    while tema.lower() not in temas_validos:
        print("Tema no válido. Temas válidos: business, technology, science, health, sports, entertainment")
        tema = input("Ingresa el tema de noticias que te interesa: ")

    noticias = solicitar_noticias(api_key, tema)
    imprimir_noticias(noticias)

if __name__ == "__main__":
    main()
