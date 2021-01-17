##
##  list
##
from programming_function_4 import Student,readfile

def readStudents(filename):
    infile = open(filename,'r')
    students = []
    for line in infile:
        students.append(readfile(line))
    return students

# s=readStudents('grade.txt')
# print(s[0].getname())
# print(s[1].getname())

def writeStudent(filename,students):
    with open(filename,'w') as f:
        for i in students:
            print('{0}\t{1}\t{2}'.format(i.getname(),i.gethours(),i.getgrade()),file=f)

def main():
    print('this program sorts student grade information by GPA')
    filename = input('please input your filename')
    s = readStudents(filename)
    s.sort(key=Student.getgap) ##传入函数
    writefilename = input('please input your write filename')
    writeStudent(writefilename,s)

main()


