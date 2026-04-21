import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)


for x in range(0,809):
    print(data[x]["name"])
person = input("Language? Japanese, English, Chinese or French: ").lower()

for x in range(0,809):
    print(data[x]["name"][person])

located = False
person = ("select your type:")
for pokemon in data:
    if person in pokemon["type"]:
        print(pokemon["type"]["english"])
        located = True
if located == False:
    print("found nothing")

count = 0 
name = input("Name Match")  