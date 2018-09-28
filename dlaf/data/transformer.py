class DataTrain(object):
	"""
	Encapsulates a dataset and adds a chaining method pattern
	for its transformation.

	:param dataset: a Dataset, the one to modify.
		
	"""
	def __init__(self, dataset):
		super(DataTrain, self).__init__()
		self.dataset = dataset

	""" Dataset modification """

	def removeAttr(self, *attrs):
		return self

	def pickAttr(self, *attrs):
		return self

	def filter(self, tuple):
		return self

	""" Data modification """

	def normalise(self):
		return self

	def rmCorrelation(self, threshold):
		return self

	def topPCA(self, nComponents):
		return self

	""" Pre-defined combinations """

	""" Additional methods """

	def apply(self):
		return self.dataset	