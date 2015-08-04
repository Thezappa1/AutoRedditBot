#!/usr/bin/env python

import schedule
import praw
import pdb
import re
import os
import time
from datetime import datetime

# Our method we want to run
def job():
	# Set up
	user_name='chochoblock'
	pw='password12@A'
	help=[]
	phrases = {
	'generalphrases':[
		'i have a bug',
		'have a problem',
		'need help',
		'lol issues',
		'lol bug',
		'big issue',
		'report a problem',
		'fix crash',
		'update issues',
		'update issue',
		'unknown error',
		'big issue in lol',
		'this needs fixing',
		'got hacked',
		'how to install PBE',
		'what data do riot collect',
		'data they collect'
		],
	'accountphrases':[
		'i lost my password',
		'cant access account',
		'cannot access account',
		'locked out of account',
		'i got suspended',
		'account is suspended',
		'account transfer help',
		'recover my username',
		'recover my password',
		'odd email from riot',
		'suspended from lol boards',
		'account got hacked',
		'account hacked',
		'account got deleted',
		'lost my summoner name',
		'refer a friend',
		'transfer lol account',
		'bought lol account'
		],
	'techphrases':[
		'lol login issue',
		'lol patching issue',
		'patching issue',
		'lol sound issues',
		'friend list missing',
		'summoner name issue',
		'reinstalling league',
		'low frame rate issue',
		'low frame rate problem'
		],
	'billingphrases':[
		'want a refund',
		'want refund',
		'aram skin boosts',
		'lol payment methods',
		'chargebacks',
		'credit card fraud',
		'stolen lol account',
		'lol account stolen',
		'store error',
		'session expired',
		'store is blank',
		'i have encountered an error'
		],
	'gameplayphrases':[
		'friend discovery',
		'champion guides',
		'party rewards',
		'ranked player faq',
		'riots matchmaking guide',
		'honor system faq',
		'is there a colourblind mode',
		'queue dodging'
	]}
	 
	responses = {
		'generalphrases': 'Sorry you are experiencing a problem! You should try their website:\n\n(https://support.riotgames.com)\n\n for support topics that may help\n\n _____ \n\n I am still in development!',
		'accountphrases': 'You should try their website:\n\n(https://support.riotgames.com/hc/en-us/categories/200137684)\n\n for support topics that may help\n\n _____ \n\n I am still in development!',
		'techphrases': 'You should try their technical support website for an answer:\n\n(https://support.riotgames.com/hc/en-us/categories/200137704)\n\n for support topics that may help\n\n _____ \n\n I am still in development!',
		'billingphrases': 'Billing issues are the worst! You should try their website:\n\n(https://support.riotgames.com/hc/en-us/categories/200137694)\n\n for support topics that may help\n\n _____ \n\n I am still in development!',
		'gameplayphrases': 'Sorry you are experiencing a problem! You should try their website:\n\n(https://support.riotgames.com/hc/en-us/categories/200134550)\n\n for support topics that may help\n\n _____ \n\n I am still in development!'
	}
	

	# don't post here for now(testing)
	banned=[
		"all"
	]

	print( "[bot] setting up connection with Reddit")

	# create reddit instance and login
	r = praw.Reddit(user_agent='Help roboot for LOL 1.0 chochoblock')
	disable_warning=True
	r.login(user_name, pw)
	print('logged in')

	# Have we run this code before? If not, create an empty list
	if not os.path.isfile("posts_replied_to.txt"):
		posts_replied_to = []
		
	# If we have run the code before, load the list of posts we have replied to
	else:
		# Read the file into a list and remove any empty values
		with open("posts_replied_to.txt", "r") as f:
			posts_replied_to = f.read()
			posts_replied_to = posts_replied_to.split("\n")
			posts_replied_to = filter(None, posts_replied_to)

	# Get the top 15 values from our subreddit, change this to leagueoflegends to run it there
	subr=r.get_subreddit('test')
	for submission in subr.get_hot(limit=15):
		# If we haven't replied to this post before and it is not in our banned list
		if submission.id not in posts_replied_to and subr not in banned:
			submissionall = submission.title + ' ' + submission.selftext
			# Do a case insensitive search
			for k,v in phrases.iteritems():
				for phrase in v:
					if re.search(phrase, submissionall, re.IGNORECASE):
						if phrase in v:
							submission.add_comment(responses[k])
							# Store the current id into our list
							posts_replied_to.append(submission.id)
							print "Bot replying to : ", submission.title + ' ' + submission.id
							# exists the loop
							break
						
	# Write our updated list back to the file
	print('posted to txt')
	with open("posts_replied_to.txt", "w") as f:
		for post_id in posts_replied_to:
			f.write(post_id + "\n")       
	
#Schedule every minute to do job
schedule.every(1).minutes.do(job)

#Our pending sleeper
while True:
	schedule.run_pending()
	print('sleeping -- '+datetime.now().strftime('%H:%M:%S'))
	time.sleep(58)