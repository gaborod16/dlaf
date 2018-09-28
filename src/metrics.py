from enum import Enum

class MetricBase(object):
	"""docstring for MetricBase"""
	def __init__(self, name, formula):
		super(MetricBase, self).__init__()
		self.name = name
		self.formula = formula

	def calculate(self, TP, TN, FP, FN):
		return self.formula(TP, TN, FP, FN)

	def getName(self):
		return self.name
		

class Metric(Enum):
	"""
		Enum with model evaluation metrics
	"""
	#Accuracy
	ACCURACY = MetricBase('Accuracy', lambda TP,TN,FP,FN: TP+TN / (TP+TN+FP+FN))

	#TP rate = Recall = Sensitivity
	TP_RATE = MetricBase('True Positive Rate', lambda TP,TN,FP,FN: TP / (TP+FN)),

	#TN rate = Specificity = Selectivity
	TN_RATE = MetricBase('True Negative Rate', lambda TP,TN,FP,FN: TN / (TN+FP)),

	#Precision = Positive Predictive Value
	PRECISION = MetricBase('Precision', lambda TP,TN,FP,FN: TP / (TP+FP)),

	#Negative Predictive Value
	NEG_PRED_VALUE = MetricBase('Negative predictive value', lambda TP,TN,FP,FN: TN / (TN+FN))

	#F1 Score: Harmonic average between recall and precision
	F1_SCORE = MetricBase('F1 Score', lambda TP,TN,FP,FN: 2 / ( 1/(TP/(TP+FN)) + 1/(TP/(TP+FP)) ) )

	#Single ROC point
	ROC_STEP = MetricBase('ROC Step', lambda TP,TN,FP,FN: (TP/(TP+FN), 1-TN/(TN+FP)) )