import requests

from teste_app import settigns


def get_page():
	with open("%s/teste.html" % __file__) as fp:
		return fp.read()


def google(q: str):
    """Faz uma pesquisa no google"""

    return requests.get(settigns.GOOGLE, params={"q": q})
