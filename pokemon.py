#!/usr/local/env python3.8

import argparse
import json
import requests
from tabulate import tabulate


def write_file(data, pokemon):
    f = open("./json-data/" + pokemon + ".json", "w")
    f.write(data)
    f.close()


def format_json(obj):
    return json.dumps(obj, indent=4)


def pokemon_parser():
    poke_arg_parser = argparse.ArgumentParser(
        description="Search for a given Pokemon to view a detailed summary."
    )

    poke_arg_parser.add_argument(
        "pokemon", metavar="P", type=str, help="desired pokemon to fetch a summary for"
    )

    args = vars(poke_arg_parser.parse_args())
    pokemon = list(args.values())[0]

    get_pokemon_data(pokemon=pokemon)


def get_pokemon_data(pokemon):
    summary = []
    url = "https://pokeapi.co/api/v2/pokemon/" + str(pokemon)

    r = requests.get(url=url)

    json_data = r.json()
    json_data_formatted = format_json(json_data)

    name = json_data["name"]
    poke_number = json_data["order"]
    ability = json_data["abilities"][0]["ability"]["name"]
    poke_type = json_data["types"][0]["type"]["name"]
    weight = json_data["weight"]

    summary = [
        {
            "Pokemon": name,
            "Type": poke_type,
            "Number": poke_number,
            "Weight": weight,
            "Ability": ability
        }
    ]

    print(tabulate(summary, headers="keys", tablefmt="github"))

    write_file(json_data_formatted, pokemon=pokemon)

    return json_data


if __name__ == "__main__":
    pokemon_parser()
