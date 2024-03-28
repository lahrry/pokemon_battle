import tkinter as tk
from tkinter import ttk
from Pokemon import simulate_battle, pokemon_dict

# Create the main window
root = tk.Tk()
root.title('Pokémon Battle Game')

# Function to call when the battle button is clicked
def on_battle():
  pokemon_name1 = pokemon_selector1.get()
  pokemon_name2 = pokemon_selector2.get()
  # Call the simulate_battle function from Pokemon.py
  result_text.set(simulate_battle(pokemon_name1, pokemon_name2))

# Dropdown for selecting the first Pokémon
pokemon_selector1 = ttk.Combobox(root, values=list(pokemon_dict.keys()))
pokemon_selector1.pack()

# Dropdown for selecting the second Pokémon
pokemon_selector2 = ttk.Combobox(root, values=list(pokemon_dict.keys()))
pokemon_selector2.pack()

# Button to start the battle
battle_button = ttk.Button(root, text='Battle!', command=on_battle)
battle_button.pack()

# Text to display the battle result
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

#Start the main event loop
root.mainloop()