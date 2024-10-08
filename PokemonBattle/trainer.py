from PokemonBattle.pokemon import Pokemon


class Trainer:

    def __init__(self, name):

        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):

        if any([x.name == pokemon.name for x in self.pokemons]):
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):

        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):

        result = f"Pokemon trainer {self.name}\nPokemon count {len(self.pokemons)}"
        for pokemon in self.pokemons:
            result += '\n' + f" - {''.join(pokemon.pokemon_details())}"
        return result


pokemon = Pokemon("Pikachu", 100)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
