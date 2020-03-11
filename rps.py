#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Created on Tue Jan  8 13:59:39 2019

# @author: ibrahimelgohary

import random


# This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round.

moves = ['rock', 'paper', 'scissors']

# The Player class is the parent class for all of the Players
# in this game


class Player():
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# Player class:
# Decscription:
# Has a method learn which has 3 parameters: self, first player move
# and the second player move
# Outputs:
# Plays a single move every round: "rock"
# Function:
# It acts as one of the two players in the rock paper scissors 3 rounds

class RandomPlayer(Player):

    def __init__(self):
        self.score = 0

    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


# RandomPlayer class:
# Description:
# Has an init function that declares a property for the score
# of a 3 rounds game,
# and the score
# is initialized to 0 at the beginning of the game.
# Has a move function that returns a random move from the moves array,
# plays either rock or paper or scissors.
# Uses the random imported module at the top of the file.
# Has a method learn which has 3 parameters: self, first player move
# and the second player move
# Outputs:
# Player's move
# Function:
# It acts as one of the two players
# in the rock paper scissors 3 rounds, that plays a random move.


class HumanPlayer(Player):

    def __init__(self):
        self.score = 0

    def move(self):
        userChoice = input("Choose a move: rock or paper or scissors:").lower()
        if (userChoice == "rock") or (userChoice == "paper")
        or (userChoice == "scissors"):
            print(f"You chose {userChoice}")
            return userChoice
        else:
            print("try again and choose one of the 3 moves")
            self.move()

    def learn(self, my_move, their_move):
        pass


# HumanPlayer class:
# Description:
# Has an init function that declares a property
# for the score of a 3 rounds game, and the score
# is initialized to 0 at the beginning of the game.
# Has a function move, that gets the user input as one
# of the 3 possible moves. If the input does not one of the
# 3 accepted choices, the user is prompted to retry inputing
# the move and recalls the move function of the class.
# Has a method learn which has 3 parameters: self, first player move
# and the second player move
# Outputs:
# Player's move
# Function:
# It acts as a human player of the two players in
# the rock paper scissors 3 rounds, that plays
# a move based on the user input.

class ReflectPlayer(Player):

        def __init__(self):
            self.moveReflect = "paper"
            self.score = 0

        def move(self):
            return self.moveReflect

        def learn(self, my_move, their_move):
                self.moveReflect = their_move


# ReflectPlayer class:
# Description:
# Has an init function that declares
# a property for the score of a 3 rounds game, and the score
# is initialized to 0 at the beginning of the game.
# It also intitializes the first move to paper as in self.moveReflect.
# Outputs:
# Plays a single move every round
# learn function: sets the moveReflect which represents the
# ReflectPlayer move to the other players move of
# the previous round.

class CyclePlayer(Player):

    def __init__(self):
            self.moveCycle = "paper"
            self.score = 0

    def move(self):
        if self.moveCycle == "paper":
            return "scissors"
        elif self.moveCycle == "rock":
            return "paper"
        elif self.moveCycle == "scissors":
            return "rock"

    def learn(self, my_move, their_move):
        self.moveCycle = my_move


# CyclePlayer class:
# Description:
# Has an init function that declares a property for
# the score of a 3 rounds game, and the score
# is initialized to 0 at the beginning of the game.
# It also intitializes the first move to paper as in
# self.moveCycle.

# Outputs:
# It outputs a move that is different every round
# based on the if statements inside the move function.
# learn function: sets the moveCycle variable to a
# certain move, which uses the CyclePlayer move of
# the previous round.


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

# beats function:
# Description:
# inputs: gets two parameters: one and two,
# which represent 1 of the 3 optional moves for both
# players and will play a role
# of deciding the winner of every round
# according to rock paper scissors game rules.

# outputs:
# 1st parameter one is which move and the
# second parameter two is which move


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

# Game class has 4 function
# an __init__ function:
# inputs:
# player 1 and player 2
# outputs:
# player 1 will be equal to p1
# player 2 will be equal to p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.play(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

# play_round function:
# inputs:
# outputs:
# the moves for player 1 and 2
# saves the player moves by calling their
# learn functions including both player moves.

# it also calls the play() function, including the 2 player moves as arguments

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        if (self.p1.score >= self.p2.score):
            print("Player 1 won")
        elif(self.p2.score >= self.p1.score):
            print("Player 2 won")
        else:
            print("Players tie")
        print("Game over!")

# play_game function:
# description:
# has a for in loop to play 3 rounds as described in the loop range
# every round: play_round function is called
# outputs:
# which player which player won the 3 rounds or if there is a tie.

    def play(self, move1, move2):

        if beats(move1, move2):
            self.p1.score += 1
            print("Player 1 wins")
            print(f"""Player 1 score: {self.p1.score} and
                Player2 score: {self.p2.score}""")
        elif beats(move2, move1):
            self.p2.score += 1
            print("Player 2 wins")
            print(f"""Player 1 score: {self.p1.score} and
                    Player2 score: {self.p2.score}""")
        else:
            print("Players tie")
            print(f"""Player 1 score: {self.p1.score} and
                    Player2 score: {self.p2.score}""")

# play function:

# inputs:
# player 1 and 2 moves

# uses the beats function to check who won
# the round according to the games rules.

# outputs:
# users scores every round
# increments the round winner score by 1 integer


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()


# game variable: initializes the game and calls the Game class and
#
# uses two arguments:
# inputs:
# the two player functions call:
# for example: HumanPlaer() and RandomPlayer()

# outputs:
# The game itself by calling the Game constructor
# and the first function to call from the Game Class: play_game().
