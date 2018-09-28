import abc

class Algorithm(object):
	"""docstring for Algorithm"""
	def __init__(self, title):
		super(Algorithm, self).__init__()
		self.title = title
		self.model = None
		self.params = {}

	def loadModel(self):
		pass
	
	def saveModel(self):
		pass

	@abc.abstractmethod
	def predict(self):
		pass

	@abc.abstractmethod
	def train(self):
		pass

	@abc.abstractmethod	
	def optimiseParams(self):
		pass