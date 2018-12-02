from urllib import request
import subprocess
import os

def getsubs(flag = 1): 
	# flag = 0 means trash series
	# flag = 1 means pewds
	url = "https://www.youtube.com/user/"
	if(not flag):
		url += "tseries"
	else:
		url += "PewDiePie"	
	r = request.urlopen(url)
	bytecode = r.read()
	htmlstr = bytecode.decode()
	ind = htmlstr.find("subscribers")
	lol = ""
	for i in range(ind-11,ind-1):
		lol += htmlstr[i]
	lol2 = ""
	for i in lol:
		if i in "0123456789":
			lol2 += i	
	return int(lol2)

lastdiff = 0

while True:
	tgay = getsubs(0)
	pewds = getsubs(1)
	diff = pewds-tgay
	print(diff)
	xd = (diff//1000)-(lastdiff//1000)
	subprocess.Popen(['notify-send', str(diff)])
	if(xd >= 2):
		os.system("xdg-open bitch_lasagna.mp3")
		lastdiff = diff
	elif xd <= -2:
		subprocess.Popen(['notify-send', 'Youtuber is ending. Create more accounts and sub to pewdiepie'])
		lastdiff = diff

