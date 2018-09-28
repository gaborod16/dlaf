# dataset.py

__all__ = ['Dataset', 'ImageDataset', 'TextDataset']

class Dataset(object):
	"""docstring for Dataset"""
	def __init__(self, path):
		super(Dataset, self).__init__()
		self.path = path

	def load(self):
		pass

	def save(self, path=None):
		pass
	
	""" Dataset manipulation """
	def split(self, *percs):
		pass

	def clone(self):
		pass

	""" Data evaluation methods """
	def pca(self):
		pass

	def kruskalWallis(self):
		pass

	def lda(self):
		pass

	def corrSpearman(self):
		pass

	def corrPearson(self):
		pass

	def casesRedundancy(self):
		pass

	def valRedundancy(self):
		pass

	def describe(self):
		pass

	def describeAttr(self, attr):
		pass

	""" Abstract methods """
	@abc.abstractmethod
	def augment(self):
		pass


class ImageDataset(Dataset):
	"""docstring for ImageDataset"""
	def __init__(self, path):
		super(ImageDataset, self).__init__(path)

	def augment(self):
		pass

class TextDataset(Dataset):
	"""docstring for TextDataset"""
	def __init__(self, path):
		super(TextDataset, self).__init__(path)

	def augment(self):
		pass
		