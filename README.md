# Aethelred's adventure

This is a tiny little text-based RPG I made with my 6 year old daughter. The story and many of the design choices were hers (e.g. the flaming blue horse representing tax collection).

Features:

1. Highly pixellated images (60x30) - thanks [Nikhil Kumar Singh]( https://github.com/nikhilkumarsingh/terminal-image-viewer/blob/master/img-viewer.py).
2. Multiple choice or text responses.
3. Locked rooms until a condition is met (e.g. item collected or correct answer given in another room).

The schema folder also contains a script that will draw a network map generated from the game data files you have have implemented so far (or a map of the complete game when it is finished).

## How to play online

Go to:


## How to run locally

To run, you will need to have Python (3.7+), [pip](https://pip.pypa.io/en/stable/installing/), [virtualenv](https://pypi.org/project/virtualenv/) and [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed. 

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