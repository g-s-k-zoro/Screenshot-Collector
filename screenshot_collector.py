###Python program to automate screenshots of web pages or websites.
##Note - the system cannot be used for other applications while the program is running as it takes screenshot.

import webbrowser
import pyautogui
import time
import os

file = open('URL_list.txt','r')		#The file which contains the list of URLs
urls = file.readlines()
i = 1							#First image saved is named as image1.png

for url in urls:
	webbrowser.open(url)	#open the default web browser
	time.sleep(20)			#waiting time for website to load, should be set based on internet speed available. (here 20s)
	
	pyautogui.screenshot('/path/Images/image'+str(i)+'.png')	#Specify the path of the folder where the images need to be stored instead of 'path'
	
	i+=1
	
os.system("killall -9 'Google Chrome'")		#To close the browser(Here the default browser is Google chrome)