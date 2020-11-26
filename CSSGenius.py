class CSSGenius:

    stream = 'Computer Science'

    def __init__(self, classCode):

        self.classCode = classCode

History = CSSGenius(101)
Science = CSSGenius(102)

print(History.stream)
print(Science.stream)
print(History.classCode)
print(Science.classCode)
print(CSSGenius.stream)
