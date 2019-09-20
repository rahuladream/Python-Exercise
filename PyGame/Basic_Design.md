The goal of the game is to avoid incoming obstacles:
The player starts on the left side of the screen.
The obstacles enter randomly from the right and move left in a straight line.
The player can move left, right, up, or down to avoid the obstacles.
The player cannot move off the screen.
The game ends either when the player is hit by an obstacle or when the user closes the window.


No multiple lives
No scorekeeping
No player attack capabilities
No advancing levels
No boss characters


SETTING UP THE GAME LOOP

The game loop does four very important things:

1. Processes user input
2. Updates the state of all game objects
3. Updates the display and audio output
4. Maintains the speed of the game


FRAME:
Every cycle of the game loop is called a frame, and the quicker you can do things each cycle, the faster your game will run. Frames continue to occur until some condition to exit the game is met.