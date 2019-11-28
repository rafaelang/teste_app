from setuptools import setup, find_packages

setup(
    name='teste_app',
    version='0.0.1',
    url='https://github.com/rafaelang/teste_app',
    license='Apache 2.0 License',
    author='Rafael',
    author_email='rafael@gmail.com',
    keywords='teste distribuição',
    description='Aplicação de teste para distribuição',
    packages=find_packages(),
    install_requires=["requests"],
    test_suite='test',
)
