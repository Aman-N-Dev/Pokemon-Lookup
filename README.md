# Pokemon Lookup

A simple command-line Python application that retrieves Pokémon information using the PokéAPI.

## Features

- Search for any Pokémon by name
- Displays:
  - Name
  - Pokédex ID
  - Height
  - Weight
- Handles invalid Pokémon names gracefully
- Uses the PokéAPI to fetch live data

---

## Technologies Used

- Python 3
- requests
- REST API
- JSON

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/pokedex-cli.git
```

Move into the project folder:

```bash
cd pokedex-cli
```

Install the required package:

```bash
pip install requests
```

---

## Usage

Run the program:

```bash
python main.py
```

Example:

```text
Enter pokemon name: pikachu

Name: pikachu
ID: 25
Height: 4
Weight: 60
```

---

## Project Structure

```
pokedex-cli/
│
├── main.py
├── README.md
└── requirements.txt
```

---

## API Used

This project uses the free PokéAPI.

https://pokeapi.co/

---

## Concepts Practiced

- Functions
- User Input
- HTTP Requests
- APIs
- JSON
- Dictionaries
- Conditional Statements
- Error Handling

---

## Future Improvements

- Display Pokémon types
- Display abilities
- Show sprite image
- Show base stats
- Display evolution chain
- Compare two Pokémon
- Save favourite Pokémon
- Build a graphical user interface (GUI)

---

## License

This project is for educational purposes.