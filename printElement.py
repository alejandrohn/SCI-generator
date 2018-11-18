class PrintElement:
    def printMatrixWithPipe(self, matrix):
        stringMatrix = '[ | '
        for i in range(0, len(matrix)):
            temp = matrix[i].__str__()
            if(i == 0):
                stringMatrix = stringMatrix + \
                    temp[1:len(temp) - 1] + '|' + '\n'
            else:
                stringMatrix = stringMatrix + '             ' + \
                    temp[1:len(temp) - 1] + '|' + '\n'
        stringMatrix = stringMatrix + '         ' + '];'
        return stringMatrix

    def printMatrixWithBrace1(self, matrix):
        matrixOfBrace = '[ '
        for i in range(0, len(matrix)):
            temp = matrix[i].__str__()
            if (i < len(matrix) - 1):
                if(i == 0):
                    matrixOfBrace = matrixOfBrace + \
                        '{' + temp[1:len(temp) - 1] + '}' + ',' + '\n'
                else:
                    matrixOfBrace = matrixOfBrace + '              ' + \
                        '{' + temp[1:len(temp) - 1] + '}' + ',' + '\n'

            else:
                matrixOfBrace = matrixOfBrace + '              ' + \
                    '{' + temp[1:len(temp) - 1] + '}' + '];'
        return matrixOfBrace
