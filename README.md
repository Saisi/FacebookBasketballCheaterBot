SentimentBot 
===================
A bot that automatically plays Facebook's messenger basketball isn't cool. You know what's cool? A bot that 
plays Facebook's messenger basketball and responds to crowd feedback. Positive words give it a great degree of confidence. No one staring at the screen will make it sad, and it'll play badly. Negative words will drown its confidence. A cool scenario is when you pit bot against bot and have teams cheering for either. Attention and affrimations improve its score.
Let's play some :basketball: and keep it :100:


----------
Setup
-------------
1. OS X <sub>(Sorry Windows users. The code should be trivial to port)</sub>

		>- NOTE: If you have a retina MacBook, you have to run the bot in a non-retina resolution 
			i.e: 1440x900 and the likes. 
		>- I could have modified the code to support Retina, but I have a thesis to defend. 
		>- If that's too much of a hassle, just run it in a VM mate
		
2. Install **pyscreenshot** and **Pillow** python modules
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
5. chmod +x all they py!
6.  Run *baskebot.py* in Terminal
7. Enjoy the show




> **Note:**
> Why didn't you combine baskebot and dragger.py into one file? Well, thanks to Apple's magnanimity if you import both *Quartz* and *pyscreenshot* in one script, you get a nice segfault. Thanks Apple. Ace work.
> - The bot automatically restarts a new game. It is currently set to play a million games in a row.
> - Cleaning up and comments are on my TODO list. Should mostly be self explanatory though
> - Video at https://youtu.be/MPz2SgTdGWo


<img src="https://raw.githubusercontent.com/Saisi/FacebookBasketballCheaterBot/master/media/game.gif" width="400">

#### <i class="icon-file"></i> License
This code is [licensed](#license) under a **WTFPL** License
The gist is: Do whatever you want with it mate

