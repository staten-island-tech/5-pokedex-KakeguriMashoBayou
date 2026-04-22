import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
moves=open("./moves.json", encoding="utf8")
data_2= json.load(moves)


'''for x in range(0,809):
    print(data[x]["name"])
person = input("Language? Japanese, English, Chinese or French: ").lower()

for x in range(0,809):
    print(data[x]["name"][person])'''
data=type
located = False
for pokemon in data:
    if pokemon in pokedex["type"]:
        print(pokemon["type"]["english"])
        located = True
if not located:
    print("found nothing")

'''name = input("Name Match: ")
count = 0 
for char in data:
    if name in char["name"]["english"]:
        print(char["name"]["english"])'''
