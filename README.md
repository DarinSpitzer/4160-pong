# 4160-pong
![image](https://user-images.githubusercontent.com/44011029/221377367-cf41c766-0798-491f-b500-32db5a41f020.png)
OS Version: Windows 10
Python Version: 3.11
Pygame Version: 2.1.2
- I chose to do pong over a game like breakout because of the interactivity of two players on one screen, even the simplest games can be fun when you are
competing.
- I kept almost all of the pong specific code inside of the pong.py model file. This means I could use my event handler, view, and game loop again by just swapping
variable names and function calls. 

Overview:
- GameLoop.py
    - Contains the loop and clock to keep movement consistent. The loop calls both move functions inside of the Pong model each frame as well as updating the screen and calling the EventHandler
- View.py
    - Declares the dimensions of the screen and the caption, and then has a function to fill the background as well as a functioni that updates each of the three moving objects in the game. Due to the simplicity of the game itself, having each get handled inside of the same function works really well. Unforunate result is this function is not very reusable.
- EventHandler.py
  - Very simple class, because the movement is all handles directly in the model, all the event handler does right now is detect the game closing, but if I were to continue developing this game I would add support for win and loss custom events.
- Pong.py
  - This is my model file, and where the large majority of the code is. 
  - The first section is bounds, which simply contains a few different rects on the edges of the screen to handle bouncing or stopping the ball and paddles. 
  - The next section declares the rects for both paddles as well as sets their speed. The move_paddles function uses pygame.key.get_pressed() to move each paddle up or down using W and S or Up and Down. At the end of the function it clamps them to the rect that encompasses the whole screen.
  - The ball class has quite a few members, including self explanatory ones like size, pos, and speed. It also has down, right, and hits. Down and Right are bools, and given their combination, determines what direction the ball is travelling, as there are only four valid directions (it only bounces at 90 degree angles). Hits increments every time the ball collides with a paddle, and then increses speed by 100 until it reaches its maximum speed of 2000. 
  - Inside of ball, thehre are two functions:
  - check_collision: This function works by checking if the ball is colliding with each of the bounds rects, and then flipping the Down and Right booleans accordingly. If it collides with the paddles, hits gets incremented after the direction gets switched. If the ball collides with either of the walls, its speed is set to 0 and the function ends, locking the ball in place. 
  - move_ball: This function calls check_collision at the beginning, then determines the delta speed, checks the Right and Down variables to choose what direction to move the ball, then calls move_ip on it, and finishes by clamping it to the bounds of the screen.
Future Work:
- I could have probably handled controls through the event manager instead of directly inside of the pong file, which would make inputs a general aspect of the
    game instead of something I'll have to rewrite. I also would have liked to add text displaying perhaps the number of times the ball bounced off of a paddle,
    the ball's speed, and a message indicating who won.
  - The ball and bouncing mechanics as well as the paddle could easily be repurposed into a breakout clone. 
