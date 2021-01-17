##
## class
##
class Student():
    def __init__(self):
        self.name = name
        self.hours = hours
        self.grade = grade
    def getname(self):
        return self.name
    def gethours(self):
        return self.hours
    def getgrade(self):
        return self.grade
    def getgap(self):
        gap =  self.grade/self.hours
        return gap

def readfile(line):
    name, hours, grade = line.split('\t')
    return Student(name, float(hours), float(grade))

def main():
    filename = input('please input your filename:')
    file = open(filename, 'r')
    best = readfile(file.readline())
    for line in file:
        s = readfile(line)
        if s.getgap() >= best.getgap():
           best = s
    print(best.getname())
    print(best.getgrade())
    print(best.gethours())
    print(best.getgap())

if __name__=='__main__':
    main()