# Pokeapi-Pokedex

**Note: this repo assumes that you are using Python 3.**

- This is a ~basic~ tool to use in your terminal of choice, to view data on a given pokemon.

* Run the below command in your terminal to pull this repo onto your machine.
 ```bash
git clone https://github.com/kaseypcantu/pokeapi-pokedex.git
```

* You will need `pip install` the packages listed in `requirements.txt`, using the following command `pip` will fetch all the dependencies necessary to run `pokemon.py` on your machine.
```bash
pip install -r requirements.txt
```

* Get usage info - accessing the `help` data using the `-h` argument.
```bash
python3 pokemon.py -h
```
 `python3 pokemon.py -h` _output_:
 ```bash
usage: pokemon.py [-h] P

Search for a given Pokemon to view a detailed summary.

positional arguments:
  P           desired pokemon to fetch a summary for

optional arguments:
  -h, --help  show this help message and exit
```

```bash
python3 pokemon.py darkrai
```

_Application output_:
 
| Pokemon   | Type   |   Number |   Weight | Ability    |
|-----------|--------|----------|----------|------------|
| darkrai   | dark   |      581 |      505 | bad-dreams |



[Data for this tool is provided by Pokeapi](https://pokeapi.co/ "Pokeapi Homepage")