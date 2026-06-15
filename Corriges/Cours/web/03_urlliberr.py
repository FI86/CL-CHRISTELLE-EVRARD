# Utilisation d'urllib.error Gestion des erreurs et des codes d'état

# Imports
import urllib.request
from urllib.error import HTTPError, URLError 
from http import HTTPStatus
from http.client import HTTPResponse

# =========================
# CONFIGURATION
# =========================
UTILISE_HTTPBIN = False # True = httpbin / False = w3schools ou postman


def main():
    # Génère URLError
    url = "http://no-such-server.org"
    # Génère HTTPError
    url = "http://httpbin.org/status/404" if UTILISE_HTTPBIN else "https://www.python.org/does-not-exist"
    # Devrait fonctionner
    url = "http://httpbin.org/html" if UTILISE_HTTPBIN else "https://www.iana.org/assignments/character-sets/character-sets.xhtml?utm_source=chatgpt.com"


    # Creation d'une requete avec un header pour simuler un navigateur et eviter erreur 403 par les sites.
    # pas obligatoire, mais sans ca beaucoup de site bloque la demande d'acces.
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

    # Utiliser la gestion des exceptions pour tenter l'accès à l'URL
    try:
        resultat: HTTPResponse = urllib.request.urlopen(req)
        print(f"Code retour : {resultat.status}")

        if (resultat.getcode() == HTTPStatus.OK):
            print(resultat.read().decode('utf-8'))
    # Se produit lorsque le serveur renvoie un code d'erreur de non-succès
    except HTTPError as err:
        print(f"Erreur : {err.code}")
        print(f"URL : {err.url}")
    # Se produit lorsque quelque chose ne va pas avec l'URL elle-même
    except URLError as err:
        print(f"Ce serveur n'existe pas. {err.reason}")
    except Exception as e:
        print(f"Une erreur non attendue est survenue : {e}")

if __name__ == "__main__":
    main()
