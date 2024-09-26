class MatrixController(object):
	"""docstring for ClassName"""
	def __init__(self, Matrix):
		self.Matrix = Matrix

		

	def printMatrix(self):
		for lign in self.Matrix.matrix:
			for cell in lign:
				print("0", end=" ")
			print()