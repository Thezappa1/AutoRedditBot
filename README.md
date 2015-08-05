# AutoRedditBot Running instructions:

You can run the python script from the CMD or from Python, if you want to run it once but you can also install the module schedule which runs like cron except you set it within your script.
I have added schedule(module) to my python script, with a schedule to run our method every 20 minutes.

To run it make sure you have these installed (I am running python27, later versions may have pip already):

Pip (https://pip.pypa.io/en/latest/installing.html)

		python get-pip.py

Schedule (https://pypi.python.org/pypi/schedule)

		install schedule

Git repo

  	git clone https://github.com/Thezappa1/AutoRedditBot.git

Just run our python script as you normally would in the terminal or cmd, it will continue to run until you terminate the script.
Now just make a post or two on /r/test with one of the keyphrases or keywords and watch the bot reply(Don't forget it's on a 20 minute schedule, change that to 0 or 1 for testing).
