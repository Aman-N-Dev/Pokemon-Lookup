import requests
baseURL = "https://pokeapi.co/api/v2/"

def get_info(name):
    url = f"{baseURL}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json() # converts json to python dict
        return pokemon_data

    else:
        print(f"Failed to retreive data {response.status_code}")

pokemon_name = input("Enter pokemon name: ")
pokemon_name = pokemon_name.lower()
pokemon_info = get_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"]}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")

