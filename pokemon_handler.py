import pokebase as pb
import random 
from random_city import random_sc_city


side = [
    "Extrema-esquerda",
    "Centro-esquerda",
    "Centro",
    "Centro-direita",
    "Extrema-direita"
]

musicals_genres = [
    "Rock",
    "Pop",
    "Hip Hop",
    "R&B",
    "Jazz",
    "Blues",
    "Country",
    "Reggae",
    "Samba",
    "Bossa Nova",
    "Funk",
    "Eletrônica",
    "House",
    "Techno",
    "Trance",
    "Metal",
    "Punk",
    "Classical",
    "Soul",
    "Folk",
    "Gospel",
    "Sertanejo",
    "Forró",
    "Trap",
    "K-Pop"
]

tipo_traducao = {
    "normal": "Normal",
    "fighting": "Lutador",
    "flying": "Voador",
    "poison": "Venenoso",
    "ground": "Terrestre",
    "rock": "Pedra",
    "bug": "Inseto",
    "ghost": "Fantasma",
    "steel": "Aço",
    "fire": "Fogo",
    "water": "Água",
    "grass": "Planta",
    "electric": "Elétrico",
    "psychic": "Psíquico",
    "ice": "Gelo",
    "dragon": "Dragão",
    "dark": "Sombrio",
    "fairy": "Fada"
}


def getRandomPokemon(max_id = 151): 
    random_id = random.randint(1, max_id);
    
    random_pokemon = pb.pokemon(random_id, lazy_load=True);
    
    nome = random_pokemon.name;
    
    tipos = [t.type.name for t in random_pokemon.types];
    
    tipos_traduzidos = [tipo_traducao[tipo.lower()] for tipo in tipos]
    tipos_str = ", ".join(tipos_traduzidos)
    
    sprite = random_pokemon.sprites.front_default
    
    lado_politico = random.choice(side);
    
    genero_musical = random.choice(musicals_genres);
    
    encontrado_em = random_sc_city()
    
    return [{
        "sprite_url": sprite,
        "content": {
            "Nome": nome,
            "Tipo(s)": tipos_str,
            "Espectro Político": lado_politico,
            "Gênero musical mais ouvido": genero_musical,
            "Encontrado em": encontrado_em
        }
    }]