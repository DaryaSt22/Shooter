1) Arcade Shooter
A simple space-style shooter: you control a fighter at the bottom of the screen, move horizontally, and fire rockets upward at descending aliens. Each successful hit respawns the alien and increases its speed slightly. The game tracks your score and shows “Game Over!” when an alien reaches the player’s line.
2) Rectangle Mover (mini demo)
A tiny practice game to learn keyboard events and screen redraws: move a rectangle around the window with the arrow keys; useful for experimenting with colors, positions, and event handling.

Tech stack: 
Python 3 with Pygame for 2D graphics, input handling, and the main loop.

Object-oriented structure: Game, Fighter, Alien, Ball, plus a small constants.py for screen, speeds, and UI text.

Sprite assets: images/fighter.png, images/alien.png, images/rocket.png.

Basic code quality: import sorting via isort.