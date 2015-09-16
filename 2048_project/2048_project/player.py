import urllib2
import json
import moves

BASE_URL = 'http://2048.semantics3.com/hi'

class Player(object):
	_score = 0

	def __init__(self):
		self._start()
		self._strategy = None

	def play(self):
		move = self.strategy.getMove(self._grid)
		move.execute()
                self.strategy.reportResults(self._grid, self._score)
		return_value = self.check_state()
		if return_value == False:
			self.strategy.reportFinalResults(self._grid, self._score)
		return return_value

	def check_state(self):
		if self._won:
			return False
		elif self._over:
			return False
		else:
			return True

	def _start(self):
		ret_val = urllib2.urlopen("%s/start/json" % BASE_URL)
		data = json.loads(ret_val.read())
		self.session_id = data['session_id']
		self._grid = data['grid']

	def execute(self, command):
		url = "%s/state/%s/%s/json" % (BASE_URL, self.session_id, command)
		ret_val = urllib2.urlopen(url)
		data = json.loads(ret_val.read())
		for row in data['grid']:
			line = '|'
			for cell in row:
				line += "{:4d}|".format(cell)
			print line

		self._grid = data['grid']
		self._won = data['won']
		self._over = data['over']
		self._score = data['score']

	@property
	def strategy(self):
		return self._strategy or None

	@strategy.setter
	def strategy(self, strategy):
		self._strategy = strategy
		self._strategy.registerPlayer(self)
