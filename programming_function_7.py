##
## top n surfing .
##

def readFile():

    file_name = input('please input your filename')
    file = open(file_name,'r')
    surfer = {}
    for line in file:
        name, grade = line.split('\t')
        surfer[name] = grade
    return surfer

def listTopN():

    surfer = readFile()
    keys = list(surfer.keys())
    values = list(surfer.values())
    sorted_sufer = sorted(surfer.items(),key = lambda x:x[1],reverse=True)
    return sorted_sufer

def main():
    cnt = 0
    dataset = listTopN()
    number = input('please input top N member:')
    for i in dataset:
        if cnt<=int(number):
           cnt += 1
           print(i)
main()
