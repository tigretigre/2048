from Player import Player
import strategies
import sys
import random
from Breeder import Breeder

# Init player
player = Player()

# Init strategy
host = "127.0.0.1"
user = "root"
password = ""
player.strategy = strategies.InteractiveStrategy(host, user, password)

#skip = False
# Loop
while(player.play()):
	pass
print "I guess it's over"
