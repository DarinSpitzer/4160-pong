# 4160-pong
![image](https://user-images.githubusercontent.com/44011029/221377367-cf41c766-0798-491f-b500-32db5a41f020.png)
OS Version: Windows 10
Python Version: 3.11
Pygame Version: 2.1.2
- I chose to do pong over a game like breakout because of the interactivity of two players on one screen, even the simplest games can be fun when you are
competing.
- I kept almost all of the pong specific code inside of the pong.py model file. This means I could use my event handler, view, and game loop again by just swapping
variable names and function calls. 
- Future Work
  - I could have probably handled controls through the event manager instead of directly inside of the pong file, which would make inputs a general aspect of the
    game instead of something I'll have to rewrite. I also would have liked to add text displaying perhaps the number of times the ball bounced off of a paddle,
    the ball's speed, and a message indicating who won.
  - The ball and bouncing mechanics as well as the paddle could easily be repurposed into a breakout clone. 
