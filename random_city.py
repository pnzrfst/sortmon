import requests
import random

def random_sc_city() :
    url = "https://brasilapi.com.br/api/ibge/municipios/v1/sc";

    response = requests.get(url);

    cities = response.json()

    randomCity = random.choice(cities);

    return randomCity["nome"]