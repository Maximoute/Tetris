class Matrix(object):
	def __init__(self):
		self.matrix = self.initMatrix()
		
	def initMatrix(self):
		board = []
		for i in range(22):
			row = []
			for j in range(10):
					row.append(None)
			board.append(row)
		return board