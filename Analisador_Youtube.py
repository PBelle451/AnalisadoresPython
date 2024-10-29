import re
from urllib.parse import urlparse, parse_qs


def extrair_id_youtube(url):
    # Corrigindo a expressão regular para garantir que ela funcione com todos os formatos comuns
    padrao_id = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
    resultado = re.search(padrao_id, url)

    # Se o ID for encontrado, ele será retornado
    if resultado:
        return resultado.group(1)

    # Caso a regex falhe, tentamos outras maneiras
    parsed_url = urlparse(url)
    if parsed_url.hostname in ["youtu.be", "www.youtube.com", "youtube.com"]:
        # Se o hostname for "youtu.be" então o ID é o caminho
        if parsed_url.hostname == "youtu.be":
            return parsed_url.path[1:]

        # Se o hostname for "youtube.com" ou "www.youtube.com", o ID geralmente está na query 'v'
        elif parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
            return parse_qs(parsed_url.query).get("v", [None])[0]

    return None

url_1 = "https://www.youtube.com/watch?v=FxdXOvhVaNk"
url_2 = "https://youtu.be/pPFF__nsmAw?si=9mzzVwlWiZYdLP-_"
url_3 = "https://youtu.be/Zd8fH8dtQe0?si=jHYtXr_HBSHfHz9C"

print(extrair_id_youtube(url_1))
print(extrair_id_youtube(url_2))
print(extrair_id_youtube(url_3))