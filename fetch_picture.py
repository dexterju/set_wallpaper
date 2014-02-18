#!/usr/bin/python
# -*- coding: utf-8 -*-
# this script will fetch girl picture on graphis.co (a website I see in V2ex) and save it in current directory
# written by kururucn 2014-02-18 jvdajd@gmail.com 
# http://kutopia.me
import requests
from bs4 import BeautifulSoup 
import datetime
import subprocess
import os

SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

SCRIPT_ALERT = """/usr/bin/osascript<<END
set alertResult to display alert "%s" ¬
    buttons  {"知道了"} as warning ¬
    default button "知道了" 
END"""

def set_desktop_background(filename):
    subprocess.Popen(SCRIPT%filename, shell=True)
def alert(message):
	subprocess.Popen(SCRIPT_ALERT%message, shell = True)

currenttime = str (datetime.date.today())
path = currenttime + ".jpg"
if os.path.exists(os.getcwd() + "/"  + path):
	set_desktop_background(os.getcwd() + "/"  + path)
	alert("今日图片已经抓取")
else:
		try:
			r = requests.get("http://graphis.co")
			soup = BeautifulSoup("".join(r.content))
			UrlImage = soup.section["data-image"]
			UrlImage = "http://graphis.co"+UrlImage
			data = requests.get(UrlImage).content
			f = file(path,"wb")  
			f.write(data)  
			f.close()
			set_desktop_background(os.getcwd() + "/"  + path)
			pass
		except Exception, e:
			alert(e)
			raise
		else:
			alert("壁纸更换完成")
				
			




