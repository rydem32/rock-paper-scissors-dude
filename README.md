# rock-paper-scissors-dude


An interactive python game of Rock, Paper, Scissors for users of all ages. 

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/rydem32/rock-paper-scissors-dude) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd rock-paper-scissors-dude
```

Use Anaconda to create and activate a new virtual environment, perhaps called "my-first-env":

```sh
conda create -n my-first-env python=3.8
conda activate my-first-env
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above).

## Setup

In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username (then make sure to SAVE the ".env" file aftwards):

    USER_NAME="Jon Snow"
    SECRET_PASSWORD="super duper secret"

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [".gitignore"](/.gitignore) file). This means we need to instruct each person who uses our code needs to create their own local ".env" file.

## Usage

Run the Python script:

```py
python game.py

# alternative module-style invocation (only required if importing from one file to another):
python -m game.py
```

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment.

Have fun, and share the game with family and friends! 