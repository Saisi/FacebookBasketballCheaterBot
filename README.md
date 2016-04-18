BasketBot 
===================
A bot that automatically plays(*cough..cheats. at.. cough*) Facebook's messenger basketball. Wish this was some cool Machine Learning? Nope, this is pure pixel tracking and Euclidean geometry. I wrote this because I was bored and procrastinating on my thesis; so the code is sloppy and rushed. But it works! Highest recorded score so far is **70**. The bot could be improved to hit **99** but I have some real life stuff to handle so I leave that to you mate. Let's play some :basketball: and keep it :100:


----------
Setup
-------------
1. OS X <sub>(Sorry Windows users. The code should be trivial to port)</sub>
		i.	NOTE: If you have a retina MacBook, you have to run the bot in a non-retina resolution i.e: 1440x900 and the likes. I could have modified the code to support Retina, but I have a thesis to defend. If that's too much of a hassle, just run it in a VM mate
		
2. Install **pyscreenshot** and **PIL** python modules
3. Install Bluestacks App player. Get it from http://www.bluestacks.com/download.html 

*	Open the App Player and do the necessary login stuff
*	Install Facebook Messenger
*	Sign into Messenger

Setup
-------------
1. Load Bluestacks App Player
2. Open messenger and open the Basketball game screen
<img src="https://raw.githubusercontent.com/Saisi/FacebookBasketballCheaterBot/master/media/gamescreen.png" width="400" height="300">
3. I hardcoded the bot to locate BlueStacks at window position (-350,0). To position the window there, run the included **positioner.scpt**. <sub>If you want to change the default coordinates go to **basketbot.py** and change *window_x* and *window_y*. </sub>
4.  Now ensure, there are no windows obscuring any part of the BlueStacks App Player
5. chmod +x *basketbot.py dragger.py*
6.  Run *baskebot.py* in Terminal
7. Enjoy the show




> **Note:**

> - Certainly, the bot isn't going to score high every single time. However, the **expected value**(think probabilistically here) after numerous runs is about **33**. Highest score to date is **70**
> - Why are there two files instead of one. Well, thanks to Apple's magnanimity if you import both *Quartz* and *pyscreenshot* in one script, you get a nice segfault. Thanks Apple. Ace work.
> - The bot automatically restarts a new game. It is currently set to play a million games in a row.
> - Cleaning up and comments are on my TODO list. Should mostly be self explanatory though


<img src="https://raw.githubusercontent.com/Saisi/FacebookBasketballCheaterBot/master/media/game.gif" width="400">

#### <i class="icon-file"></i> License
This code is [licensed](#license) under a **WTFPL** License
The gist is: Do whatever you want with it mate

