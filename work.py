import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)


for x in range (1,809):
    print(data[x]["name"])

user = input("Language?")

for x in range (1,809):
    if user == "japanese":
        print(data[x]["name"]["japanese"])
    elif user == "english":
        print(data[x]["name"]["english"])
    else:
        print(data[x]["name"]["fench"])

for i in range():

person= input(the_types:)
the_types={"fighting","psychic","poison","dragon","ghost","dark","ground","fire","fairy","water","flying","normal","rock","electric","bug","grass","ice","steel"}