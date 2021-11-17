from project.pokemon import Pokemon
class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {Pokemon.pokemon_details(pokemon)}"

    def release_pokemon(self, pokemon_name: str):
        for this_pokemon in self.pokemons:
            if this_pokemon.name == pokemon_name:
                self.pokemons.remove(this_pokemon)
                return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self):
        caught_pokemons_as_str = ""
        for each_pokemon in self.pokemons:
            caught_pokemons_as_str += f"- {each_pokemon.pokemon_details()}\n"
        result = f"""
Pokemon Trainer {self.name}
Pokemon count {len(self.pokemons)}
{caught_pokemons_as_str}
"""
        return result
