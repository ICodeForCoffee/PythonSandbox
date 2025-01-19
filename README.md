# Python Sandbox

A series of scripts for learning about Python that calculate and do various things.

## DiceProbability.py - Two Dice Result Probability Graphs

A program to generate a graph of the probability of the result of rolling two d6 dice for values of 10, 100, 1,000, and 10,000 times.

[View file.](https://github.com/ICodeForCoffee/PythonSandbox/blob/main/DiceProbability.py)

## Fibonacci.py - Fibonacci Number Generator

Generate any Fibonacci number you want.

[View file.](https://github.com/ICodeForCoffee/PythonSandbox/blob/main/Fibonacci.py)

## MontyHall.py - Monty Hall Problem Tester

The Monty Hall Problem is an interesting statistical problem and a brain teaser, and it is named after the famous host of Let's Make a Deal, Monty Hall. 

The problem is defined as follows. First, there are three doors, and one of the doors has a prize. A contestant will pick a door. The host will then open one of the doors that contestant has not chosen and will reveal that the prize is not behind that door. The host will then offer the contestant the opportunity to change doors. Most people think the odds of the prize being behind their door is 50/50 when it's really 1/3rd. There is a 2/3rd chance the prize is behind the door that was not opened. This code proves experimentally the 2/3rd probably of getting the prize if you switch doors.

For more information about the Monty Hall problem, [check out the Wikipedia article](https://en.wikipedia.org/wiki/Monty_Hall_problem).

[View file.](https://github.com/ICodeForCoffee/PythonSandbox/blob/main/MontyHall.py)

## RollForAbilityArray.py - Roll For Ability Array

Creates a graph that compares the average of roled ability scores in D&D compared to the standard array.

[View file.](https://github.com/ICodeForCoffee/PythonSandbox/blob/main/RollForAbilityArray.py)

## RollForAbilityScore.py - Roll For Ability Score

Graph of the probability of an ability score by rolling four d6s and dropping the lowest value.

[View file.](https://github.com/ICodeForCoffee/PythonSandbox/blob/main/RollForAbilityScore.py)

## RollWithAdvantage1.py - Roll With Advantage

Calculates how useful it is to roll a d20 with advantage is. Rolling with advantage is defined as throwing two d20 and using the highest rolled value for the ability or attack roll.

In real life, some players will throw the same day twice while other others will throw two different dice, and they might even throw those two dice at the same time. That means are two ways to look at probability here. First, we can treat the dice rolls as if they occur separately, meaning we look at how the second die improves the result based on what the result of the first die landed on. Second, we can treat the rolls as concurrent, which means that improvement is based on the lowest dice thrown between those two rolls. How we frame the question changes how we calculate the results of the improvement advantage gives.

[View file.](https://github.com/ICodeForCoffee/PythonSandbox/blob/main/RollWithAdvantage1.py)

## RollWithAdvantage2.py - Roll With Advantage, Graphed

Graphs the possible outcomes of rolling with advantage and how much advantage that gives. Provides graphs for the probability of each roll, a graph of the improvement if you treat the dice as separate events, and a graph if you treat the dice as concurrent events.

[View file.](https://github.com/ICodeForCoffee/PythonSandbox/blob/main/RollWithAdvantage2.py)

## Sudoku.py - Sudoku Solver

Solves Suddoku. This project has a main() file, two class files, and multiple test files you can run through the application.

- Sudoku.py - Main() [View file.](https://github.com/ICodeForCoffee/PythonSandbox/blob/main/Sudoku.py)
- SudokuPuzzle.py - Class that represents a Sudoku puzzle. [View file.](https://github.com/ICodeForCoffee/PythonSandbox/blob/main/SudokuPuzzle.py)
- SudokuSolver.py - Logic for solving a Sudoky puzzle. [View file.](https://github.com/ICodeForCoffee/PythonSolver.py)

## VectorizationVsLoops.py - Vectorization vs Loops

A file that explores the difference between array vectorization and using a for loop to populate values into an array. For some reason the first time you run vectorization it's a little slow compared to when the technique is called again.

[View file.](https://github.com/ICodeForCoffee/PythonSandbox/blob/main/VectorizationVsLoops.py)
