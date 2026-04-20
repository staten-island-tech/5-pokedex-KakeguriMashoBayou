import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)


for x in range (0,809):
    print(data[x]["name"])

user = input("Language?")

for x in range (0,809):
    if user == "japanese":
        print(data[x]["name"]["japanese"])
    elif user == "english":
        print(data[x]["name"]["english"])
    else:
        print(data[x]["name"]["french"])

person = ("select your type:")
for pokemon in data:
  if person in pokemon["type"]:
        print(pokemon["type"]["english"])
        located = True
  else: located = False
if located == False:
    print("found nothing")
