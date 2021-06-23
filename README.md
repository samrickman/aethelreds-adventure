# Aethelred's adventure

This is a tiny little text-based RPG my 6 year old daughter and I made together. The story and many of the design choices were hers (e.g. the flaming blue horse representing the King's tax collectors).

![Aethelred's Adventure](https://raw.githubusercontent.com/samrickman/aethelreds-adventure/main/img/demo.png)

Features:

1. Colored spaces giving the appearance of highly pixellated images (60x30).
2. Multiple choice or text responses.
3. Locked rooms until a condition is met (e.g. item collected or correct answer given in another room).

The schema folder also contains a script that will draw a network map generated from the game data files you have have implemented so far (or a map of the complete game when it is finished).

## How to play online

Go to: https://samrickman.github.io/aethelred/

Note: This is a terminal in a virtual machine. It might take about thirty seconds to load the first time you play it. Downloading and running locally is easier if you wish to play regularly (...).

If it does not start automatically (even after some text appears), click the green Play button in the bottom-right hand corner.

## How to run locally

### Installation 

To run, you will need to have [Python (3.7+)](https://www.python.org/downloads/), [pip](https://pip.pypa.io/en/stable/installing/), [virtualenv](https://pypi.org/project/virtualenv/) and [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed. 

Once this is done, open a terminal to the folder you want to download the game to and:

On Windows:
```
git clone https://github.com/samrickman/aethelreds-adventure
.\venv\Scripts\activate
pip install -r .\requirements.txt
python main.py
```

On Mac/Linux:
```
git clone https://github.com/samrickman/aethelreds-adventure
source venv/bin/activate
pip install -r .\requirements.txt
python main.py
```

This should enter the game. Once you leave, don't forget to deactivate the virtual environment (or just close the window):

```
deactivate venv
```

### Running

Once you have installed once, you should just be able to run by navigating to the folder in a terminal and typing:

```
python main.py
```


## How it works / how to modify

This is a simple game. 

The images are generated to text in imgviewer.py.

The only other logic happens in main.py, which reads in the room json files, prints the options, and then enters the next room depending which option the user selected.

The rooms are json files in the /rooms folder. 

As long as you have an intro room called "intro.json", you can delete everything else, and change the options accordingly.

If your room does not have an image, set the "image" property to _false_ (no quotes).

# TODO:

This is not a very complex game and it is not a very good story. It was just fun to do with a child.

Now there is a basic game, I suspect we will make the story more complex, and less nonsensical over time.