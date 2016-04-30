import json
import urllib2
import sys

def getJSON(username):
	""" str -> dictcd
	
	Returns JSON object of users dashboard.
	
	Arguments:
		username {[str]} -- A string containing a username
	"""
	#Try to grab the JSON object, handles 404 and 429(I guess reddit doesn't like this)
	while True:
		try:
			url = "https://reddit.com/u/"+username+".json"
			data = json.load(urllib2.urlopen(url))
			break
		except urllib2.HTTPError, err:
			if str(err.code) == "429":
				continue
			else:
				print "Invalid username, try again!"
				username = raw_input("Please enter the name of the first user for comparison: ")
				continue

	return data

def run():

	#Loop as long as user wants to compare
	while True:

		print "Welcome to reddit-karma!\nA comparison tool for users' most recent posts' score\n"

		username1 = raw_input("Please enter the name of the first user for comparison: ")

		data1 = getJSON(username1)

		username2 = raw_input("Please enter the name of the second user for comparison: ")

		data2 = getJSON(username2)
		
		#Extracts karma value of the users' most-recent post
		karma1 = data1["data"]["children"][0]["data"]["score"]
		karma2 = data2["data"]["children"][0]["data"]["score"] 

		print "\n" + username1 +" received " + str(karma1) + " karma for his most-recent post, while " + username2 + " got " + str(karma2) 

		if karma1 > karma2:
			print "\n" + username1 + " got more karma, with difference being " + str(karma1-karma2) + " points.\n"
		elif karma2 > karma1:
			print "\n" + username2 + " got more karma, with difference being " + str(karma2-karma1) + " points.\n"
		else:
			print "\n Both users have the same amount of karma for their post. It's a tie!\n"

		while True:
			query = raw_input("Do you want to compare another 2 users?[Y/N]\n").lower()

			if query == "y":
				print "\n"
				break
			elif query == "n":
				print "Have a nice day ^_^"
				sys.exit(0)
			else:
				print "Invalid input\n"
				continue

run()