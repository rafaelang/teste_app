import os

import requests

from teste_app import settigns


def get_page():
	with open("%s/teste.html" % os.path.dirname(__file__)) as fp:
		data = fp.read()

    with open("%s/tempaltes/template1.html" % os.path.dirname(__file__)) as fp:
        data2 = fp.read()

    return data, data2


def google(q: str):
    """Faz uma pesquisa no google"""

    return requests.get(settigns.GOOGLE, params={"q": q})
