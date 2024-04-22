# Classes and Objects

# Big Ideas:
#   - Classes allow us to couple data and functions together
#   - Objects are the ACTUAL representation of the classes


# Create a Pokemon class; this represents a Pokemon
class Pokemon:  # use a capital letter for class name
    def __init__(self):
        """A special method (function) called the
        Constructor. Contains all the properties/variables
        that describe a Pokemon."""
        self.name = ""
        self.id = 0
        self.weight = 0
        self.height = 0
        self.type = "normal"
        self.actual_cry = "Roooooooooooooar!"

        print("A new Pokémon is born!")

    def cry(self) -> str:
        """Represents the sound a Pokemon makes

        Returns:
           - string representing the sound it makes"""
        return f'{self.name} says, "{self.actual_cry}"!'

    def eat(self, food: str) -> str:
        """Represents feeding the Pokemon

        Params:
            - food: what food you feed it

        Return:
            - what it says after eating it"""
        if food.lower() == "berry":
            return f'{self.name} ate the berry and says, "YUM!"'
        elif food.lower() == "potion":
            return f"{self.name} consumed the potion and feels healthier!"
        else:
            return f"{self.name} batted the {food} away."


# Create a new child class of Pokemon
class Pikachu(Pokemon):
    def __init__(self, name="pikachu"):
        # Call constructor of parent class
        super().__init__()


        # Assign the default values to properties
        self.name = name
        self.id = 25
        self.type = "electic"
        self.actual_cry = "pikachu"

    def thundershock(self, defender: Pokemon) -> str:
        """simulate a thundershock attack against another pokemon.
        params:
            - defender: defending pokemon
            
        returns:
            str representing result of attack.
            """
        response = f"{self.name} used thundershock on {defender.name}"

        if defender.type.lower() in ["water", "flying"]:
            response = response + "it was super efffective."

        return response
# Create a new child-class of pokemon for the type of your choice
# If you don't know any pokemon, use this: https://pokemondb.net/pokedex/national
#   - create a new child class
#   - create a constructor and set the default values for its properties
#       - i.e. its name, id, type, etc.
#   - create a new method for its attack
class Eevee(Pokemon):
    def __init__(self, name="eeve"):
        
        super().__init__()
        
        self.name = name
        self.id = 133
        self.type = "normal"
        self.actual_cry = "eevee"  
    
    def swift(self, defender: Pokemon) -> str:
      
        response = f"{self.name} used swift on {defender.name}"

        if defender.type.lower() in ["rock", "steel"]:
            response = response + "not every effective."
        if defender.type.lower() in ["ghost"]:
            response = response + "no effect."

        return response
# Create two Pokemon using our class
# Make one Pokemon that is Pikachu
pokemon_one = Pokemon()

# Change some properties in pokemon_one
#   Change its name
print(pokemon_one.name)  # ""
pokemon_one.name = "Pikachu"
print(pokemon_one.name)  # "Pikachu"

pokemon_one.id = 25
pokemon_one.type = "Electric"

print(pokemon_one.id)
print(pokemon_one.type)


# Make one Pokemon of your choice
# Store it in a variable called
#    pokemon_two
#    - you can make Squirtle
#       - id -> 4
#       - type -> "Water"
pokemon_two = Pokemon()

pokemon_two.name = "Squirtle"
pokemon_two.id = 4
pokemon_two.type = "water"

print(pokemon_two.name)
print(pokemon_two.id)
print(pokemon_two.type)

pokemon_one.actual_cry = "Pikachu"
pokemon_two.actual_cry = "GRRraaggrrggg"

print(pokemon_one.cry())
print(pokemon_two.cry())

# Test the eat method
print(pokemon_one.eat("berry"))
print(pokemon_one.eat("potion"))
print(pokemon_one.eat("poison"))  # mr. ubial does not condone
print(pokemon_two.eat("berry"))
print(pokemon_two.eat("potion"))
print(pokemon_two.eat("poison"))  # mr. ubial does not condone

pikachu_one = Pikachu()
pikachu_two = Pikachu("speedy")

print(pikachu_one.name)  #pikachu
print(pikachu_two.name)
print(pikachu_one.cry())
print(pikachu_two.eat("potion"))

print(pikachu_one.thundershock(pokemon_one))
print(pikachu_two.thundershock(pokemon_two))