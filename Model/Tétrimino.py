class Tetrimino(object):
	def __init__(self):
		
class Tetrimino_I(Tetrimino):
	def __init__(self):
		self.type = "I"
		self.colour = "Aqua"
		self.size = [[1,1,1,1]]

class Tetrimino_O(Tetrimino):
	def __init__(self):
		self.type = "O"
		self.colour = "Yellow"
		self.size = [[1,1],[1,1]]

class Tetrimino_T(Tetrimino):
	def __init__(self):
		self.type = "T"
		self.colour = "Purple"
		self.size = [[1,1,1],[0,1,0]]

class Tetrimino_L(Tetrimino):
	def __init__(self):
		self.type = "L"
		self.colour = "Orange"
		self.size = [[1,1,1],[1,0,0]]

class Tetrimino_J(Tetrimino):
	def __init__(self):
		self.type = "J"
		self.colour = "Blue"
		self.size = [[1,1,1],[0,0,1]]

class Tetrimino_Z(Tetrimino):
	def __init__(self):
		self.type = "Z"
		self.colour = "Red"
		self.size = [[1,1,0],[0,1,1]]

class Tetrimino_S(Tetrimino):
	def __init__(Self):
		self.type = "S"
		self.colour = "Green"
		self.size = [[0,1,1],[1,1,0]]