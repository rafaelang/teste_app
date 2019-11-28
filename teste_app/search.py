import requests

from teste_app import settigns


def google(q: str):
    """Faz uma pesquisa no google"""

    return requests.get(settigns.GOOGLE, params={"q": q})
