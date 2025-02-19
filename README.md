# Aethelred's adventure

This is a tiny little text-based RPG my 6 year old daughter and I made together. The story and many of the design choices were hers (e.g. the flaming blue horse representing the King's tax collectors).

![Aethelred's Adventure](https://raw.githubusercontent.com/samrickman/aethelreds-adventure/main/img/demo.png)

Features:

1. Colored spaces giving the appearance of highly pixellated images (60x30).
2. Multiple choice or text responses.
3. Locked rooms until a condition is met (e.g. item collected or correct answer given in another room).

The schema folder also contains a script that will draw a network map generated from the game data files you have have implemented so far (or a map of the complete game when it is finished).

## How to play online

The game is hosted [here](https://aethelreds-adventure-production.up.railway.app/) using [Railway](https://railway.com/). 

Note: This is a terminal in a virtual machine. It might take about thirty seconds to load the first time you play it. Downloading and running locally is easier if you wish to play regularly (...).

## How to run locally

### Installation 

To run, you will need to have [Python (3.12+)](https://www.python.org/downloads/), [pip](https://pip.pypa.io/en/stable/installing/), [virtualenv](https://pypi.org/project/virtualenv/) and [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed. 

Once this is done, open a terminal to the folder you want to download the game to and:

On Windows:
```
git clone https://github.com/samrickman/aethelreds-adventure
cd .\aethelreds-adventure\
python -m venv venv
.\venv\Scripts\activate
pip install -r .\requirements.txt
python main.py
```

On Linux/Mac:

```
git clone https://github.com/samrickman/aethelreds-adventure
cd aethelreds-adventure/
python -m venv venv
source venv/bin/activate
pip install -r .\requirements.txt
python main.py
```

This should enter the game.

### Running

Once you have installed once, you should just be able to run by navigating to the folder in a terminal, activating the virtual environment (either `.\venv\Scripts\activate` on Windows or `` on Linux/Mac) and typing:

```
python main.py
```


## How it works / how to modify

This is a simple game. 

The images are generated to text in `imgviewer.py`.
The rooms are `json` files in the `/rooms` folder. 

The only other logic happens in `main.py`, which reads in the room `json` files, prints the options, and then enters the next room based on the option the user selected.

To extend the game, as long as you have an intro room called `intro.json`, you can delete everything else, and change the options accordingly.

If your room does not have an image, set the following property in the room `json` file:

```
"image" : false
```