import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('C:/Users/ASUS/PycharmProjects/assignment3/pokedex.csv')

# Count occurrences for Type 1 and Type 2
type1_counts = df['Type 1'].value_counts()
type2_counts = df['Type 2'].value_counts()

# Set the style for seaborn
sns.set(style="whitegrid")

# Plot for Type 1
plt.figure(figsize=(10, 6))
sns.barplot(x=type1_counts.index, y=type1_counts.values)
plt.title('Distribution of Pokémon by Primary Type (Type 1)')
plt.xlabel('Type 1')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()  # Display the chart

# Plot for Type 2
plt.figure(figsize=(10, 6))
sns.barplot(x=type2_counts.index, y=type2_counts.values)
plt.title('Distribution of Pokémon by Secondary Type (Type 2)')
plt.xlabel('Type 2')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()  # Display the chart

import pandas as pd

# Load the dataset
df = pd.read_csv('C:/Users/ASUS/PycharmProjects/assignment3/pokedex.csv')

# Sort the DataFrame by the 'Total' column in descending order and get the top 10 Pokémon
top_10_pokemon = df.sort_values(by='Total', ascending=False).head(10)

# Display the top 10 Pokémon
print("Top 10 Pokémon based on Total stats:")
print(top_10_pokemon[['Name', 'Type 1', 'Type 2', 'Total']])

import cv2

# List of Pokémon details (image paths and data)
pokemon_data = [
    {'path': 'C:/Users/ASUS/PycharmProjects/assignment3/images/1058.png', 'name': 'Eternatus Eternamax', 'type1': 'Poison', 'type2': 'Dragon', 'stat': 1125},
    {'path': 'C:/Users/ASUS/PycharmProjects/assignment3/images/475.png', 'name': 'Rayquaza Mega Rayquaza', 'type1': 'Dragon', 'type2': 'Flying', 'stat': 780},
    {'path': 'C:/Users/ASUS/PycharmProjects/assignment3/images/202.png', 'name': 'Mewtwo Mega Mewtwo Y', 'type1': 'Psychic', 'type2': None, 'stat': 780},
    {'path': 'C:/Users/ASUS/PycharmProjects/assignment3/images/201.png', 'name': 'Mewtwo Mega Mewtwo X', 'type1': 'Psychic', 'type2': 'Fighting', 'stat': 780},
    {'path': 'C:/Users/ASUS/PycharmProjects/assignment3/images/473.png', 'name': 'Groudon Primal Groudon', 'type1': 'Ground', 'type2': 'Fire', 'stat': 770},
    {'path': 'C:/Users/ASUS/PycharmProjects/assignment3/images/471.png', 'name': 'Kyogre Primal Kyogre', 'type1': 'Water', 'type2': None, 'stat': 770},
    {'path': 'C:/Users/ASUS/PycharmProjects/assignment3/images/961.png', 'name': 'Necrozma Ultra Necrozma', 'type1': 'Psychic', 'type2': 'Dragon', 'stat': 754},
    {'path': 'C:/Users/ASUS/PycharmProjects/assignment3/images/605.png', 'name': 'Arceus', 'type1': 'Normal', 'type2': None, 'stat': 720},
    {'path': 'C:/Users/ASUS/PycharmProjects/assignment3/images/865.png', 'name': 'Zygarde Complete Forme', 'type1': 'Dragon', 'type2': 'Ground', 'stat': 708},
    {'path': 'C:/Users/ASUS/PycharmProjects/assignment3/images/1054.png', 'name': 'Zacian Crowned Sword', 'type1': 'Fairy', 'type2': 'Steel', 'stat': 700}
]

# Loop through each Pokémon entry, loading and displaying the image with details
for pokemon in pokemon_data:
    img = cv2.imread(pokemon['path'])

    # Check if the image was loaded successfully
    if img is not None:
        # Add text to the image for name, type, and stat
        display_text = f"{pokemon['name']} - {pokemon['type1']}/{pokemon['type2']} - Stat: {pokemon['stat']}"
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, display_text, (10, 30), font, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

        # Show the image with the details
        cv2.imshow(f"Pokémon Image - {pokemon['name']}", img)
        cv2.waitKey(0)  # Wait until a key is pressed to close the image
        cv2.destroyAllWindows()
    else:
        print(f"Image at {pokemon['path']} not found or could not be loaded.")

import pandas as pd

# Load the dataset
df = pd.read_csv('C:/Users/ASUS/PycharmProjects/assignment3/pokedex.csv')

# Code 1: Top 5 Pokémon based on Attack + Special_attack
df['Attack_Total'] = df['Attack'] + df['Special_attack']
top_5_attack = df.sort_values(by='Attack_Total', ascending=False).head(5)
print(top_5_attack[['Name', 'Attack', 'Special_attack', 'Attack_Total']])

# Code 2: Top 5 Pokémon based on Defense + Special_defense
df['Defense_Total'] = df['Defense'] + df['Special_defense']
top_5_defense = df.sort_values(by='Defense_Total', ascending=False).head(5)
print(top_5_defense[['Name', 'Defense', 'Special_defense', 'Defense_Total']])

# Code 3: Top 5 Pokémon based on HP
top_5_hp = df.sort_values(by='HP', ascending=False).head(5)
print(top_5_hp[['Name', 'HP']])

# Code 4: Top 5 Pokémon based on Speed
top_5_speed = df.sort_values(by='Speed', ascending=False).head(5)
print(top_5_speed[['Name', 'Speed']])

import csv
import json

# File paths
csv_file_path = 'C:/Users/ASUS/PycharmProjects/assignment3/pokedex.csv'
json_file_path = 'C:/Users/ASUS/PycharmProjects/assignment3/pokedex.json'

# CSV to JSON conversion
pokemon_data = []
with open(csv_file_path, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        # Adjust keys to match the structure you need
        pokemon_entry = {
            "name": row["Name"],
            "type1": row["Type 1"],
            "type2": row.get("Type 2", None),  # Using None if "Type 2" is blank
            "total": int(row["Total"]),
            "img": f"images/{row['Index']}.png"  # Assuming images are named by Pokémon ID
        }
        pokemon_data.append(pokemon_entry)

# Save to JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(pokemon_data, json_file, indent=4)
