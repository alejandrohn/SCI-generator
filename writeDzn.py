from printElement import PrintElement

TAnswer = '%number of attributes'
KAnswer = '%maximum size of support set'
NAnswer = '%number of positive instances'
MAnswer = '%number of negative instances'
CAnswer = '%number of atMostOne Constraints'


class ManageWriteDzn:

    global f

    def __init__(self):
        self.printElement = PrintElement()

    def writeDzn(self, fileName, answer, omegap, omegan, atMostOne):
        self.openFile(fileName)
        self.writeParams(answer)
        self.writeLineBreak(1)
        self.writeOmegap(omegap)
        self.writeLineBreak(2)
        self.writeOmegan(omegan)
        self.writeLineBreak(4)
        self.writeAtMostOne(atMostOne)

        self.f.close()

    def writeLine(self, attribute, text, symbol):
        self.f.write(symbol + '=' + attribute.__str__() + '; ' + text + '\n')

    def writeOmegap(self, omegap):
        self.f.write(
            'omegap = ' + self.printElement.printMatrixWithPipe(omegap))

    def writeOmegan(self, omegan):
        self.f.write(
            'omegan = ' + self.printElement.printMatrixWithPipe(omegan))

    def writeParams(self, answer):
        self.writeLine(answer.numberAttributeT, TAnswer, 't')
        self.writeLine(answer.maximumSizeSetK, KAnswer, 'k')
        self.writeLine(answer.positiveInstancesN, NAnswer, 'n')
        self.writeLine(answer.negativeInstancesM, NAnswer, 'm')
        self.writeLine(answer.atMostConstraintsC, CAnswer, 'c')

    def writeLineBreak(self, number):
        for i in range(0, number):
            self.f.write('\n')

    def openFile(self, fileName):
        self.f = open('models/' + fileName + '.dzn', "w+")

    def writeAtMostOne(self, atmostone):
        self.f.write('atMostOne = ' +
                     self.printElement.printMatrixWithBrace1(atmostone))
