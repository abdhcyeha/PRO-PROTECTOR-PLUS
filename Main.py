import pyautogui
import time
import requests
import termcolor
import socks
import urllib
import json

time.sleep(3)
print("ANTICHEAT LOADING---- MADE BY FARTLORD AND CYPPHI")

PLAYER_HACKING = input("Which Player is Hacking?")
def Main():
   pyautogui.keyDown("t")
   pyautogui.keyUp("t")
   pyautogui.typewrite("/ban "+PLAYER_HACKING)
   pyautogui.keyDown("enter")
   pyautogui.keyUp("enter")

time.sleep(2)
Main()
