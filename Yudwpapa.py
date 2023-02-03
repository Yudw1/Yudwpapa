from urllib import response

import mechanize

import os

from time import sleep

import datetime

import sys

browser = mechanize.Browser()

browser.set_handle_robots(False)

cookies = mechanize.CookieJar()

browser.set_cookiejar(cookies)

browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]

browser.set_handle_refresh(False)

url = 'https://m.facebook.com/login.php'

def openlink(msg4):

    r = browser.open(msg4)

def aclass():

    browser.open(url)

    browser.select_form(nr = 0)

    browser.form['email'] = emailx

    browser.form['pass'] = pwx

    r = browser.submit()

    browser.select_form(nr = 0)

    msg1=str(input("➣Enter 2 step google code : "))

    print(msg1)

    browser.form['approvals_code'] = msg1

    r=browser.submit()

   

    browser.select_form(nr = 0)

    browser.form['name_action_selected'] = ['save_device']

    r = browser.submit()

      

      

      

    r = browser.open(url)

    x = browser.title()

    if x == "Review recent login":

        print("\nFacebook wants to review your recent actions.\nPlease fix that and then re run the program.")

        exit(1)

    if x == "Login approval needed":

        print("\nYour account is stuck on verification\nPlease do it and then re run the program.")

        exit(1)

    if x == "Epsilon":

        print("\nYour account got locked, recover it kindly and re run the script.")

        exit(1)

  

    

def poct(comment):

    browser.select_form(nr = 0)

    r = browser.submit()

print ("[-[ TH3 T00L CREATE BY YUDAW RULEX  ]-]")

emailx=str(input("➣Enter email : "))

pwx =str(input("➣Enter pswrd : "))

aclass()

msg4=str(input("➣Enter post link : "))

msg5=str(input("➣enter notpad link : "))

f=open(msg5, 'r')

lines = f.readlines()

f.close()

msg6= int(input("➣Enter TIME : "))

os.system('clear')

sys.stdout.flush()

print("\033[1;37;40m")

e = datetime.datetime.now()

print(e.strftime("Start Time = %d/%m/%Y   %I:%M:%S %p"))

count = 0

while True:

    for line in lines:

        if len(line) > 0:

            if count != 0:

                sleep(msg6)

            openlink(msg4)

            

            poct(line)

            print("\033[1;33;40m", end = "")

            print('LE BHAI GYA COMMENT SUNITA MISHRA URF KARAN KI MA KI CHUT MAI - ', line)

            print("\033[1;37;40m")

            count += 1

            

            if count % 50 == 0:

                sleep(1)
