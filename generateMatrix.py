from random import randint
from printElement import PrintElement


class GenerateValues:
    def __init__(self, allowsRepeatNumber=False, startValue=1):
        self.allowsRepeatNumber = allowsRepeatNumber
        self.startValue = startValue
        self.matrix = []

    def generateRandom(self, size):
        return randint(self.startValue, size)

    def generateVector(self, sizeVector, possiblesValues):
        vector = []
        count = 0
        while (count < sizeVector):
            randomValue = self.generateRandom(possiblesValues)
            if (self.checkArray(vector, randomValue)):
                vector.append(randomValue)
                count = count + 1
        return vector

    def checkArray(self, vector, value):
        if (self.allowsRepeatNumber):
            return True
        for i in range(0, len(vector)):
            if (vector[i] == value):
                return False
        return True

    def checkVector(self, matrix, vector):
        for i in range(0, len(matrix)):
            if (self.isEqualVectors(vector, matrix[i])):
                return False
            if (vector == matrix[i]):
                return False
        return True

    def isEqualVectors(self, vectorFirst, vectorLast):
        if (self.allowsRepeatNumber):
            return False
        countSimilarity = 0
        for i in range(0, len(vectorFirst)):
            for j in range(0, len(vectorFirst)):
                if (vectorFirst[i] == vectorLast[j]):
                    countSimilarity += 1
                    break
            if (countSimilarity < i + 1):
                return False
        return True
        
    def generateMatrix(self, colsMatrix, rowsMatrix, possiblesValues):
        self.matrix = []
        self.matrix.append(self.generateVector(colsMatrix, possiblesValues))
        while (len(self.matrix) < rowsMatrix):
            vectorAux = self.generateVector(colsMatrix, possiblesValues)
            if (self.checkVector(self.matrix, vectorAux)):
                self.matrix.append(vectorAux)
        return self.matrix


class WrapperOmeganOmegap:

    def __init__(self, cols, rowsOmegap, rowsOmegan, possiblesValues):
        self.cols = cols
        self.rowsOmegap = rowsOmegap
        self.rowsOmegan = rowsOmegan
        self.matrix = GenerateValues(True, 0).generateMatrix(
            cols, rowsOmegan + rowsOmegap, possiblesValues)

    def getOmegan(self):
        return self.matrix[self.rowsOmegap:len(self.matrix)]

    def getOmegap(self):
        return self.matrix[0: self.rowsOmegap]


class AtMostOne:
    def getMatrix(self, sizeSet, numberOfConstraints, possibleNumbers):
        matrix = GenerateValues().generateMatrix(
            sizeSet, numberOfConstraints, possibleNumbers)
        return matrix
