from Model import Matrix
from Controller import MatrixController

matrice = Matrix.Matrix()
MatriceController = MatrixController.MatrixController(matrice) 

MatriceController.printMatrix()