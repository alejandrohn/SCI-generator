from answer import Answer
from writeDzn import ManageWriteDzn
from generateMatrix import WrapperOmeganOmegap
from generateMatrix import AtMostOne
from random import randint

NAMEOFFILEDZN = "Give me the file name"
NUMBEROFATTRIBUTTEQUESTION = 'Give me the number of attributes'
MAXIMUMSIZEVECTORQUESTION = 'Give me the maximum size of support set'
POSITIVEINTANCESQUESTION = 'Give me the number of positive instances'
NEGATIVEINTANCESQUESTION = 'Give me the number of negatives instances'
ATMOSTONEINTANCESQUESTION = 'Give me the number of atMostOne contraints'


class Question:

    global answer

    def __init__(self):
        self.filename = ''
        self.numberAttributeT = 0
        self.maximumSizeSetK = 0
        self.positiveInstancesN = 0
        self.negativeInstancesM = 0
        self.atMostConstraintsC = 0
        self.manageWriteDzn = ManageWriteDzn()

    def getValueOfForm(self, question):
        isCorrect = False
        while(not isCorrect):
            answer = raw_input(question + '\n').__str__()
            try:
                isCorrect = True
                return int(answer)
            except:
                isCorrect = False

    def getFilenName(self, question):
        filename = raw_input(question + '\n').__str__()
        return filename

    def getQuestionsViaInput(self):
        self.filename = self.getFilenName(NAMEOFFILEDZN)
        self.numberAttributeT = self.getValueOfForm(NUMBEROFATTRIBUTTEQUESTION)
        self.maximumSizeSetK = self.getValueOfForm(MAXIMUMSIZEVECTORQUESTION)
        self.positiveInstancesN = self.getValueOfForm(POSITIVEINTANCESQUESTION)
        self.negativeInstancesM = self.getValueOfForm(NEGATIVEINTANCESQUESTION)
        self.atMostConstraintsC = self.getValueOfForm(
            ATMOSTONEINTANCESQUESTION)

        return self.getAnswer()

    def getQuestions(self, filename, t, k, n, m, c):
        self.filename = filename
        self.numberAttributeT = t
        self.maximumSizeSetK = k
        self.positiveInstancesN = n
        self.negativeInstancesM = m
        self.atMostConstraintsC = c
        return self.getAnswer()

    def generateDZNInput(self):
        answer = self.getQuestionsViaInput()
        self.generateDznFile(answer)

    def generateDZNWithValues(self, filename, t, k, n, m, c):
        answer = self.getQuestions(filename, t, k, n, m, c)
        self.generateDznFile(answer)

    def generateDznFile(self, answer):
        omegap, omegan = self.getMatrixsOmegaPN(answer)
        atMostOne = self.getAtMostOne(answer)
        self.manageWriteDzn.writeDzn(
            self.filename, answer, omegap, omegan, atMostOne)

    def getMatrixsOmegaPN(self, answer):
        wrapperMatrixs = WrapperOmeganOmegap(
            answer.numberAttributeT, answer.positiveInstancesN, answer.negativeInstancesM, 1)
        omegap = wrapperMatrixs.getOmegap()
        omegan = wrapperMatrixs.getOmegan()
        return omegap, omegan

    def getAtMostOne(self, answer):
        return AtMostOne().getMatrix(answer.atMostConstraintsC, answer.atMostConstraintsC, answer.numberAttributeT)

    def getAnswer(self):
        return Answer(self.numberAttributeT, self.maximumSizeSetK,
                      self.positiveInstancesN, self.negativeInstancesM,
                      self.atMostConstraintsC)

