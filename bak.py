import json
import urllib2
import sys



while True:

	print "Welcome to reddit-karma!\nA comparison tool for users' most recent posts' score\n"

	username1 = raw_input("Please enter the name of the first user for comparison: ")

	while True:
		try:
			url1 = "https://reddit.com/u/"+username1+".json"
			data1 = json.load(urllib2.urlopen(url1))
			break
		except urllib2.HTTPError, err:
			if str(err.code) == "429":
				continue
			else:
				print "Invalid username, try again!"
				username1 = raw_input("Please enter the name of the first user for comparison: ")
				continue

	username2 = raw_input("Please enter the name of the second user for comparison: ")

	while True:
		try:
			url2 = "https://reddit.com/u/"+username2+".json"
			data2 = json.load(urllib2.urlopen(url2))
			break
		except urllib2.HTTPError, err:
			if str(err.code) == "429":
				continue
			else:
				print "Invalid username, try again!"
				username2 = raw_input("Please enter the name of the second user for comparison: ")
				continue

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
