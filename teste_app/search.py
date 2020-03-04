import requests

from teste_app import settigns


def get_page():
	with open("teste.html") as fp:
		return fp.read()


def google(q: str):
    """Faz uma pesquisa no google"""

    return requests.get(settigns.GOOGLE, params={"q": q})
