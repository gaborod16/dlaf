from base import Algorithm

class LogisticRegression(Algorithm):
	"""docstring for LogisticRegression"""
	def __init__(self):
		super(LogisticRegression, self).__init__("Logistic Regression")
		self.params = {}

	def predict(self):
		pass

	def train(self):
		pass
	
	def optimiseParams(self):
		pass


# --- Usage --- #

if __name__ == '__main__':
	L = LogisticRegression()
	print("End")