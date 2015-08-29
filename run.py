"""
This script runs an AI using the RubricStrategy based on past gameplay observed while running run.py.
"""
from Player import Player
import strategies
import sys
import time
import random
from Breeder import Breeder

# Init player
player = Player()

# Init strategy
host = "127.0.0.1"
user = "root"
password = ""
player.strategy = strategies.RubricStrategy(host, user, password)

#skip = False
# Loop
while(player.play()):
	time.sleep(3)
print "I guess it's over"
