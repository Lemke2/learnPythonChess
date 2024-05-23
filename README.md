# learnPythonChess
Chess game I made in 2021 when I decided to learn python, before starting I had never written a line of python code

# Reqs:
Pygame

# How it works
Works by manipulating strings to "draw" on a board. Simulates legal moves by creating pseudo-legal moves, then actually playing them and looking if an illegal positions (own king under attack) occurs. This, paired with the fact that it's written in an OOP fashion and in python with lots of iteration makes it painfully slow when simulating milions of moves (chesswiki positions to ensure it handles all positions properly, even very fringe positions (en passant, underpromotions etc..))

