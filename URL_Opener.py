import webbrowser

def abrir_url_youtube(url):
    if "youtube.com" in url or "youtu.be" in url:
        webbrowser.open(url)
        print(f"Abrindo a URL: {url}")
    else:
        print("URL inválida para Youtube")

url = input(f"Insira aqui uma URL do Youtube: ")
abrir_url_youtube(url)