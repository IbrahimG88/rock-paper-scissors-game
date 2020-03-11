# Rock Paper Scissors game

### Run the app
- Run the python file rps.py

### Play the game
- First you choose either to play a single round or multiple rounds
- There 4 types of player strategies you may choose from
- Play the traditional rock paper scissors game with its rules
- The player with the highest scores wins the game

### About the project
- The main target of the project is practicing object oriented programming in python.
- Every player strategy is a subclass that inherits from a parent class called `Player()`.
- The project starts compiling the code of the py file from the `__init__()` function
- Every player class has multiple methods like `__init__()`, `move()` that applies the user's move per turn and a `learn()` function that remembers the players moves from the previous rounds.
- The game has an option of playing a single or multiple rounds. For playing the multiple rounds option, to create this functionality in python a `for..in` loop in addition to `range()` method are being used, that accepts an integer as a parameter that creates a playing round equivalent to the argument's value.
