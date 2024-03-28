import pandas as pd

class Pokemon:
  def __init__(self, name, type1, type2, total, hp, attack, defense, sp_atk, sp_def, speed):
    self.name = name
    self.type1 = type1
    self.type2 = type2
    self.total = total
    self.hp = hp
    self.attack = attack
    self.defense = defense
    self.sp_atk = sp_atk
    self.sp_def = sp_def
    self.speed = speed


def load_pokemon(filename):
  #Load dataset
  df = pd.read_csv(filename)
  #Create a dictionary of Pokemon objects, with Pokemon name as keys
  pokemon_dict = {}
  for index, row in df.iterrows():
    #Create a Pokemon object for each row
    pokemon = Pokemon(row['Name'], row['Type 1'], row['Type 2'], row['Total'], 
                      row['HP'], row['Attack'], row['Defense'], row['Sp. Atk'], 
                      row['Sp. Def'], row['Speed'])
    #Add the Pokemon object to the dictionary
    #The Pokemon name is used as the key
    pokemon_dict[row['Name']] = pokemon
  return pokemon_dict

pokemon_dict = load_pokemon('pokemon.csv')
list(pokemon_dict.keys())[:5]

def simulate_battle(pokemon1, pokemon2):
  #Retrieve the two Pokemon objects from the dictionary
  pokemon1 = pokemon_dict[pokemon1]
  pokemon2 = pokemon_dict[pokemon2]

  #Calculate the total stats of each Pokemon
  pokemon1_total = pokemon1.hp + pokemon1.attack + pokemon1.defense + pokemon1.sp_atk + pokemon1.sp_def + pokemon1.speed
  pokemon2_total = pokemon2.hp + pokemon2.attack + pokemon2.defense + pokemon2.sp_atk + pokemon2.sp_def + pokemon2.speed
  
  #Check if both pokemon were found
  if not pokemon1 or not pokemon2:
    return "Pokemon not found"
  
  #Determine the winner based on total stats
  if pokemon1_total > pokemon2_total:
    winner = pokemon1.name
  elif pokemon2_total > pokemon1_total:
    winner = pokemon2.name
  else:
    winner = "It's a tie!"
  
  return f'The winner is {winner}!'

simulate_battle_result = simulate_battle('Pikachu', 'Bulbasaur')
print(simulate_battle_result)
